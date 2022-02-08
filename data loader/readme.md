
**Reference:**

Some code in this code base is from following paper or Github repos.

* "Completer: Incomplete Multi-view Clustering via Contrastive Prediction", <a href="https://github.com/XLearning-SCU/2021-CVPR-Completer">Github</a>

## Introduction

This is a framework of loading multi-view data. As you can see, the file organization is simple.

```c
- mv data
  - data
  - load_data_fn.py
  - MVDataBaseClass.py
  - test.py
  - readme.md
```

- `data`: this is directory contains many source data, generally are '.mat' file
- `load_data_fn.py`: it defines sample function used to load multi-view data.
- `MVDataBaseClass.py`: it defines two classes. Those classes are the basic class of this code base. `MVDataBaseClass` just a abstract super class. `DataShell` is a class representing the framework of other specific dataset class.
- `test.py`: just for some simple test.

## Todolist

- load_mirflickr

## Use

1. download this code base
2. implement a function of loading data.
3. instance a `DataShell