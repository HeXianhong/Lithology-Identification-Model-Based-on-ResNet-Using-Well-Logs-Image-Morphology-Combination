from PIL import Image, ImageDraw
import random


def draw(i):
    # Set each pic's size as 500x110
    image = Image.new('RGB', (500, 110), 'white')
    draw = ImageDraw.Draw(image)

    # Set the lines' position through changing the randint parameters
    red_x = random.randint(190, 230)
    green_x = random.randint(230, 260)
    blue_x = random.randint(260, 320)

    draw.line((red_x, 0, red_x, 110), fill='red', width=3)

    draw.line((green_x, 0, green_x, 110), fill='green', width=3)

    draw.line((blue_x, 0, blue_x, 110), fill='blue', width=3)

    # Set the pics save path
    path = r"path" + 'name' + str(i) + ".jpg"
    image.save(path)

# Through setting the loop times to generate pics
for i in range(1, 101):
    draw(i)
