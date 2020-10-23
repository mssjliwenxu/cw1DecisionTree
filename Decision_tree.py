import numpy as np

class Node():
    def __init__(self, dataval): #if the node is a leaf node, dataval=label. else, dataval=[i,split] correspondig to the choosing attribute and value
        self.dataval = dataval
        self.rightval = None  #xi>=split
        self.leftval = None   #xi<split

class Bi_tree():
    def __init__(self):
        self.rootval = None

    # def visualize(self):

class Decision_tree():
    def __init__(self):
        self.build()

    def build(self):
        self.tree=Bi_tree()


    def dt_training(self,X_train,depth):
        init=X_train[0][-1]
        all_same=True
        for i in X_train[:][-1]:
            if i !=init:
                all_same=False
        if all_same:
            return Node(init)

        split=self.find_split(X_train)
        ldataset,rdataset=self.split_data(X_train,split)

        new_node=Node(split)
        if self.tree.rootval==None:
            self.tree.rootval=new_node

        new_node.leftval=self.dt_training(ldataset,depth+1)
        new_node.rightval=self.dt_training(rdataset,depth+1)
        return new_node

    # def split_data(self,X_train, split):
    #
    #
    # def find_split(self,X_train):


    # def dt_evluation(self,X_test, depth):


    # def dt_pruning(self,X_valid):

