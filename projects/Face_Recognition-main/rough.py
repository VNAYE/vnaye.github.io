from skimage import data, color
from skimage.feature import Cascade
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import patches
from pillow_avif import AvifImagePlugin

# Load the trained cascade file for frontal face detection
trained_file = data.lbp_frontal_face_cascade_filename()

# Initialize the detector cascade
detector = Cascade(trained_file)

# Load and convert the image to grayscale
img = Image.open('faces.avif')
img_array = np.array(img)

# Detect faces
detected = detector.detect_multi_scale(
    img=img_array, scale_factor=1.2, step_ratio=1, min_size=(60, 60), max_size=(123, 123)
)

# Plot the image with detected faces
fig, ax = plt.subplots()
ax.imshow(img_array, cmap='gray')

for patch in detected:
    ax.add_patch(
        patches.Rectangle(
            (patch['c'], patch['r']),
            patch['width'], patch['height'],
            fill=False, edgecolor='red', linewidth=2
        )
    )

plt.show()
