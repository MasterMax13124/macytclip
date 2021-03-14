from klaxon import klaxon
import youtube_dl
import rumps
import clipboard
import os

# Author: MasterMax13124
# Date: 12.Mar 2021
# Notes: Proof of concept completed. Rumps notifications seem broken, so I am using klaxon
# To-Do: Expand download options, add better icon and config options

class macytclipapp():
    def __init__(self):
        self.app = rumps.App("MacYTclip", "⤓")
        # self.download_button = rumps.MenuItem(title="Download", callback=self.download_from_clipboard)
        self.title_entry = rumps.MenuItem(title="macytclip v1.1", callback=None)
        self.download_h264 = rumps.MenuItem(title="Download video (H.264)", callback=self.download_h264_function)
        self.app.menu = [self.title_entry, self.download_h264]
        
    def download_h264_function(self, sender):
        klaxon("Download started", "macytclip", "")
        ydl_opts = {'format' : 'bestvideo+bestaudio[ext=m4a]/best', 'merge_output_format': 'mp4', 'nocheckcertificate': 'true'}
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([clipboard.paste()])
            klaxon("Download complete!", "macytclip", "Check your Downloads folder!")
        except:
            klaxon("The copied text was not a valid url!", "macytclip")
    
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