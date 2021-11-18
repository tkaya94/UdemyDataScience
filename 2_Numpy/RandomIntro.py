import numpy as np
np.random.seed(42)
import matplotlib.pyplot as plt


def plot_hist(x, num_bins):
    y = np.histogram(x, bins=num_bins)
    plt.vlines(y[1][:-1], ymin=0, ymax=y[0])


def plot_scatter(x):
    fig, ax = plt.subplots(1, 1)
    plt.scatter(x[:, 0], x[:, 1], s=5)
    ax.axis('tight')


a = np.arange(10)
print(a)

x = np.random.randn(1_000_000)
bins = 1000
plot_hist(x, bins)

x = np.random.normal(loc=5.0, scale=0.2, size=1_000_000)
