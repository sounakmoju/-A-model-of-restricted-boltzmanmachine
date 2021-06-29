import numpy as np
from sig_activation import Sigmoid
from utils import batch_ite,train_test_spilit
from gibs import gibbs_sampler
sigmoid = Sigmoid()
class RBM():
     def __init__(self, n_hidden=128, learning_rate=0.1,n_iterations=100):
         self.n_iterations=n_iterations
         self.lr=learning_rate
         self.n_hidden=n_hidden

     def weights(self, X):
         input1=X.shape[1]
         self.W=np.random.normal(scale=0.1,size=(input1,n_hidden))
         self.b_in=np.zeros(input_1)
         self.h=np.zeros(n_hidden)
    
          
     def fit(self,X,y):
         self.weights(X)
         
         self.training_errors=[]
         for _ in range(n_iterations):
              batch_errors=[]
              
             for x_i in batch_ite(X,batch_size=64):
                 positive_hidden=sigmoid(x_i.dot(self.W)+self.h)
                 positive_grad=x_i.T.dot(positive_hidden)
                 x_=gibbs_sampler(x_i)
                 negative_hidden=sigmoid(x_.dot(self.W)+self.h)
                 negative_grad=x_.T.dot(negetive_hidden)
                 self.W+=self.lr*(positive_hidden-negative_hidden)
                 self.b_in+=self.lr*(x_i.sum(axis=0)- x_.sum(axis=0))
                 self.h+=self.lr*(positive_hidden.sum(axis=0)-negative_hidden.sum(axis=0))
             batch_errors.append(np.mean((x_i -x_) ** 2))
        self.training_errors=append(np.mean(batch_errors))
             
                      
                 
