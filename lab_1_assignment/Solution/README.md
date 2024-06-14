# 2D and 3D Shape Transformations 🧙

🚀 This project demonstrates various linear transformations on 2D and 3D shapes using Python's NumPy, Matplotlib, and OpenCV libraries. The shapes included are a "Batman" logo, a star, and a pyramid. The transformations include rotation, scaling, reflection, shearing, and custom transformations.

## Getting Started

🔧 **Prerequisites**

- Python
- NumPy
- Matplotlib
- OpenCV (for image transformations)

Install the required libraries using:
```bash
pip install numpy matplotlib opencv-python
```

## Running the Code

1. Save the code in a Python file, e.g., `transformations.py`.
2. Ensure you have the required libraries installed.
3. Run the script using a Python IDE such as VSCode or Jupyter Notebook, or from the terminal using the command below:

```bash
python transformations.py
```

## 🌟 Features

✨ **Shapes**

- **Batman Logo**
- **Star**
- **Pyramid**
- **Custom Images** (for image transformations)

✨ **Transformations**

- **2D Transformations:**
  - Rotation
  - Scaling
  - Reflection
  - Shearing
  - Custom transformations
- **3D Transformations:**
  - Rotation around X, Y, and Z axes
  - Scaling
  - Translation
- **Image Transformations (OpenCV):**
  - Rotation
  - Scaling
  - Reflection

## 🤳 Usage

🎮 **Key Bindings for 2D and 3D Transformations**

- **Right Arrow**: Next transformation
- **Left Arrow**: Previous transformation
- **A**: Next original shape
- **D**: Previous original shape
- **Z**: Next transformation and original shape (Right Arrow + A)
- **X**: Previous transformation and original shape (Left Arrow + D)

The plot will update to show the original shape and the transformed shape side by side.

🎮 **Key Bindings for Image Transformations (OpenCV)**

- **ESC**: Exit the application
- **A**: Previous transformation
- **D**: Next transformation

## ❕Used sources:
- [numpy angles](https://numpy.org/doc/stable/reference/generated/numpy.rot90.html)
- [rotate matrix](https://www.geeksforgeeks.org/numpy-radians-deg2rad-python/)
- [plt axes](https://www.geeksforgeeks.org/matplotlib-axes-class/)
- [Updating](https://youtu.be/PpzaVR3PaBY) and there were other vids...
- [mpl_connect](https://matplotlib.org/stable/users/event_handling.html) + [ChatGPT](https://chat.openai.com/)(only for the purpose to interact with the user!!)
- [shear matrix](https://youtu.be/fuBsMED8GOw?t=716)
- [3D Plottings](https://youtu.be/fAztJg9oi7s)
- [3D Pyramid](https://stackoverflow.com/questions/39408794/python-3d-pyramid)

https://youtu.be/P5TfA5Y9jbo

- [Flip Method](https://www.geeksforgeeks.org/python-opencv-cv2-flip-method/)
- [How to detect when a key is released in OpenCV?](https://stackoverflow.com/questions/59924396/how-to-detect-when-a-key-is-released-in-opencv)
- [Working with Keyboards](https://codeloop.org/python-opencv-working-with-keyboards/)
