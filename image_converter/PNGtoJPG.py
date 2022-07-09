from PIL import Image

im = Image.open("astronaut-alone.png").convert("RGB")
im.save("astronaut-alone.jpg", "jpeg")
