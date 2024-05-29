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


def plot_shape(ax, title: str, shape: np.array) -> None:
    """
    Plot the shape with the given title (string) and shape (numpy array)
    """
    ax.clear()
    ax.plot(shape[:, 0], shape[:, 1])
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.axis('equal')


def rotate(shape: np.array, angle: float) -> np.array:
    """
    Rotate the shape by the given angle (in degrees)
    """
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


def key_press(event):
    global current_transformation, current_original
    if event.key == 'right':
        current_transformation = (current_transformation + 1) % len(transformations)
    elif event.key == 'left':
        current_transformation = (current_transformation - 1) % len(transformations)
    elif event.key == 'a':
        current_original = (current_original + 1) % len(originals)
    elif event.key == 'd':
        current_original = (current_original - 1) % len(originals)
    elif event.key == 'z':
        current_transformation = (current_transformation + 1) % len(transformations)
        current_original = (current_original + 1) % len(originals)
    elif event.key == 'x':
        current_transformation = (current_transformation - 1) % len(transformations)
        current_original = (current_original - 1) % len(originals)
    update_plot()


def update_plot():
    ax1.clear()
    ax2.clear()
    title_og, original_shape = originals[current_original]
    plot_shape(ax1, title_og, original_shape)

    title_t, transformed_shape = transformations[current_transformation]
    plot_shape(ax2, title_t, transformed_shape)
    plt.draw()


originals = [
    ("Original Batman", batman),
    ("Original Star", star)
]
transformations = [
    ("Rotated Batman 180 degrees", rotate(batman, 180)),
    ("Rotated Star 90 degrees", rotate(star, 90))
]

current_original = 0
current_transformation = 0

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
plot_shape(ax1, originals[0][0], originals[0][1])
plot_shape(ax2, transformations[0][0], transformations[0][1])

fig.canvas.mpl_connect('key_press_event', key_press)
plt.show()
