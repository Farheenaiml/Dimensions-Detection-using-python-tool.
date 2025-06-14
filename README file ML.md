
#  Dimension Capture from Image Using Python

##  Project Overview

This tool uses Python and OpenCV to estimate the **real-world dimensions (in centimeters)** of a **target rectangular object** (e.g., a box, book) in an image by comparing it to a **known-size reference object** (e.g., a credit card).  
It processes a single image and outputs the target's width and height, both visually and in text.


##  Dependencies Explained

This project relies on a few essential Python libraries:

### 1. **OpenCV (`opencv-python`)**
- **Purpose**: Core library for image loading, processing, edge detection, contour detection, drawing rectangles, text annotations, and image saving.
- **Installation**:
  pip install opencv-python

### 2. **Matplotlib (`matplotlib`)**
- **Purpose**: Used for displaying the final annotated image with accurate dimension labels. OpenCV’s native `imshow()` may not work consistently across platforms, hence `matplotlib` is used.
- **Installation**:
  pip install matplotlib

### 3. **NumPy (`numpy`)**
- **Purpose**: Required by OpenCV for internal array handling and numerical operations, even if not used directly in the code.
- **Installation**:
  pip install numpy

### Install all together:
pip install opencv-python matplotlib numpy


##  How to Run the Script

###  Folder Structure

```
measure_dimensions_project/
├── measure_rect.py               # Main Python script
├── sample_images/
│   └── Image_refn.jpeg           # Input image containing reference + target
├── annotated_box_dimensions.jpg # Output image (auto-saved)
└── README.md                     # This file

###  Command-Line Instructions

1. **Open Command Prompt or Terminal**
2. **Navigate to your project folder**:
   cd Downloads/measure_dimensions_project

3. **Run the script with the image as an argument**:
   python measure_rect.py sample_images/Image_refn.jpeg


### How to run in VS Code

1.Open Terminal : 
python measure_rect.py sample_images/Image_refn.jpeg

###  Sample Terminal Output

Total contours found: 354
Detected rectangles: 2
Scale: 0.0103 cm/pixel
Box Dimensions (real-world): Width = 14.88 cm, Height = 11.72 cm

- The output image `annotated_box_dimensions.jpg` will show the target object with red-labeled real-world dimensions.


##   How to Specify the Reference Dimensions
To accurately estimate the dimensions of the target object, you must first specify the real-world width (in centimeters) of the reference object in the image.

 **Common Reference**: Credit Card
If you're using a credit card as your reference object (which is standard size), its width is 8.56 cm. This is already specified in the code like this:

ref_width_cm = 8.56  # Real-world width of the reference object in cm
Using a Different Reference Object?
You can use any flat, rectangular object with known dimensions, such as:

A business card
A printed label
A small book
A ruler or scale

Just measure the actual width in centimeters of the reference object, and update the line in the script:

ref_width_cm = 7.0  # Replace with your object's real width in cm
 Only the width is required in the script because the width in pixels is used to calculate the scale (cm_per_pixel). Make sure the reference object is placed flat and fully visible in the image.

##  Notes and Assumptions

- The script assumes the **reference object is the smallest detected valid rectangle**.
- The next largest rectangle is assumed to be the **target**.
- We can adjust the thresholds for area and aspect ratio in the contour loop to suit different objects/images.


##  Output Image Example

After running the script, will find an annotated image like this:

annotated_box_dimensions.jpg

It will show:

- The **target object** in a green rectangle
- The **real-world dimensions** in red text above it
