# macytclip
Download videos from the internet with this handy macOS menu bar app!

## How to set it up:
macytclip is written in python and depends on some python libraries. Fortunately these dependencies can be easily installed using pip. Open a terminal and issue the following commands:

```
pip install py2app klaxon clipboard rumps youtube-dl
```

Let the installation finish. Next we will download this repository and enter it with:

```
git clone https://github.com/MasterMax13124/macytclip/
cd macytclip
```

Inside we need to run:

```
python3 setup.py py2app
```

Once finished, you will see multiple new folders. Open the folder 'dist' and inside you will find the compiled .app file. You can delete the new folders afterwards, if you want.

## Usage:

Currently usage is very limited. Simply copy a link to a youtube video, or any other video source that youtube-dl can download, and then click on the macytclip icon in your menu bar. Click 'Download' and your download will start. Once it's done, you can find your downloaded video file in finder in your Downloads folder.
