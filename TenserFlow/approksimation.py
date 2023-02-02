import sys

import matplotlib.pyplot as plt
import tensorflow as tf

learning_rate = 0.01
training_epochs = 500

sys.stdin = open('data_set_approksimaton.txt')
n = int(input())
x, y = [], []
for i in range(n):
    a, b = map(float, input().split())
    x.append(a)
    y.append(b)

tf.compat.v1.disable_eager_execution()
X = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)


def model(X, k, b):
    tmp = tf.multiply(k, X)
    return tf.add(tmp, b)


k = tf.Variable(0., name='K')
b = tf.Variable(0., name='B')

y_model = model(X, k, b)
cost = tf.square(Y - y_model)

train_op = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost)

sess = tf.compat.v1.Session()
init = tf.compat.v1.global_variables_initializer()
sess.run(init)

for epoch in range(training_epochs):
    for (xx, yy) in zip(x, y):
        sess.run(train_op, feed_dict={X: xx, Y: yy})

k_val = sess.run(k)
b_val = sess.run(b)

sess.close()

print(f"k = {k_val}     b = {b_val}")

x_ar = [i for i in range(0, 10)]
plt.scatter(x, y)
y_learn = [k_val * i + b_val for i in x_ar]
plt.plot(x_ar, y_learn, 'g')
# plt.xlim(0, 10)
# plt.ylim(0, 50)
plt.show()
