import sys
from PIL import Image, ImageOps


def main():
    input_file, output_file = check_args(sys.argv)
    process_image(input_file, output_file)


def check_args(argv):
    """Validate command-line arguments and return input and output filenames."""

    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = argv[1]
    output_file = argv[2]

    valid_ext = (".jpg", ".jpeg", ".png")

    # Require supported image formats for both input and output
    if not input_file.lower().endswith(valid_ext):
        sys.exit("Invalid input")

    if not output_file.lower().endswith(valid_ext):
        sys.exit("Invalid output")

    # Ensure input and output share the same extension
    in_ext = input_file.rsplit(".", 1)[-1].lower()
    out_ext = output_file.rsplit(".", 1)[-1].lower()

    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")

    return input_file, output_file


def process_image(input_file, output_file):
    """Overlay shirt.png onto the input image and save the result."""

    try:
        shirt = Image.open("shirt.png")
        input_img = Image.open(input_file)

        # Resize and crop input to match the shirt's dimensions
        input_img = ImageOps.fit(input_img, shirt.size)

        # Use the shirt image as both overlay and mask (for transparency)
        input_img.paste(shirt, shirt)

        input_img.save(output_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
