from klaxon import klaxon
import youtube_dl
import rumps
import clipboard
import os

# Author: MasterMax13124
# Date: 12.Mar 2021
# Notes: Proof of concept completed. Rumps notifications seem broken, so I am using klaxon
# To-Do: Expand download options, add notification for failed ytdl, add better icon and config options

class macytclipapp():
    def __init__(self):
        self.app = rumps.App("MacYTclip", "👇")
        self.download_button = rumps.MenuItem(title="Download", callback=self.download_from_clipboard)
        self.app.menu = [self.download_button]
    
    def download_from_clipboard(self, sender):
        klaxon("Download started", "macytclip", "Youtube-dl is initializing")
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([clipboard.paste()])
        klaxon("Download complete!", "macytclip", "Check Finder")

    def run(self):
        self.app.run()


if __name__ == '__main__':
    os.chdir(os.path.expanduser('~'))
    os.chdir('Downloads')
    app = macytclipapp()
    app.run()
