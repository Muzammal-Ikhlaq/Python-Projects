from PIL import Image
import os
import matplotlib.pyplot as plt

# Folder path
location = r"E:\PycharmProjects\DataSets Work\Task 7 [Read Image Dataset]\Melanoma Cancer Image Dataset\test\Malignant"

# Get all image files
image_files = [f for f in os.listdir(location) if f.lower().endswith(('.jpg', '.png'))]
image_files.sort()

# Show all images and auto-close
if image_files:
    for image_file in image_files:
        image_path = os.path.join(location, image_file)
        image = Image.open(image_path)

        # Display image using matplotlib
        plt.figure()  # Create a new figure
        plt.imshow(image)
        plt.title(f"Showing: {image_file}")
        plt.show()  # Show the image

        plt.close()  # Close the figure immediately
        image.close()  # Free memory
else:
    print("No images found")