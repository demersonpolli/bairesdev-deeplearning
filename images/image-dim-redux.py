from PIL import Image
from tqdm import tqdm


def convert_to_grayscale(image):
    width, height = image.size
    grayscale_img = Image.new('L', (width, height))

    with tqdm(total= width * height) as pbar:
        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                # Calculate the grayscale value
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                grayscale_img.putpixel((x, y), gray)
                pbar.update(1)
    
    return grayscale_img


def convert_to_binary(image, threshold= 128):
    width, height = image.size
    binary_image = Image.new('1', (width, height))

    with tqdm(total= width * height) as pbar:
        for x in range(width):
            for y in range(height):
                gray = image.getpixel((x, y))
                # Convert to binary based on the threshold
                binary_value = 255 if gray > threshold else 0
                binary_image.putpixel((x, y), binary_value)
                pbar.update(1)
    
    return binary_image


if __name__ == '__main__':
    image_path = 'C:\\Users\\polli\\Downloads\\lagarta.jpg'

    # Open an image file
    with Image.open(image_path) as img:
        # Display image details
        print(f"Image format: {img.format}, image size: {img.size}, image mode: {img.mode}")
        # Show the image
        img.show()

        # Convert the image to grayscale
        grayscale_img = convert_to_grayscale(img)
        # Show the grayscale image
        grayscale_img.show()

        # Convert the grayscale image to binary
        binary_img = convert_to_binary(grayscale_img)
        # Show the binary image
        binary_img.show()


