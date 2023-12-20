from PIL import Image
import requests
from io import BytesIO

def open_image(image_path):
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        try:
            response = requests.get(image_path)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))
        except Exception as e:
            print(f"Error: {e}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    return image

def image_to_ascii(image_path, output_width=100):
    image = open_image(image_path)

    if image:
        aspect_ratio = image.height / image.width
        output_height = int(output_width * aspect_ratio)

        image = image.resize((output_width, output_height))

        ascii_chars = "@%#*+=-:. "

        image = image.convert("L")

        ascii_image = ""
        for pixel_value in image.getdata():
            ascii_image += ascii_chars[pixel_value // (256 // len(ascii_chars))]

        lines = [ascii_image[i:i+output_width] for i in range(0, len(ascii_image), output_width)]

        print("\n".join(lines))

if __name__ == "__main__":
    image_path = "https://t2.genius.com/unsafe/172x172/https%3A%2F%2Fimages.genius.com%2Fa7716525000d5d3943ad3fbe97b5d7b4.1000x1000x1.jpg"

    image_to_ascii(image_path)
