# Convert Image Format

These scripts can change format of images from PNG to JPG and JPG to PNG

### Prerequisites

Required Modules
- PIL==1.1.6

To install:
```
$ pip install -r requirements.txt
```

### How to run the script

- JPG to PNG (single image)
    1. Copy the JPG image to the directory where `JPGtoPNG.py` exists
    2. Replace file name `astronaut-alone.jpg` inside `JPGtoPNG.py`
	   (line 3) to input file name (JPG).
    3. Replace file name `astronaut-alone.png` inside `JPGtoPNG.py`(line 4) to
       output file name (PNG).
    4. Run following command:
      ```
      $ python JPGtoPNG.py
      ```
- PNG to JPG (single image)
    1. Copy the PNG image in directory where `PNGtoJPG.py` exists
    2. Replace file name `astronaut-alone.png` inside `PNGtoJPG.py`
	   (line 3) to input file name (PNG).
    3. Replace file name `astronaut-alone.jpg` inside `PNGtoJPG.py`
	   (line 4) to output file name (JPG).
    4. Run following command:
      ```
      $ python PNGtoJPG.py
      ```

## Author Name

[Anurag Rajput](https://github.com/anurag0345)
