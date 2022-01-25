import torch
from torch.utils.data import Dataset
from abc import ABCMeta, abstractmethod
import numpy as np
from numpy.random import randint
from sklearn.preprocessing import OneHotEncoder
from typing import Union
import scipy.io as scio


class MVDataBaseClass(Dataset, metaclass=ABCMeta):

    def __init__(self):
        super(MVDataBaseClass, self).__init__()

    def __len__(self):
        if self.sample_num:
            return self.sample_num
        else:
            raise Exception("Not calculated length of dataset!")

    def __getitem__(self, index):
        pass

    @abstractmethod
    def _gen_miss_matrix(self):
        pass

    @abstractmethod
    def _load_miss_matrix(self):
        pass

    @abstractmethod
    def get_dim(self):
        pass

    def get_mask(self):
        """Randomly generate incomplete data information, simulate partial
        view data with complete view data. **This method may be not a good choice for
        more than two view situations.**
        Returns:
            mask: (tensor) shape is (sample_num, view_num)
        """
        view_num = len(self.x)
        data_len = self.__len__()
        missing_rate = self.missing_info

        missing_rate = missing_rate / 2
        one_rate = 1.0 - missing_rate
        if one_rate <= (1 / view_num):
            enc = OneHotEncoder()
            view_preserve = enc.fit_transform(randint(0, view_num, size=(data_len, 1))).toarray()
            return view_preserve
        error = 1

        matrix = None
        if one_rate == 1:
            matrix = randint(1, 2, size=(data_len, view_num))
            return matrix
        while error >= 0.005:
            enc = OneHotEncoder()
            view_preserve = enc.fit_transform(randint(0, view_num, size=(data_len, 1))).toarray()
            one_num = view_num * data_len * one_rate - data_len
            ratio = one_num / (view_num * data_len)
            matrix_iter = (randint(0, 100, size=(data_len, view_num)) < int(ratio * 100)).astype(np.int)
            a = np.sum(((matrix_iter + view_preserve) > 1).astype(np.int))
            one_num_iter = one_num / (1 - a / one_num)
            ratio = one_num_iter / (view_num * data_len)
            matrix_iter = (randint(0, 100, size=(data_len, view_num)) < int(ratio * 100)).astype(np.int)
            matrix = ((matrix_iter + view_preserve) > 0).astype(np.int)
            ratio = np.sum(matrix) / (view_num * data_len)
            error = abs(one_rate - ratio)

        return torch.from_numpy(matrix)


class DataShell(MVDataBaseClass):
    """
    The data and missing matrix dependent on the function of loading data. That's how
    the name 'DataShell' comes from.
    """

    def __init__(self, data_dir, load_data_function, missing: Union[str, float], transform=None):
        """
        Args:
            data_dir: (str) path to data
            load_data_function: (function)
            missing: (str, float) if this is str, that means path to missing matrix.
                else that means the missing rate.
            transform: (transform)
        """
        super(DataShell, self).__init__()

        self.transform = transform
        self.missing_info = missing
        self._load_data = load_data_function

        # list contains tensor
        self.x: list
        self.y: torch.Tensor
        self.miss_matrix: Union[torch.Tensor, None]

        self.x, self.y, self.sample_num = self._load_data(data_dir)

        if type(missing) == str:
            self._load_miss_matrix()
        else:
            self._gen_miss_matrix()

    def __getitem__(self, index):

        if not self.transform:
            ret_list = []
            for item in self.x:
                ret_list.append(self.transform(item))
            return tuple(ret_list), self.y
        else:
            return tuple(self.x), self.y

    def _gen_miss_matrix(self):
        self.miss_matrix = self.get_mask()

    def _load_miss_matrix(self):
        """
        The file stored the missing matrix must be '.mat'. This method requires the missing matrix
        file existed to be easily loaded.
        """
        mat = scio.loadmat(self.missing_info)
        self.miss_matrix = torch.from_numpy(mat)

    def get_dim(self):
        """
        Returns: (list) contains dimension of each view feature
        """
        dim_list = []
        for item in self.x:
            dim_list.append(item.shape[1])
        return dim_list
