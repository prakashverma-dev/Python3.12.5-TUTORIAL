
# https://youtu.be/i53GrzvJSkY?si=5HFVAorIvEgBWPgB

# url = "https://youtu.be/UomU-iD0uvY?si=16K2P-lEUJkTDRpN"

# Youtube video download with yt_dlp package -

import os
from yt_dlp import YoutubeDL

def get_video_info(url):
    with YoutubeDL() as ydl:
        return ydl.extract_info(url, download=False)

def list_video_only_formats(formats):
    video_only = []
    print("\nAvailable Video Qualities (no audio):")
    for f in formats:
        if f.get('vcodec') != 'none' and f.get('acodec') == 'none' and f.get('ext') == 'mp4':
            res = f.get('height')
            fps = f.get('fps')
            size = round((f.get('filesize', 0) or 0) / (1024 * 1024), 2)
            print(f"{len(video_only)+1}: {res}p - {fps}fps - {size}MB - Format ID: {f['format_id']}")
            video_only.append(f)
    return video_only

def download_video_audio_merge(url, video_format_id, output_file):
    ydl_opts = {
        'format': f"{video_format_id}+bestaudio[ext=m4a]",
        'outtmpl': output_file,
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }]
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# === MAIN ===
url = input("Enter YouTube video URL: ").strip()
info = get_video_info(url)
formats = info['formats']
title = info['title'].replace(" ", "_").replace("/", "_")

video_formats = list_video_only_formats(formats)
choice = int(input("\nSelect the video quality number to download: ")) - 1
format_id = video_formats[choice]['format_id']

output_filename = f"{title}_{video_formats[choice]['height']}p.mp4"

print(f"\n🔽 Downloading video ({video_formats[choice]['height']}p) + best audio...")
download_video_audio_merge(url, format_id, output_filename)
print(f"✅ Done! Merged file saved as: {output_filename}")

