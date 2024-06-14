import numpy as np
import matplotlib.pyplot as plt


pyramid = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0.5, 0.5, 1]])


def square_pyramid_edges(pyramid_vertices: np.ndarray) -> list:
    """
    Returns the edges of a square pyramid
    """
    base_edges = [[pyramid_vertices[i], pyramid_vertices[(i + 1) % 4]] for i in range(4)]
    apex_edges = [[pyramid_vertices[i], pyramid_vertices[4]] for i in range(4)]
    edges = base_edges + apex_edges
    return edges


def plot_shape_3d(ax, title: str, shape_og: np.ndarray, shape_tr: np.ndarray) -> None:
    """
    Plot the 3D shape with the given title (string) and shape (numpy array)
    """
    ax.clear()
    edges_og = square_pyramid_edges(shape_og)
    for edge in edges_og:
        ax.plot(
            [edge[0][0], edge[1][0]],
            [edge[0][1], edge[1][1]],
            [edge[0][2], edge[1][2]], color='b')

    edges_tr = square_pyramid_edges(shape_tr)
    for edge in edges_tr:
        ax.plot(
            [edge[0][0], edge[1][0]],
            [edge[0][1], edge[1][1]],
            [edge[0][2], edge[1][2]], color='r')
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.grid(True)
    ax.axis('equal')


def rotate_3d(shape: np.ndarray, angle: float, axis: str) -> np.ndarray:
    """
    Rotate the 3D shape by the given angle (in degrees) around the specified axis (x, y, or z)
    """
    angle = np.radians(angle)
    cos = np.cos(angle)
    sin = np.sin(angle)

    if axis == 'x':
        rotation_matrix = np.array([
            [1,   0,    0],
            [0, cos, -sin],
            [0, sin,  cos]
        ])
    elif axis == 'y':
        rotation_matrix = np.array([
            [cos,  0, sin],
            [0,    1,   0],
            [-sin, 0, cos]
        ])
    elif axis == 'z':
        rotation_matrix = np.array([
            [cos, -sin, 0],
            [sin, cos,  0],
            [0,     0,  1]
        ])
    else:
        raise ValueError("Invalid axis. Must be 'x', 'y' or 'z'")

    rotated_shape = rotation_matrix @ shape.T
    return rotated_shape.T


def scale_3d(shape: np.ndarray, factor: float) -> np.ndarray:
    """
    Scale the 3D shape by the given factor
    """
    return shape * factor


def translate_3d(shape: np.ndarray, translation_vector: np.ndarray) -> np.ndarray:
    """
    Translate the 3D shape by the given vector
    """
    return shape + translation_vector


def key_press(event):
    global current_transformation, current_original
    if event.key == 'right':
        current_transformation = (current_transformation + 1) % len(transformations)
    elif event.key == 'left':
        current_transformation = (current_transformation - 1) % len(transformations)
    update_plot()


def update_plot():
    ax.clear()

    original_shape = original[1]
    title_t, transformed_shape = transformations[current_transformation]
    plot_shape_3d(ax, title_t, original_shape, transformed_shape)
    plt.draw()


original = ("Original Pyramid", pyramid)
transformations = [
    ("Rotated Pyramid 90 degrees around X", rotate_3d(pyramid, 90, 'x')),
    ("Rotated Pyramid 90 degrees around Y", rotate_3d(pyramid, 90, 'y')),
    ("Scaled Pyramid 2x", scale_3d(pyramid, 2)),
    ("Translated Pyramid by [1, 1, 1]", translate_3d(pyramid, np.array([1, 1, 1])))
]

current_original = 0
current_transformation = 0

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')

plot_shape_3d(ax, transformations[0][0], original[1], transformations[0][1])

fig.canvas.mpl_connect('key_press_event', key_press)
plt.show()
