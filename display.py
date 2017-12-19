import scipy.io as sio
import numpy as np
from matplotlib import pyplot as plt
def show_shape(mat):
    print("get shape")
    print(np.shape(mat))


def get_record(mat):
    print(len(mat['y']))


def show_image(mat, n):
    print(mat['y'][n])
    plt.imshow(mat['X'][:, :, :, n], interpolation='nearest')
    plt.show()


train = sio.loadmat("../data/train_32x32.mat")
test = sio.loadmat("../data/test_32x32.mat")

show_shape(train['X'])
# (32, 32, 3, 73257)
show_shape(train['y'])
# (73257, 1)

# for i in range(26000, 26010):
    # show_image(test, i)


# for i in range(73100, 73210):
    # if(train['y'][i] == 10):
        # show_image(train, i)

# for i in range(25900, 26010):
    # if(test['y'][i] == 10):
        # show_image(test, i)
