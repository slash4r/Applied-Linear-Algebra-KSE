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


def plot_shape(ax, title: str, shape_og: np.ndarray, shape_tr: np.ndarray = None) -> None:
    """
    Plot the shape with the given title (string) and shape (numpy array)
    """
    ax.clear()
    if shape_tr is not None:
        ax.plot(shape_tr[:, 0], shape_tr[:, 1], c='r')
    ax.plot(shape_og[:, 0], shape_og[:, 1])
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.axis('equal')


def rotate(shape: np.ndarray, angle: float) -> np.ndarray:
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


def scale(shape: np.ndarray, x: float) -> np.ndarray:
    """
    Scale the shape by the given factor x
    """
    return shape * x


def reflection(shape: np.ndarray, axis: np.ndarray) -> np.ndarray:

    x, y = axis[0], axis[1]
    matrix = np.array([
            [x**2 - y**2, 2 * x * y],
            [2 * x * y, y**2 - x**2]
        ])

    transformation_matrix = matrix / (x**2 + y**2)
    reflected_shape = transformation_matrix @ shape.T
    return reflected_shape.T


def shear(shape: np.ndarray, coord: str, factor: float) -> np.ndarray:
    """
    Shear the shape by the given factor in the given direction
    """
    if coord == 'x':
        shear_matrix = np.array([
            [1, 0],
            [factor, 1]
        ])
    elif coord == 'y':
        shear_matrix = np.array([
            [1, factor],
            [0, 1]
        ])
    else:
        raise ValueError("Invalid parameter coord. Must be 'x' or 'y'")
    sheared_shape = shear_matrix @ shape.T
    return sheared_shape.T


def custom_transform(shape: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """
    Apply a custom transformation to the shape using the given matrix
    """
    transformed_shape = matrix @ shape.T
    return transformed_shape.T


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
    plot_shape(ax2, title_t, original_shape, transformed_shape)
    plt.draw()


originals = [
    ("Original Batman", batman),
    ("Original Star", star)
]
transformations = [
    ("Rotated Batman 180 degrees", rotate(batman, 180)),
    ("Rotated Star 90 degrees", rotate(star, 90)),

    ("Scaled Batman 2x", scale(batman, 2)),
    ("Scaled Star 0.5x", scale(star, 0.5)),

    ("Reflected Batman over xy-axis", reflection(batman, np.array([1, 1]))),
    ("Reflected Star over x-axis", reflection(star, np.array([1, 0]))),

    ("Sheared Batman in x-direction by 3", shear(batman, 'x', 0.5)),
    ("Sheared Star in y-direction by 1", shear(star, 'y', 0.5)),

    ("Custom Batman", custom_transform(batman, np.array([[6, 9], [9, 6]]))),
    ("Custom Star", custom_transform(star, np.array([[1, -1], [2, 1]])))
]

current_original = 0
current_transformation = 0

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
plot_shape(ax1, originals[0][0], originals[0][1])
plot_shape(ax2, transformations[0][0], originals[0][1], transformations[0][1])

fig.canvas.mpl_connect('key_press_event', key_press)
plt.show()
