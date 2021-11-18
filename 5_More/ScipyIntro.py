import numpy as np
np.random.seed(0)
import scipy as sc
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt


def plot_rv(xk, yk):
    fig, ax = plt.subplots(1, 1)
    ax.scatter(xk, yk, marker='o', s=5)
    ax.vlines(xk, 0, yk)
    plt.show()


x = np.random.randn(1_000_000)


class gaussian_gen(scipy.stats.rv_continuous):
    "Gaussian distribution"
    def _pdf(self, x):
        return np.exp(-x**2 / 2.) / np.sqrt(2.0 + np.pi)


gaussian = gaussian_gen(name="gaussian")
xi = np.linspace(-5.0, 5.0, 1000)
pdf_x = gaussian.pdf(xi)
plot_rv(xi, pdf_x)
