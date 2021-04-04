# macytclip
Download videos from the internet with this handy macOS menu bar app!

## Installation:
There are two ways to install macytclip. The easiest option is to head over to the [Releases](https://github.com/MasterMax13124/macytclip/releases) and simply download the latest version. Then unzip the file you downloaded and copy the included macytclip.app file to your Mac's Applications folder. Then launch it and enjoy!

Alternatively you can compile the .app file from the source code. To do this you need to download this repository. Then navigate into the folder and execute the start.sh script. The script will set up a virtual environment for you and download all the required libraries. It will then compile the app for you. Once it's done you can find the app file in the same folder as start.sh.

## Usage:

Currently usage is very limited. First you need to start the app and make sure that the menu icon appears. Then simply copy a link to a youtube video, or any other video source that youtube-dl can download, and then click on the macytclip icon in your menu bar. Click 'Download' and your download will start. Once it's done, you can find your downloaded video file in finder in your Downloads folder.

## Thanks to:
[Youtube-dl](https://github.com/ytdl-org/youtube-dl/), the piece of software that does all of the actual work here

[RUMPS](https://github.com/jaredks/rumps), which makes macOS menu bar apps so easy that even I can make one

[py2app](https://github.com/ronaldoussoren/py2app/blob/master/LICENSE.txt), which makes it possible to package all this as a standalone Mac app

[klaxon](https://github.com/knowsuchagency/klaxon), which makes the notifications possible, since those in rumps break

[clipboard](https://github.com/terryyin/clipboard), which was the first and simplest way I found of reading from the system clipboard
