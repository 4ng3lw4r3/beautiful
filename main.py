from module2.lyrics_crawler import crawl_song_list, crawl_lyrics
from module1.image_crawler import crawl_image_url, image_to_ascii

def greetings():
    print("Greetings Angel! Let's read some beautiful lyrics now, Angel<3?")
    response = input("Yes/No: ").lower()
    return response == "yes"

def crawl(artist, time_limit=60, source='genius', return_format='csv'):
    if greetings():
        while True:
            song_list = crawl_song_list(artist)
            if song_list:
                print("Choose a song, Angel<3:")
                for i, song in enumerate(song_list, 1):
                    print(f"{i}. {song}")

                try:
                    selected_song_index = int(input("Enter the number of the song you want to see the lyrics for, Angel<3: ")) - 1
                    selected_song = song_list[selected_song_index]

                    crawl_lyrics(artist, selected_song)
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid number, Angel<3")

            artworks_response = input("Do you want to see the artwork, Angel<3? (yes/no): ").lower()
            if artworks_response != "yes":
                break

            image_url = crawl_image_url(artist)
            if image_url:
                print(f"Image URL: {image_url}")
                image_to_ascii(image_url)

                next_image = input("Next, Angel<3? (yes/no): ").lower()
                if next_image != "yes":
                    break
            else:
                break

if __name__ == "__main__":
    artist_name = "Reyna Deyna"
    crawl(artist_name, time_limit=60, source='genius', return_format='csv')
