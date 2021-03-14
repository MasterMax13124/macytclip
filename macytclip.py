from klaxon import klaxon
import youtube_dl
import rumps
import clipboard
import os
import json

# Author: MasterMax13124
# Date: 12.Mar 2021
# Notes: Proof of concept completed. Rumps notifications seem broken, so I am using klaxon
# To-Do: Expand download options, add better icon and config options

class macytclipapp():
    def __init__(self):
        self.app = rumps.App("MacYTclip", "⤓")
        self.download_h264 = rumps.MenuItem(title="Download video (H.264)", callback=self.download_h264_function)
        self.title_entry = rumps.MenuItem(title="macytclip v1.1", callback=None)
        self.download_dnxhr25fps = rumps.MenuItem(title="Download video (DNxHR 25FPS)", callback=self.download_dnxhr25fps_function)
        self.app.menu = [self.title_entry, self.download_h264, self.download_dnxhr25fps]
        
    def download_h264_function(self, sender):
        klaxon("Download started", "macytclip", "")
        ydl_opts = {'format' : 'bestvideo+bestaudio[ext=m4a]/best','outtmpl': 'macytclipvideo','writeinfojson': 'true', 'merge_output_format': 'mp4', 'nocheckcertificate': 'true'}
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([clipboard.paste()])

            with open('macytclipvideo.info.json') as json_file: 
                data = json.load(json_file) 
                os.rename("macytclipvideo.mp4", data["fulltitle"] + ".mp4")

            os.remove("macytclipvideo.info.json")

            klaxon("Check your Downloads folder!", "macytclip", "Download completed successfully")

        except:
            klaxon("The copied text was not a valid url!", "macytclip")
    
    def download_dnxhr25fps_function(self, sender):
        klaxon("Download started", "macytclip", "")
        ydl_opts = {'format': 'bestvideo+bestaudio', 'outtmpl': 'macytclipvideo', 'writeinfojson': 'true', 'no-check-certificate': 'true'}
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([clipboard.paste()])

            #ffmpeg -i video.mp4 -c:v dnxhd -profile:v dnxhr_hq -vf fps=25/1,format=yuv422p -c:a pcm_s16le video.mov && rm video.mp4
            os.system("ffmpeg -i macytclipvideo.mp4 -c:v dnxhd -profile:v dnxhr_hq -vf fps=25/1,format=yuv422p -c:a pcm_s16le macytclipvideo.mov && rm macytclipvideo.mp4")

            with open('macytclipvideo.info.json') as json_file: 
                data = json.load(json_file) 
                os.rename("macytclipvideo.mov", data["fulltitle"] + ".mov")

            os.remove("macytclipvideo.info.json")

            klaxon("Check your Downloads folder!", "macytclip", "Download completed successfully")
        except:
            klaxon("The copied text was not a valid url!", "macytclip")


    # template for the download function:
    # def download_from_clipboard(self, sender):
    #     klaxon("Download started", "macytclip", "")
    #     ydl_opts = {}
    #     try:
    #         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #             ydl.download([clipboard.paste()])
    #         klaxon("Download complete!", "macytclip", "Check your Downloads folder!")
    #     except:
    #         klaxon("The copied text was not a valid url!", "macytclip")

    def run(self):
        self.app.run()


if __name__ == '__main__':
    os.chdir(os.path.expanduser('~'))
    os.chdir('Downloads')
    app = macytclipapp()
    app.run()