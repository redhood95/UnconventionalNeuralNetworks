from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as pyplot
import numpy as np

mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)

batch_xs, batch_ys = mnist.train.next_batch(500000)


with open("classify/input.txt","a") as f:
    for i, data, in enumerate(batch_xs):

        data = np.rint(batch_xs[0]).astype(int)
        labl=np.rint(batch_ys[0]).astype(int)
        pixels=data.reshape((28,28))
        index_value = np.argmax(label)
        new_label=np.array(100*[index_value]).reshape((10,10))
        str_img = str(pixels).replace(" ","")
        str_label= str(new_label).replace(" ","")
