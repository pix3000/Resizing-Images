import os
import cv2

def adjust_image_size(input_dir, output_dir, max_pixel_limit):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is an image (you can add more image extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            # Read the image
            image = cv2.imread(input_path)
            
            # Get the current image dimensions
            height, width = image.shape[:2]
            
            # Check if resizing is required
            if height > max_pixel_limit or width > max_pixel_limit:
                # Calculate the scaling factor
                scale = min(max_pixel_limit / height, max_pixel_limit / width)
                
                # Calculate the new dimensions
                new_height = int(scale * height)
                new_width = int(scale * width)
                
                # Resize the image
                resized_image = cv2.resize(image, (new_width, new_height))
                
                # Save the resized image to the output directory
                cv2.imwrite(output_path, resized_image)
                print(f"Resized {filename} - Original Size: ({width}x{height}) - Resized Size: ({new_width}x{new_height})")
            else:
                # If no resizing is required, simply copy the image to the output directory
                cv2.imwrite(output_path, image)
                print(f"Copied {filename} - Size: ({width}x{height})")

# Usage example
input_directory = " "
output_directory = " "
max_pixel_limit = 1024  # Specify the maximum pixel limit here

adjust_image_size(input_directory, output_directory, max_pixel_limit)
