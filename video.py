import pytube

def download_video(url, download_location):
    try:
        print("Downloading Video...")
        youtube = pytube.YouTube(url)
        stream = youtube.streams.get_highest_resolution()
        video_path = stream.download(download_location)
        print("Video downloaded successfully. Path: " + video_path)

    except youtube.exceptions.RegexMatchError:
        print("Invalid YouTube URL.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    

def download_audio(url, download_location):
    try:
        print("Downloading Audio...")
        youtube = pytube.YouTube(url)
        audio_stream = youtube.streams.filter(only_audio=True).first()
        audio_path = audio_stream.download(output_path=download_location)
        new_audio_path = audio_path.split('.')[0] + '.mp3'

        if audio_path != new_audio_path:
            import os
            os.rename(audio_path, new_audio_path)
            audio_path = new_audio_path

        print("Audio downloaded successfully.")

    except pytube.exceptions.RegexMatchError as e:
        print(f"An error occurred: {str(e)}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    download_location = "video/" 
    url = input("Enter the URL: ")
    try: 
        option = int(input('''
        Select any following options:
                1. MP3
                2. MP4
        '''))
        if option == 1:
            download_audio(url, download_location)
        elif option == 2:
            download_video(url, download_location)
        else:
            print("Please select any 2 options!!!")
    
    except ValueError:
        print("[!] Strings/Symbols not allowed [!]")


if __name__ == "__main__":
    main()
