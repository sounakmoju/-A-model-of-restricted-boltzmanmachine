def batch_ite(X,batch_size=64):
    n_samples=X.shape[0]
    for i in np.arrange(0,n_samples,batch_size=64):
        start,end=i,min(i+batch_size,n_sample)
        yield X[start:end]
def train_test_spilit(X,y,test_size=0.2):
    split_i=len(y)-int(len(y)//(1/test_size))
    X_train,X_test=X[:split_i],X[split_i:]
    y_train,y_test=y[:split_i],y[split_i]

    return X_train,y_train,y_train,y_test

