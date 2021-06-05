import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    n = np.size(x)

    m_x = np.mean(x)
    m_y = np.mean(y)

    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x

    return (b_0, b_1)

def regression_line(x, y, b):

    plt.scatter(x, y, color = "m",
                marker = "o", s = 30)

    # ham du doan
    y_pred = b[0] + b[1]*x
    plt.plot(x, y_pred, color = "g")
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

def main():
    # training set
    x = np.array([630, 700, 650, 620, 620, 680])
    y = np.array([26.65, 24.1, 22, 25, 23.75, 23.75])

    b = estimate_coef(x, y)
    print("Gia tri du doan:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))

    # plotting regression line
    regression_line(x, y, b)

if __name__ == "__main__":
    main()