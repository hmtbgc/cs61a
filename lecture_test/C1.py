import numpy as np
import matplotlib.pyplot as plt

def normfun(x, mu, sigma):
    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf

def printf(x, mu, sigma):
    y = normfun(x, mu, sigma)
    plt.plot(x, y)

x = np.arrange(0, 1, 0.001)
printf(x, 0, 1)
