from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup
import re
import random

def crawl_image_url(artist):
    artist = artist.replace(' ', '-').lower()

    url = f"https://genius.com/artists/{artist}"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        image_url_style = soup.find('div', class_='mini_card-thumbnail')['style']
        match = re.search(r"url\('([^']+)'\)", image_url_style)
        
        if match:
            image_url = match.group(1)
            image_url += f"?random={random.randint(1, 1000)}"
            return image_url

    print(f"Failed to retrieve image URL. Status code: {response.status_code}")
    return None

def open_image(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
    except Exception as e:
        print(f"Error: {e}")
        return None

    return image

def image_to_ascii(image_url, output_width=100):
    image = open_image(image_url)

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
    artist = "Reyna-deyna"

    while True:
        image_url = crawl_image_url(artist)

        if image_url:
            print(f"Image URL: {image_url}")

            image_to_ascii(image_url)

            next_image = input("Next? (yes/no): ").lower()
            if next_image != "yes":
                break
        else:
            break
