import requests
from bs4 import BeautifulSoup

def crawl_song_list(artist):
    artist = artist.replace(' ', '-').lower()

    url = f"https://genius.com/artists/{artist}"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        song_list = soup.find_all('div', class_='mini_card-title')

        return [song.get_text() for song in song_list]

    else:
        print(f"Failed to retrieve the song list. Status code: {response.status_code}")
        return None

def crawl_lyrics(artist, song_title):
    artist = artist.replace(' ', '-').lower()
    song_title = song_title.replace(' ', '-').lower()

    url = f"https://genius.com/{artist}-{song_title}-lyrics"

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
    artist = "Reyna-deyna"

    song_list = crawl_song_list(artist)
    if song_list:
        print("Available Songs, Angel<3:")
        for i, song in enumerate(song_list, 1):
            print(f"{i}. {song}")

        try:
            selected_song_index = int(input("Enter the number of the song you want to see the lyrics for, Angel<3: ")) - 1
            selected_song = song_list[selected_song_index]

            crawl_lyrics(artist, selected_song)
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid number, Angel<3")
