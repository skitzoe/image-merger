from PIL import Image
import os
import random

# Set the input folders and output folder path
input_folders = [r"K:\Development\python\image layers\cards", r"K:\Development\python\image layers\def",r"K:\Development\python\image layers\deff", r"K:\Development\python\image layers\dice", r"K:\Development\python\image layers\attachment"
                 , r"K:\Development\python\image layers\fighting", r"K:\Development\python\image layers\strength", 
                 r"K:\Development\python\image layers\off", r"K:\Development\python\image layers\melee", r"K:\Development\python\image layers\namez", r"K:\Development\python\image layers\origin"]
output_folder = r"K:\Development\merged_images"

# Loop through 20 times to create 20 merged images
for i in range(50):
    # Create a list to store all images
    images = []

    # Loop through all input folders
    for folder in input_folders:
        # Get a list of all image files in the folder
        image_files = [f for f in os.listdir(folder) if f.endswith(".png")]

        # Select a random image file from the folder
        random_file = os.path.join(folder, random.choice(image_files))

        # Open the image file and add it to the list
        image = Image.open(random_file).convert("RGBA")
        images.append(image)

    # Get the size of the first image
    width, height = images[0].size

    # Create a new empty image
    merged_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Loop through all images and paste them onto the merged image
    for image in images:
        merged_image.paste(image, (0, 0), image)

    # Save the merged image as a new file in the output folder
    output_file = os.path.join(output_folder, f"merged_{i}.png")
    merged_image.save(output_file)

    # Clean up
    for image in images:
        image.close()
