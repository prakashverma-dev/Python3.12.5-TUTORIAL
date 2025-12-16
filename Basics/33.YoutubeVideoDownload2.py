
# MINI PROJECTS - 05 : -
# Project Name : Youtube Video Download and MP3 Downloder With CLI Selection -

# url = "https://youtu.be/UomU-iD0uvY?si=16K2P-lEUJkTDRpN"


import os
import ffmpeg
from pytubefix import YouTube
import re
from InquirerPy import inquirer
from datetime import datetime
from pytubefix.cli import on_progress

def download_and_merge_with_ffmpeg_python():

    # --- User-defined fixed output folder ---
    download_folder = r"D:\YouTubeDownloads"  # Change this to your desired path
    os.makedirs(download_folder, exist_ok=True)

    # --- Get URL input ---
    url = input("Enter the YouTube video URL: ").strip()
    # url = "https://youtu.be/UomU-iD0uvY?si=16K2P-lEUJkTDRpN"


    try:
        yt = YouTube( url, on_progress_callback = on_progress )
        print(f"\n🎬 Title: {yt.title}")

        # Clean + Unique title + SHorten Title -
        safe_title = re.sub(r'[<>:"/\\|?*]', '-', yt.title) #Replacing illegal characters
        safe_title = re.sub(r'[\u200B-\u200D\uFEFF]', '', safe_title).strip()  # Remove zero-width/invisible chars

        # short_title = (safe_title[:50].rstrip() + "...") if len(safe_title) > 53 else safe_title

        
        # Ask: Audio(MP3) or Video? -

        media_type = inquirer.select(
        message="What do you want to download?",
        choices=[
            {"name": "🎥 Video (MP4)", "value": "video"},
            {"name": "🎧 Audio (MP3)", "value": "audio"},
          ]
        ).execute()

        if media_type == "video":  # Video Mode -

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
            
             # ------------------------------------------------

            selected_stream = video_streams[selected_video_index]

           

            print("\n ⬇️ Downloading Only the selected video stream...")
            video_path = selected_stream.download(output_path = download_folder,  filename="video_only.mp4")

            print(" ⬇️ Downloading only the best audio stream...")
            audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
            audio_path = audio_stream.download(output_path=download_folder, filename="audio_only.mp4")


            # --- Sanitize output filename directly here ---
            video_filesize_mb = round(selected_stream.filesize / (1024 * 1024), 2)
            
            output_filename = f"{safe_title} [{selected_stream.resolution}_{selected_stream.fps}fps__{video_filesize_mb}MB__{selected_stream.video_codec}].mp4"

            output_path = os.path.join(download_folder, output_filename)

            print("🛠️ Merging video and audio with ffmpeg-python...")

            # Merge using ffmpeg-python -
            input_video = ffmpeg.input(video_path)
            input_audio = ffmpeg.input(audio_path)
            ffmpeg.output(input_video, input_audio, output_path, vcodec='copy', acodec='aac').run(overwrite_output=True)

            print(f"\n ✅ Merged video saved at:\n{output_path}")

            # Clean up temp files
            os.remove(video_path)
            os.remove(audio_path)

            print("Video Downloaded Successfully !!")


        else:  # for MP3(Audio) Download only -

            audio_streams = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc()

            print("\n📺 Available MP3 Files:-")
            
            audio_choices = []
            for i, stream in enumerate(audio_streams):

                # print(audio_streams)

                audio_size_mb = round(stream.filesize / (1024 * 1024), 2)

                label = f"{i+1}. {stream.abr} - {audio_size_mb} MB, Codec: {stream.audio_codec}"
                
                audio_choices.append({"name": label, "value": i})

            selected_audio_index = inquirer.select(

                message="Select audio quality:",
                choices=audio_choices,
                pointer="👉"

             ).execute() 

            selected_audio_stream = audio_streams[selected_audio_index] 

            # --- Sanitize output filename directly here ---
            audio_size = round(selected_audio_stream.filesize / (1024 * 1024), 2)

            audio_filename =f"{safe_title} [{selected_audio_stream.abr}__{audio_size}MB__{selected_audio_stream.audio_codec}].mp3"

            audio_output_path = os.path.join(download_folder, audio_filename)

            print("⬇️ Downloading MP4a audio...")
            mp4a_Audio_tmp_path = selected_audio_stream.download(output_path=download_folder, filename="temp_Mp4a_audio.mp4")

            print("🎧 Converting to MP3...")
            ffmpeg.input(mp4a_Audio_tmp_path).output(audio_output_path, format='mp3', acodec='libmp3lame').run(overwrite_output=True)
            
            # Clean up temp files
            os.remove(mp4a_Audio_tmp_path)
            print(f"✅ MP3 saved as: {audio_output_path}")  

            print("Mp3 Downloaded Successfully !!")



    except Exception as e:
        print(f"❌ Error: {e}")

        

# Run the function
download_and_merge_with_ffmpeg_python()  


