import numpy as np
import scipy.io as sio

class LOAD_TRAIN:

    def __init__(self, path, n_classes):
        self.n_classes = n_classes
        train = sio.loadmat(path + "train_32x32.mat")
        print("load" + path + "train_32x32.mat")
        self.labels = self.__mat_01(train['y'])
        self.examples = train['X'].shape[3]
        self.data = self.__store_data(train['X'].astype("float32"), self.examples)

    def __mat_01(self, data):
        n = data.shape[0] # 73257 | 26032
        n_10 = np.zeros(shape=(n, self.n_classes)) # n , 10
        for s in range(n):
            temp = np.zeros(self.n_classes)
            num = data[s][0]
            if num == 10: # 10 thay = 0
                temp[0] = 1
            else:
                temp[num] = 1
            n_10[s] = temp
        return n_10

    def __store_data(self, data, num_of_examples):
        d = []
        for i in range(num_of_examples):
                d.append(data[:, :, :, i])
        return np.asarray(d)
class LOAD_TEST:

    def __init__(self, path, n_classes):
        self.n_classes = n_classes

        test = sio.loadmat(path + "test_32x32.mat")
        print("load" + path + "test_32x32.mat")
        self.labels = self.__mat_01(test['y'])
        self.examples = test['X'].shape[3]
        self.data = self.__store_data(test['X'].astype("float32"), self.examples)


    def __mat_01(self, data):
        n = data.shape[0] # 26032
        n_10 = np.zeros(shape=(n, self.n_classes)) # n , 10
        for s in range(n):
            temp = np.zeros(self.n_classes)
            num = data[s][0]
            if num == 10: # 10 thay = 0
                temp[0] = 1
            else:
                temp[num] = 1
            n_10[s] = temp
        return n_10

    def __store_data(self, data, num_of_examples):
        d = []
        for i in range(num_of_examples):
                d.append(data[:, :, :, i])
        return np.asarray(d)
class LOAD_MAT:

    def __init__(self, path, n_classes):
        self.n_classes = n_classes

        train = sio.loadmat(path + "train_32x32.mat")
        print("load" + path + "train_32x32.mat")
        self.train_labels = self.__mat_01(train['y'])
        self.train_examples = train['X'].shape[3]
        self.train_data = self.__store_data(train['X'].astype("float32"), self.train_examples)

        test = sio.loadmat(path + "test_32x32.mat")
        print("load" + path + "test_32x32.mat")
        self.test_labels = self.__mat_01(test['y'])
        self.test_examples = test['X'].shape[3]
        self.test_data = self.__store_data(test['X'].astype("float32"), self.test_examples)


    def __mat_01(self, data):
        n = data.shape[0] # 73257 | 26032
        n_10 = np.zeros(shape=(n, self.n_classes)) # n , 10
        for s in range(n):
            temp = np.zeros(self.n_classes)
            num = data[s][0]
            if num == 10: # 10 thay = 0
                temp[0] = 1
            else:
                temp[num] = 1
            n_10[s] = temp
        return n_10

    def __store_data(self, data, num_of_examples):
        d = []
        for i in range(num_of_examples):
                d.append(data[:, :, :, i])
        return np.asarray(d)

