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
])

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


def plot_shape(title: str, shape: np.array) -> None:
    """
    Plot the shape with the given title (string) and shape (numpy array)
    """
    #               X            Y
    plt.plot(shape[:, 0], shape[:, 1])
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')


def rotate(shape: np.array, angle: float) -> np.array:
    """
    Rotate the shape by the given angle (in degrees)
    """
    # to radians
    angle = np.radians(angle)

    cos = np.cos(angle)
    sin = np.sin(angle)

    # rotation matrix
    rotation_matrix = np.array([
        [cos, -sin],
        [sin, cos]
    ])

    rotated_shape = rotation_matrix @ shape.T  # error here
    return rotated_shape.T


def main():
    plt.figure(figsize=(10, 5))

    # for badman
    plt.subplot(1, 2, 1)
    plot_shape("Batman", batman)

    # second plot
    plt.subplot(1, 2, 2)
    plot_shape("Star", star)

    plt.show(block=False)
    plt.pause(2)
    plt.clf()

    plt.subplot(1, 2, 1)
    plot_shape("Batman", batman)

    plt.subplot(1, 2, 2)
    plot_shape("Batman", rotate(batman, 180))
    plt.show()


if __name__ == "__main__":
    main()
