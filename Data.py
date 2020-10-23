import numpy as np

class Dataset():
    def __init__(self,filepath):
        self.data=np.loadtxt(filepath)

    def kf_split(self, k): #k-fold cross validation
        size=len(self.data)//k
        return ((np.concatenate((self.data[0:i*size],self.data[i*size+size:])), self.data[i*size:i*size+size])
                       for i in range(k))

    def tv_split(self, X_train,k): #split training dataset into training set and  validation set for pruning
        size=len(self.data)//k
        return X_train[size:], X_train[0:size]
