import numpy as np
from Data import *
from Decision_tree import *

d=Dataset("./clean_dataset.txt")
for X_train, X_test in d.kf_split(10):
    X_train, X_valid=d.tv_split(X_train,10)
    dc_tree=Decision_tree()

    # dc_tree.dt_training(X_train)
    # dc_tree.pruning(X_valid)
    # dc_tree.tree.visualize()
    # dc_tree.dt_evluation(X_test)

    dc_tree.build()