import pytube

video_id = input("Enter the video ID: ")
path_to_download_video = input("Enter the path to save the video: ")

# Define the YouTube video URL
video_url = "https://www.youtube.com/watch?v=" + video_id

# Create a YouTube object
youtube = pytube.YouTube(video_url)

# Get the highest resolution video stream
stream = youtube.streams.get_highest_resolution()

# Download the video
stream.download(output_path = path_to_download_video)

print("Video downloaded successfully!")