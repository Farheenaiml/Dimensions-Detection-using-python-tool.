import cv2
import matplotlib.pyplot as plt
import sys

# Check for command line argument
if len(sys.argv) < 2:
    print("Usage: python measure_box.py <image_path>")
    sys.exit(1)

# Get image path from command line argument
image_path = sys.argv[1]

# Load image
image = cv2.imread(image_path)
if image is None:
    raise Exception("Image not found or path is incorrect!")

orig = image.copy()

# Preprocessing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blur, 50, 150)

# Find contours
contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw all contours for debugging
print(f"Total contours found: {len(contours)}")

# Analyze contours
detected = 0
rectangles = []  # store valid rectangles

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    area = w * h
    aspect_ratio = w / float(h)

    if 10000 < area < 500000 and 1.3 < aspect_ratio < 1.8:
        # Likely credit card
        rectangles.append((x, y, w, h))
        cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 255, 0), 4)
        detected += 1

    elif 50000 < area < 2000000 and 0.9 < aspect_ratio < 1.3:
        # Likely box
        rectangles.append((x, y, w, h))
        cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 255, 0), 4)
        detected += 1

print(f"Detected rectangles: {detected}")

if len(rectangles) < 2:
    raise Exception("Could not detect both reference object and box.")

# Sort rectangles by area: smallest = credit card, largest = box
rectangles = sorted(rectangles, key=lambda r: r[2] * r[3])

ref_rect = rectangles[0]      # Credit card
target_rect = rectangles[1]   # Box

# Get width of credit card in pixels
ref_width_pixels = ref_rect[2]  # width (w) from (x, y, w, h)

# Known real-world width of a credit card (in cm)
ref_width_cm = 8.56

# Compute scale: cm per pixel
cm_per_pixel = ref_width_cm / ref_width_pixels
print(f"Scale: {cm_per_pixel:.4f} cm/pixel")

# Extract box dimensions in pixels
_, _, box_w_pixels, box_h_pixels = target_rect

# Convert pixels to centimeters
box_width_cm = box_w_pixels * cm_per_pixel
box_height_cm = box_h_pixels * cm_per_pixel

print(f"Box Dimensions (real-world): Width = {box_width_cm:.2f} cm, Height = {box_height_cm:.2f} cm")

# Coordinates for the box
box_x, box_y, box_w, box_h = target_rect

# Prepare label text
label = f"{box_width_cm:.2f}cm x {box_height_cm:.2f}cm"

# Put label text above the box rectangle
cv2.putText(orig, label, (box_x, box_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 
            0.7, (0, 0, 255), 2)  # Red color text

# Show annotated image
plt.figure(figsize=(12, 8))
plt.imshow(cv2.cvtColor(orig, cv2.COLOR_BGR2RGB))
plt.title("Box with Real-World Dimensions")
plt.axis("off")
plt.show()

# Optionally save the image
cv2.imwrite("annotated_box_dimensions.jpg", orig)

# Show result again for confirmation
plt.figure(figsize=(12, 8))
plt.imshow(cv2.cvtColor(orig, cv2.COLOR_BGR2RGB))
plt.title("Detected Rectangles")
plt.axis("off")
plt.show()
