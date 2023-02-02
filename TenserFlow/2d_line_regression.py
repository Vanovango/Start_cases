# region Libraries
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# endregion

learning_rate = 0.1
training_epochs = 2000


def sigmoid(x):
    return 1. / (1. + np.exp(-x))


# region Init Fake Data

x1_x = np.random.normal(5, 1, 1000)
x1_y = np.random.normal(5, 1, 1000)
x2_x = np.random.normal(1, 1, 1000)
x2_y = np.random.normal(1, 1, 1000)
x1s = np.append(x1_x, x2_x)
x2s = np.append(x1_y, x2_y)
ys = np.asarray([0.] * len(x1_x) + [1.] * len(x2_x))

# endregion

# region Variables
tf.compat.v1.disable_eager_execution()
x1 = tf.compat.v1.placeholder(tf.float32, shape=(None,), name="x1")
x2 = tf.compat.v1.placeholder(tf.float32, shape=(None,), name="x2")
Y = tf.compat.v1.placeholder(tf.float32, shape=(None,), name="y")
w = tf.Variable([0., 0., 0.], name="w", trainable=True)
# endregion

# region Learning
y_model = tf.sigmoid(w[2] * x2 + w[1] * x1 + w[0])
cost = tf.reduce_mean(-tf.compat.v1.log(y_model * Y + (1 - y_model) * (1 - Y)))
train_op = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost)
# endregion

# region Session
sess = tf.compat.v1.Session()
init = tf.compat.v1.global_variables_initializer()
sess.run(init)

prev_err = 0
for epoch in range(training_epochs):
    err, _ = sess.run([cost, train_op], {x1: x1s, x2: x2s, Y: ys})
    print(epoch, err)
    if abs(prev_err - err) < 0.0001:
        break
    prev_err = err

w_val = sess.run(w, {x1: x1s, x2: x2s, Y: ys})

sess.close()
# endregion

# region Граничные точки
x1_boundary, x2_boundary = [], []
for x1_test in np.linspace(0, 10, 100):
    for x2_test in np.linspace(0, 10, 100):
        z = sigmoid(-x2_test * w_val[2] - x1_test * w_val[1] - w_val[0])
        if abs(z - 0.5) < 0.01:
            x1_boundary.append(x1_test)
            x2_boundary.append(x2_test)
# endregion

# region Show
plt.scatter(x1_boundary, x2_boundary, c='b', marker='o', s=20)
plt.scatter(x1_x, x1_y, c='r', marker='x', s=20)
plt.scatter(x2_x, x2_y, c='g', marker='1', s=20)

plt.show()
# endregion
