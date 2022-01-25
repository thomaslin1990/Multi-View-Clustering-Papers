import scipy.io as scio
import torch
import numpy as np
from scipy import sparse


def load_scene15(data_dir):
    mat = scio.loadmat(data_dir)
    x = [
        torch.from_numpy(mat['X'][0][0].astype('float32')),
        torch.from_numpy(mat['X'][0][1].astype('float32'))
    ]
    y = torch.from_numpy(np.squeeze(mat['Y']).astype('int'))
    return x, y, x[0].shape[0]


def load_landuse21(data_dir):
    mat = scio.loadmat(data_dir)
    x = [
        torch.from_numpy(sparse.csr_matrix(mat['X'][0, 0]).A),
        torch.from_numpy(sparse.csr_matrix(mat['X'][0, 1]).A),
        torch.from_numpy(sparse.csr_matrix(mat['X'][0, 2]).A)
    ]

    y = torch.from_numpy(np.squeeze(mat['Y']).astype('int'))

    return x, y, x[0].shape[0]


def load_caltech101_20(data_dir):
    mat = scio.loadmat(data_dir)
    view_num = len(mat['X'][0])
    x = [torch.from_numpy(mat["X"][0][i]) for i in range(view_num)]
    y = torch.from_numpy(np.squeeze(mat['Y']).astype('int'))
    return x, y, x[0].shape[0]

