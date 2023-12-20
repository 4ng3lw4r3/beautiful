import requests
from bs4 import BeautifulSoup

def angelsworld(artist, song_title):
    artist = artist.replace(' ', '-').lower()
    song_title = song_title.replace(' ', '-').lower()

    url = f"https://genius.com/Reyna-deyna-angels-world-lyrics"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        lyrics_div = soup.find('div', class_='Lyrics__Container-sc-1ynbvzw-1 kUgSbL')
        if lyrics_div:
            lyrics_text = lyrics_div.get_text('\n').replace('<br>', '\n')



            print(lyrics_text)
        else:
            print("Lyrics not found on the page.")

    else:
        print(f"Failed to retrieve the lyrics. Status code: {response.status_code}")

if __name__ == "__main__":
    artist = "Reyna Deyna"
    song_title = "Angels World"

    angelsworld(artist, song_title)
