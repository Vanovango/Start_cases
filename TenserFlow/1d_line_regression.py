import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

learning_rate = 0.001
training_epochs = 1000


def sigmoid(x):
    return 1. / (1. + np.exp(-x))


x1 = np.random.normal(-4, 2, 1000)
x2 = np.random.normal(4, 2, 1000)
xs = np.append(x1, x2)
ys = np.asarray([0.] * len(x1) + [1.] * len(x2))

plt.scatter(xs, ys, c='g')

tf.compat.v1.disable_eager_execution()
X = tf.compat.v1.placeholder(tf.float32, shape=(None,), name="x")
Y = tf.compat.v1.placeholder(tf.float32, shape=(None,), name="y")
w = tf.Variable([0., 0.], name="parametr", trainable=True)
y_model = tf.sigmoid(w[1] * X + w[0])
cost = tf.reduce_mean(-Y * tf.compat.v1.log(y_model) - (1 - Y) * tf.compat.v1.log(1 - y_model))

train_op = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost)

sess = tf.compat.v1.Session()
init = tf.compat.v1.global_variables_initializer()
sess.run(init)

prev_err = 0
for epoch in range(training_epochs):
    err, _ = sess.run([cost, train_op], {X: xs, Y: ys})
    print(epoch, err)
    if abs(prev_err - err) < 0.0001:
        break
    prev_err = err

w_val = sess.run(w, {X: xs, Y: ys})

sess.close()

all_xs = np.linspace(-10, 10, 100)
plt.plot(all_xs, sigmoid((all_xs * w_val[1] + w_val[0])))
plt.show()
