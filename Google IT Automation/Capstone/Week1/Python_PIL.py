# Read, rotate and display the image

from PIL import Image
im = Image.open("bride.jpg")
im.rotate(45).show()

# Resize an image and save the new image with a new name

from PIL import Image
im = Image("example.jpg")
new_im = im.resize((640,480))
new_im.save("example_resized.jpg")

# Rotate an image and save the image with a new name

from PIL import Image
im = Image("example.jpg")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")

# Rotate, resize and save an image, all at once

from PIL import Image
im = Image("example.jpg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")