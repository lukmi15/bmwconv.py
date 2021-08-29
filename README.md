# `bmwconv.py`

This is a reimplementation of `bmwconv` provided by Justin Newman found on [e90post.com](https://www.e90post.com/forums/showthread.php?t=279294&page=2)

This re-implementation is done in Python 3 because it does not need to be compiled and can therefore lowers the bar for inexperienced users and also works on all platforms supporting Python 3.

If you call this program without arguments it will print its usage and some licensing information.

Pass all files you want to convert as arguments. They will be transformed to mp3 files if possible.
BR3 files will be transformed to MP4, BR4 files to MP3, and BR5 files to WMA. If `ffmpeg` was found on the system, a call to `ffmpeg` will be made trying to transform these files to MP3.
If you pass a directory as argument, `bmwconv.py` will recursively scan the directory for files BR{3,4,5} it can convert.
