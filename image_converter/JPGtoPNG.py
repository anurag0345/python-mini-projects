from PIL import Image

im = Image.open("astronaut-alone.jpg").convert("RGB")
im.save("astronaut-alone.png", "png")
