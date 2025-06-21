

# url = "https://youtu.be/UomU-iD0uvY?si=16K2P-lEUJkTDRpN"


import os
import ffmpeg
from pytubefix import YouTube
import re
from InquirerPy import inquirer
import uuid
from datetime import datetime
import sys

def show_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = round(bytes_downloaded / total_size * 100, 2)
    progress_bar = f"[{'█' * int(percentage_of_completion // 2):50}]"
    sys.stdout.write(f"\r📦 Downloading: {progress_bar} {percentage_of_completion}%")
    sys.stdout.flush()

def download_and_merge_with_ffmpeg_python():

        # --- User-defined fixed output folder ---
        download_folder = r"D:\YouTubeDownloads"  # Change this to your desired path
        os.makedirs(download_folder, exist_ok=True)

        # --- Get URL input ---
        url = input("Enter the YouTube video URL: ").strip()
        # url = "https://youtu.be/UomU-iD0uvY?si=16K2P-lEUJkTDRpN"


        try:
            yt = YouTube(url, on_progress_callback = show_progress)
            print(f"\n🎬 Title: {yt.title}")

            # Clean + Unique title -
            safe_title = re.sub(r'[<>:"/\\|?*]', '-', yt.title) #Replacing illegal characters
            safe_title = re.sub(r'[\u200B-\u200D\uFEFF]', '', safe_title).strip()  # Remove zero-width/invisible chars


            # Get adaptive video-only streams/Filter available video-only streams -
            video_streams = yt.streams.filter(only_video=True, file_extension='mp4').order_by('resolution').desc()

            print("\n📺 Available video resolutions:-")

            # Prepare display options for InquirerPy / Create CLI selection list -
            video_choices = []
            for i, stream in enumerate(video_streams):

                video_size_mb = round(stream.filesize / (1024 * 1024), 2)

                label = f"{i+1}. {stream.resolution} - {stream.fps}fps {video_size_mb} MB, Codec: {stream.video_codec}"

                video_choices.append({"name": label, "value": i})

            selected_video_index = inquirer.select(

                message="Select video resolution to download: ",
                choices=video_choices,
                cycle=True,
                default=0 

                ).execute()   


            selected_stream = video_streams[selected_video_index]


            unique_id = uuid.uuid4().hex[:6]

            print("\n ⬇️ Downloading video stream only...")
            video_path = selected_stream.download(output_path=download_folder, filename=f"video_only_{unique_id}.mp4")

            print(" \n ⬇️ Downloading best audio stream only...")
            audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
            audio_path = audio_stream.download(output_path=download_folder, filename=f"audio_only_{unique_id}.mp4")


            # --- Sanitize output filename directly here ---
            video_filesize_mb = round(selected_stream.filesize / (1024 * 1024), 2)
            
            output_filename = f"{safe_title} [{selected_stream.resolution}_{selected_stream.fps}fps__{video_filesize_mb}MB__{selected_stream.video_codec}].mp4"

            output_path = os.path.join(download_folder, output_filename)

            print(" \n 🛠️ Merging stream video with stream audio using ffmpeg-python...")

            # Merge using ffmpeg-python -
            input_video = ffmpeg.input(video_path)
            input_audio = ffmpeg.input(audio_path)
            ffmpeg.output(input_video, input_audio, output_path, vcodec='copy', acodec='aac').run(overwrite_output=True)

            print(f"\n ✅ Merged video saved at:\n{output_path}")

            # Clean up temp files
            os.remove(video_path)
            os.remove(audio_path)

            print("Video Downloaded Successfully !!")


        except Exception as e:
            print(f"❌ Error: {e}")

       

# Run the function
download_and_merge_with_ffmpeg_python()
