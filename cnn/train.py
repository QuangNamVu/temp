import os
import tensorflow as tf
from load_mat import LOAD_TRAIN

learning_rate = 0.001
iterations = 50000
batch_size = 50
display_step = 1000

channels = 3
image_size = 32
n_classes = 10
dropout = 0.8
hidden = 128
depth_1 = 16
depth_2 = 32
depth_3 = 64
filter_size = 5
normalization_offset = 0.0  # beta
normalization_scale = 1.0  # gamma
normalization_epsilon = 0.001  # epsilon


def weight_variable(shape):
    return tf.Variable(tf.truncated_normal(shape, stddev=0.1))


def bias_variable(shape):
    return tf.Variable(tf.constant(1.0, shape=shape))


def convolution(x, w):
    return tf.nn.conv2d(x, w, strides=[1, 1, 1, 1], padding="SAME")


def max_pool(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                          padding="SAME")


# train_data = LOAD_TRAIN("/tmp/data/", n_classes)
train_data = LOAD_TRAIN("../data/", n_classes)


# model
X = tf.placeholder(tf.float32, [None, image_size, image_size, channels]) # 32 32 3
y = tf.placeholder(tf.float32, [None, n_classes])


# Weights & Biases
weights = {
    "layer1": weight_variable([filter_size, filter_size, channels, depth_1]),
    "layer2": weight_variable([filter_size, filter_size, depth_1, depth_2]),
    "layer3": weight_variable([filter_size, filter_size, depth_2, depth_3]),
    "layer4": weight_variable([image_size // 8 * image_size // 8 * depth_3,
                               hidden]),
    "layer5": weight_variable([hidden, n_classes])
}

biases = {
    "layer1": bias_variable([depth_1]),
    "layer2": bias_variable([depth_2]),
    "layer3": bias_variable([depth_3]),
    "layer4": bias_variable([hidden]),
    "layer5": bias_variable([n_classes])
}


def normalize(x):
    """ Applies batch normalization """
    mean, variance = tf.nn.moments(x, [1, 2, 3], keep_dims=True)
    return tf.nn.batch_normalization(x, mean, variance, normalization_offset,
                                     normalization_scale,
                                     normalization_epsilon)


def cnn(x):
    # Batch normalization
    x = normalize(x)

    # Convolution 1 -> RELU -> Max Pool
    convolution1 = convolution(x, weights["layer1"])
    relu1 = tf.nn.relu(convolution1 + biases["layer1"])
    maxpool1 = max_pool(relu1)

    # Convolution 2 -> RELU -> Max Pool
    convolution2 = convolution(maxpool1, weights["layer2"])
    relu2 = tf.nn.relu(convolution2 + biases["layer2"])
    maxpool2 = max_pool(relu2)

    # Convolution 3 -> RELU -> Max Pool
    convolution3 = convolution(maxpool2, weights["layer3"])
    relu3 = tf.nn.relu(convolution3 + biases["layer3"])
    maxpool3 = max_pool(relu3)

    # Fully Connected Layer
    shape = maxpool3.get_shape().as_list()
    reshape = tf.reshape(maxpool3, [-1, shape[1] * shape[2] * shape[3]])
    fc = tf.nn.relu(tf.matmul(reshape, weights["layer4"]) + biases["layer4"])

    # Dropout Layer
    keep_prob_constant = tf.placeholder(tf.float32)
    dropout_layer = tf.nn.dropout(fc, keep_prob_constant)

    return (tf.matmul(dropout_layer, weights["layer5"]) + biases["layer5"],
            keep_prob_constant)
# Build the graph for the deep net
y_conv, keep_prob = cnn(X)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,
                                                              logits=y_conv))

optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y, 1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    start = 0
    end = 0

    train_accuracies = []
    train_losses = []
    test_accuracies = []
    test_losses = []

    saver.restore(sess, "39999/my_model_final.ckpt")
    # for i in range(iterations):
    for i in range(10000):
        # Construct the batch
        file_name = str(i + 40000)
        if start == train_data.examples:
            start = 0

        end = min(train_data.examples, start + batch_size)

        batch_x = train_data.data[start:end]
        batch_y = train_data.labels[start:end]

        start = end

        sess.run(optimizer, feed_dict={X: batch_x, y: batch_y, keep_prob: dropout})

        if (i + 1) % display_step == 0:
            _accuracy, _cost = sess.run([accuracy, cost], feed_dict={X: batch_x, y: batch_y, keep_prob: 1.0})
            print("Step: {0:6d}, Training Accuracy: {1:5f}, Batch Loss: {2:5f}"
                  .format(i + 1, _accuracy, _cost))
            train_accuracies.append(_accuracy)
            train_losses.append(_cost)
            os.mkdir(file_name)
            save_path = saver.save(sess, file_name +"/my_model_final.ckpt")
            save_path = saver.save(sess, "../checkpoint/my_model_final.ckpt")
