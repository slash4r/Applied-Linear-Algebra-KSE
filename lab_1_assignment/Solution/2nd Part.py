import numpy as np
import cv2 as cv


image = cv.imread("batman.png")


def rotate(image: np.ndarray, angle: float) -> np.ndarray:
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv.warpAffine(image, rotation_matrix, (w, h))
    return rotated_image


def scale(image: np.ndarray, fx: float, fy: float) -> np.ndarray:
    scaled_image = cv.resize(image, None, fx=fx, fy=fy)
    return scaled_image


def reflect(image: np.ndarray, axis: str) -> np.ndarray:
    if axis == 'x':
        reflected_image = cv.flip(image, 0)
    elif axis == 'y':
        reflected_image = cv.flip(image, 1)
    else:
        raise ValueError("Invalid axis. Must be 'x' or 'y'")
    return reflected_image


transformations = [
    ("Original Batman", image),
    ("Rotated Batman 180 degrees", rotate(image, 180)),
    ("Rotated Batman 90 degrees", rotate(image, 90)),
    ("Scaled Batman 2x", scale(image, 2.5, 1)),
    ("Reflected Batman over y-axis", reflect(image, 'y'))
]


def display_transformation(index):
    title, transformation = transformations[index]
    cv.imshow(title, transformation)


if __name__ == "__main__":
    current_transformation = 0

    while True:
        display_transformation(current_transformation)
        key = cv.waitKey(0)  # wait endlessly for a key press

        if key == 27:  # ESC key to exit
            break
        elif key == ord('a'):
            current_transformation = (current_transformation - 1) % len(transformations)
            cv.destroyAllWindows()
        elif key == ord('d'):
            current_transformation = (current_transformation + 1) % len(transformations)
            cv.destroyAllWindows()

    cv.destroyAllWindows()
