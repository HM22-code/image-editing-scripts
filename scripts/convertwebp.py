from PIL import Image
import os

def convert_webp(input_file, output_format='png'):
    """
    Convert a .webp image file to either .png or .gif format.

    Args:
        input_file (str): Path to the input .webp file.
        output_format (str): Output format, either 'png' or 'gif'.
    """
    # Check if the input file is a .webp file
    if not input_file.lower().endswith('.webp'):
        print(f"Error: The file {input_file} is not a .webp file.")
        return
    # Load the webp image
    try:
        with Image.open(input_file) as img:
            # Determine the output file name
            output_file = os.path.splitext(input_file)[0] + f'.{output_format}'
            # Save the image in the desired format
            img.save(output_file, format=output_format.upper())
            print(f"Image successfully converted to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# Exmple :
convert_webp('example_image.webp', 'png')
