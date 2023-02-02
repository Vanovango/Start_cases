import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import sys

learning_rate = 0.001
train_epochs = 1000
num_coefs = 5

sys.stdin = open("data_set_interpoletion.txt")
n = int(input())
x, y = [], []
for i in range(n):
    a, b = map(float, input().split())
    x.append(a)
    y.append(b)

tf.compat.v1.disable_eager_execution()
X = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)


def mocel(X, w):
    terms = []
    for i in range(num_coefs):
        term = tf.multiply(w[i], tf.pow(X, i))
        terms.append(term)
    return tf.add_n(terms)


w = tf.Variable([0.] * num_coefs)
y_model = mocel(X, w)

cost = tf.square(Y - y_model)
train_op = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost)

sess = tf.compat.v1.Session()
init = tf.compat.v1.global_variables_initializer()
sess.run(init)

for epoch in range(train_epochs):
    for (xx, yy) in zip(x, y):
        sess.run(train_op, feed_dict={X: xx, Y: yy})

w_val = sess.run(w)

sess.close()

print(w_val)
plt.scatter(x, y, c='g')
y_out = 0
for i in range(num_coefs):
    y_out += w_val[i] * np.power(x, i)
plt.plot(x, y_out, 'r')
plt.show()
