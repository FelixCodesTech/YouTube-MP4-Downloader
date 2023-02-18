#!/usr/bin/env python3


import ctypes.util
ctypes.util.find_library('libffi')
import tkinter as tk
from tkinter import messagebox
import yt_dlp
import pathlib
import os

class YoutubeDownloader:
    def __init__(self, master):
        self.master = master
        master.title("Youtube Downloader")

        self.video_url_label = tk.Label(master, text="Video URL:")
        self.video_url_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.video_url_entry = tk.Entry(master, width=50)
        self.video_url_entry.grid(row=0, column=1, padx=5, pady=5)

        self.download_button = tk.Button(master, text="Download", command=self.download)
        self.download_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.location_label = tk.Label(master, text="Download location: ")
        self.location_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.location_value = tk.StringVar()
        self.location_value.set(pathlib.Path.home().joinpath("Downloads"))
        self.location_entry = tk.Entry(master, textvariable=self.location_value, width=50)
        self.location_entry.grid(row=2, column=1, padx=5, pady=5)

    def download(self):
        video_url = self.video_url_entry.get()
        dl_format = "best"

        dl_location = pathlib.Path(self.location_entry.get())
        os.makedirs(name=dl_location, exist_ok=True)

        print(f"The downloads will be saved in: {dl_location}")
        print()

        with yt_dlp.YoutubeDL({
            "noplaylist": True,
            "format": dl_format,
            "outtmpl": f"{dl_location}/%(extractor)s__%(title)s.%(ext)s",
            "postprocessors": [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'best',
                    'preferredquality': '192',
                },
            ],
            "addmetadata": True,
            "embedthumbnail": True,
        }) as ytdl:
            try:
                ytdl.download([video_url])
                messagebox.showinfo("Download Complete", "Download completed successfully!")
            except yt_dlp.utils.DownloadError as e:
                return
        print()

        messagebox.showinfo("Download Complete", "Download completed successfully!")
        return

if __name__ == "__main__":
    root = tk.Tk()
    downloader = YoutubeDownloader(root)
    root.mainloop()
