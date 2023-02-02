import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

x_label_0 = np.random.normal(5, 1, 10)
x_label_1 = np.random.normal(2, 1, 10)
xs = np.append(x_label_0, x_label_1)
labels = [0.] * len(x_label_0) + [1.] * len(x_label_1)

plt.scatter(xs, labels)

learning_rate = 0.001
training_epochs = 1000

tf.compat.v1.disable_eager_execution()
X = tf.compat.v1.placeholder("float")
Y = tf.compat.v1.placeholder("float")


def model(X, w):
    return tf.add(
        tf.multiply(w[1], tf.pow(X, 1)),
        tf.multiply(w[0], tf.pow(X, 0)))


w = tf.Variable([0., 0.], name="parametrs")
y_model = model(X, w)
cost = tf.reduce_sum(tf.square(Y - y_model))

train_op = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost)

sess = tf.compat.v1.Session()
init = tf.compat.v1.global_variables_initializer()
sess.run(init)

for epoch in range(training_epochs):
    sess.run(train_op, feed_dict={X: xs, Y: labels})
    current_cost = sess.run(cost, feed_dict={X: xs, Y: labels})
    if epoch % 100 == 0:
        print(epoch, current_cost)

w_val = sess.run(w)
print('learned parameters', w_val)

correct_prediction = tf.equal(Y, tf.compat.v1.to_float(tf.greater(y_model, 0.5)))
accuracy = tf.reduce_mean(tf.compat.v1.to_float(correct_prediction))
print('accuracy', sess.run(accuracy, feed_dict={X: xs, Y: labels}))

sess.close()

all_xs = np.linspace(0, 7, 100)
plt.plot(all_xs, all_xs*w_val[1] + w_val[0])
plt.show()