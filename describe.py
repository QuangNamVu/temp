import numpy
import scipy.io as sio
from matplotlib import pyplot as plt


def get_record(mat):
    print(len(mat['y']))


def show_image(mat, n):
    print(mat['y'][n])
    plt.imshow(mat['X'][:, :, :, n], interpolation='nearest')
    plt.show()


train = sio.loadmat("../data/train_32x32.mat")
test = sio.loadmat("../data/test_32x32.mat")

print(numpy.shape(train['X']))
# (32, 32, 3, 73257)
print(numpy.shape(test['X']))
# (32, 32, 3, 26032)

print(numpy.shape(train['y']))
# (73257, 1)
# RGB
