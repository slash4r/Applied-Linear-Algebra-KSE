import numpy as np
import matplotlib.pyplot as plt

batman = np.array([
    [0, 0],
    [1, 0.2],
    [0.4, 1],
    [0.5, 0.4],
    [0, 0.8],
    [-0.5, 0.4],
    [-0.4, 1],
    [-1, 0.2],
    [0, 0]
],
)

star = np.array([
    [0, 1],
    [0.2, 0.2],
    [1, 0.2],
    [0.4, -0.2],
    [0.6, -1],
    [0, -0.5],
    [-0.6, -1],
    [-0.4, -0.2],
    [-1, 0.2],
    [-0.2, 0.2],
    [0, 1]
])


def main():
    plt.figure(figsize=(10, 5))

    # for badman
    plt.subplot(1, 2, 1)
    #               X            Y
    plt.plot(batman[:, 0], batman[:, 1])
    plt.title("Batman")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')

    # second plot
    plt.subplot(1, 2, 2)
    plt.plot(star[:, 0], star[:, 1])
    plt.title("Star")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')

    plt.show()


if __name__ == "__main__":
    main()