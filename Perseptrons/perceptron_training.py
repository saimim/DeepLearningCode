# -*- coding: utf-8 -*-
"""Perceptron_training.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M0kIbmq_zBes-Nqkps4X_cWh79vfG_4n
"""

from sklearn.datasets import make_classification
import numpy as np
x,y = make_classification(n_samples=100, n_features=2, n_informative=1,n_redundant=0,n_classes=2,n_clusters_per_class=1, random_state=41,hypercube=False,class_sep=10)

x

y

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.scatter(x = x[:,0],y =x[:,1],c=y,cmap='winter',s=100)

def perceptron(x,y):
  x = np.insert(x,0,1,axis = 1)
  weights = np.ones(x.shape[1])
  lr = 0.1

  for i in range(1000):
    j = np.random.randint(0,100)
    y_hat = step(np.dot(x[j],weights))
    weights = weights + lr*(y[j]-y_hat)*x[j]

  return weights[0],weights[1:]

def step(z):
  return 1 if z>0 else 0

intercept_,coef_ = perceptron(x,y)

m = -(coef_[0]/coef_[1])
b = -(intercept_/coef_[1])

x_input = np.linspace(-3,3,100)
y_input = m*x_input + b

plt.figure(figsize=(10,6))
plt.plot(x_input,y_input,color='red',linewidth=3)
plt.scatter(x[:,0],x[:,1],c=y,cmap='winter',s=100)
plt.ylim(-3,2)

def perceptron(x,y):
  m= []
  b= []
  x = np.insert(x,0,1,axis=1)
  weights = np.ones(x.shape[1])
  lr = .1

  for i in range(200):
    j = np.random.randint(0,100)
    y_hat = step(np.dot(x[j],weights))
    weights = weights + lr*(y[j]-y_hat)*x[j]

    m.append(-weights[1]/weights[2])
    b.append(weights[0]/weights[2])

  return m,b

m,b = perceptron(x,y)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib notebook
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(9,5))

x_i = np.arange(-3, 3, 0.1)
y_i = x_i*m[0] +b[0]
ax.scatter(x[:,0],x[:,1], c=y,cmap='winter',s=100)
line, =ax.plot(x_i,x_i*m[0] +b[0],'r-', linewidth=2)
plt.ylim(-3,3)
def update(i):
  label = 'epoch {0}'.format(i + 1)
  line.set_ydata(x_i*m[i] + b[i])
  ax.set_xlabel(label)

anim = FuncAnimation(fig, update, repeat=True, frames=200,interval=100)

anim