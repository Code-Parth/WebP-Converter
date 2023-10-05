# Import the necessary libraries
from PIL import Image  # Pillow library for image processing
import os              # OS library for file and directory operations
import sys             # Sys library for system-related operations

# Define a function to convert input image files to WebP format
def convert_to_webp(input_files, output_folder):
    # Loop through each input file
    for input_path in input_files:
        try:
            # Open the input image using Pillow's Image.open method
            with Image.open(input_path) as img:
                # Get the base name of the input file without the extension
                base_name = os.path.splitext(os.path.basename(input_path))[0]
                # Construct the output file path with the .webp extension
                output_path = os.path.join(output_folder, f"{base_name}.webp")
                # Save the image in WebP format at the specified output path
                img.save(output_path, 'webp')
                # Print a message indicating successful conversion
                print(f"Converted {input_path} to webp.")
        except Exception as e:
            # Print an error message if an exception occurs during conversion
            print(f"Error converting {input_path}: {str(e)}")

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 3:
        print("Usage: python convert_to_webp.py input_file_or_folder output_folder")
        sys.exit(1)

    # Extract the input files (all arguments except the last) and the output folder (last argument)
    input_files = sys.argv[1:-1]
    output_folder = sys.argv[-1]

    # Check if the specified output folder doesn't exist, and create it if necessary
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Call the convert_to_webp function to perform the actual conversion
    convert_to_webp(input_files, output_folder)
