# heic-converter
Simple python script to recursively convert all *.heic files in a folder to *.jpg and compress the original files. All EXIF data is preserved.

I wrote this script because I had *.heic files saved sporadically in a large folder tree that I needed converted to *.jpg format.

Simply run the script 

    python heic-converter.py <path>

and it will traverse the folder tree starting in `<path>` and convert all *.heic files to *.jpg. The script converts the files in place and compresses the original *.heic files in each subfolder.

# Dependencies
Requires [Pillow](https://github.com/python-pillow/Pillow) and [pillow-heif](https://github.com/bigcat88/pillow_heif)

    pip install pillow
    pip install pillow_heif
