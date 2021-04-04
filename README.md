# macytclip
Download videos from the internet with this handy macOS menu bar app!

<img width="600" alt="image" src="https://user-images.githubusercontent.com/44755603/113511526-7d81f500-9560-11eb-93b4-0641384b6261.png">

## Installation:
This repository contains a script which will set up a virtual environment on your machine and download all the necessary dependencies to compile the source. To do this you need to download this repository, either as a zip or using git like this:

    git clone https://github.com/MasterMax13124/macytclip.git

Then navigate into the folder and execute the start.sh script. In the terminal you can do this with:

    cd macytclip && ./start.sh

The script will set up a virtual environment for you and download all the required packages. It will then compile the app for you using py2app. Once it's done you can find the app file in the same folder as the start.sh script.

## Usage:

To use macytclip, you can either start the app directly in the folder where you compiled it, or copy it to your Applications folder. That way it will show up in Spotlight and Launchpad. Once the app is running, you can find it's icon in the menubar. Simply copy the link to a the video you want to download, then open the macytclip menu by clicking on it's icon in the menubar. Select one of the download options and wait for the notifications confirming your download and then open the Downloads folder in Finder. Here you can find the downloaded file with the same name as the original video. Macytclip can download any media that youtube-dl can download.

## Thanks to:
[Youtube-dl](https://github.com/ytdl-org/youtube-dl/), the piece of software that does all of the actual work here

[rumps](https://github.com/jaredks/rumps), which makes macOS menu bar apps so easy that even I can make one

[py2app](https://github.com/ronaldoussoren/py2app/blob/master/LICENSE.txt), which makes it possible to package all this as a standalone Mac app

[klaxon](https://github.com/knowsuchagency/klaxon), which makes the notifications possible, since those in rumps break

[clipboard](https://github.com/terryyin/clipboard), which was the first and simplest way I found of reading from the system clipboard
