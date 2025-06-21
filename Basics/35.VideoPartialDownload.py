

#!/usr/bin/env python3
# pip install pytubefix InquirerPy ffmpeg-python

import os, re, subprocess, uuid, sys
from InquirerPy import inquirer
from pytubefix import YouTube
import time
import subprocess
import threading

def download_with_progress(cmd, total_duration):
    start_time = time.time()

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, bufsize=1)

    def show_progress():
        last_out_time = 0
        while True:
            line = process.stdout.readline()
            if not line:
                break
            line = line.strip()
            if line.startswith("out_time_ms="):
                out_time_ms = int(line.split('=')[1])
                out_time_sec = out_time_ms / 1_000_000
                last_out_time = out_time_sec

                percent = (out_time_sec / total_duration) * 100
                elapsed = time.time() - start_time
                remaining = (elapsed / percent) * (100 - percent) if percent > 0 else 0

                bar = f"[{'█' * int(percent // 2):<50}]"
                print(f"\r⬇️  Downloading: {bar} {percent:.2f}% | ⏱ Elapsed: {int(elapsed)}s | ⏳ ETA: {int(remaining)}s", end='')

    # Start progress monitor in main thread
    show_progress()
    process.wait()
    print("\n✅ Download & merge complete.\n")


# -------- helpers ------------------------------------------------------------
def hhmmss_to_float(ts):
    parts = [int(p) for p in ts.split(":")]
    if len(parts) == 1:    return parts[0]
    if len(parts) == 2:    return parts[0]*60 + parts[1]
    return parts[0]*3600 + parts[1]*60 + parts[2]

def safe_name(txt):

    safe_title = re.sub(r'[<>:"/\\|?*\[\]]', "-", txt).strip() #Replacing illegal characters
    return re.sub(r'[\u200B-\u200D\uFEFF]', '', safe_title).strip()  
    # return re.sub(r'[<>:"/\\|?*\[\]]', "-", txt).strip()

# -------- user input ---------------------------------------------------------
url   = input("🔗  YouTube URL: ").strip()
yt = YouTube(url)
print(f"🎬 Title: {yt.title} \n")
title = safe_name(yt.title)

ss_in = input("⏱  Start  (HH:MM:SS): ").strip()
to_in = input("⏱  End    (HH:MM:SS): ").strip()

ss = hhmmss_to_float(ss_in);   to = hhmmss_to_float(to_in)
if ss >= to: sys.exit("❌  End time must be after start time.")


# title = title[:100]
download_dir = r"D:\YouTubeDownloads";  os.makedirs(download_dir, exist_ok=True)

# -------- choose video‑only format -------------------------------------------
video_streams = (yt.streams.filter(only_video=True, file_extension="mp4")
                         .order_by("resolution").desc())
if not video_streams:
    sys.exit("❌  No DASH video-only streams found.")


choices = [{"name": f"{s.resolution}  {s.fps}fps - { round (s.filesize /(1024*1024), 2)} MB  , {s.video_codec}", "value": s.itag}
           for s in video_streams]

itag = inquirer.select("🎞  Pick video quality:", choices).execute()
vstream = yt.streams.get_by_itag(itag)
astream = yt.streams.filter(only_audio=True, file_extension="mp4")\
                    .order_by("abr").desc().first()

unique = uuid.uuid4().hex[:6]
v_url, a_url = vstream.url, astream.url

safe_ss = ss_in.replace(":", "-")
safe_to = to_in.replace(":", "-")
video_size_name = round( vstream.filesize / (1024 * 1024) , 2)

filename = f"{title}[{safe_ss}-to-{safe_to}]_{vstream.resolution}_{vstream.fps}fps__{video_size_name} MB.mp4"
out_path = os.path.join(download_dir, filename)

# -------- ffmpeg: pull only the slice and merge ------------------------------
cmd = [
    "ffmpeg",
    "-loglevel", "error",        # keep console clean
    "-ss", str(ss), "-to", str(to),
    "-i", v_url,
    "-ss", str(ss), "-to", str(to),
    "-i", a_url,
    "-c", "copy",                # stream‑copy, no re‑encode
    "-movflags", "+faststart",   # nice for web players
    out_path
]
print("\n⬇️  Downloading selected clip …")
# subprocess.run(cmd, check=True)
duration = to - ss  # total clip length in seconds
cmd += ["-progress", "pipe:1", "-nostats"]  # enables live progress output
download_with_progress(cmd, duration)
print("✅  Saved to:", out_path)



