import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

learning_rate = 0.01
training_epochs = 40

trX = np.linspace(-1, 1, 101)

num_coefs = 6
trY_coefs = [1, 2, 3, 4, 5, 6]
trY = 0

for i in range(num_coefs):
    trY += trY_coefs[i] * np.power(trX, i)

trY += np.random.randn(*trX.shape) * 1.5

# plt.scatter(trX, trY)
# plt.show()

tf.compat.v1.disable_eager_execution()
X = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)


def model(X, w):
    terms = []
    for i in range(num_coefs):
        term = tf.multiply(w[i], tf.pow(X, i))
        terms.append(term)
    return tf.add_n(terms)


w = tf.Variable([0.] * num_coefs)
y_model = model(X, w)

# cost = tf.square(tf.pow(Y - y_model, 2))
cost = tf.square(Y - y_model)
train_op = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost)

sess = tf.compat.v1.Session()
init = tf.compat.v1.global_variables_initializer()
sess.run(init)

for epoch in range(training_epochs):
    for (х, у) in zip(trX, trY):
        sess.run(train_op, feed_dict={X: х, Y: у})

w_val = sess.run(w)
print(w_val)

sess.close()

plt.scatter(trX, trY)
trY2 = 0
for i in range(num_coefs):
    trY2 += w_val[i] * np.power(trX, i)
plt.plot(trX, trY2, 'r')
plt.show()
