from PIL import Image, ImageDraw, ImageFont

chars = "论十大关系里  逍   的近义词"
# chars = "道德经三十六章必固予之的前句"
# chars = "郦道元三峡里属引凄异的后一句"
# chars = "炎系拳王坡无系十六级屏小技能"


width = 1500

image = Image.new(mode='RGB', size=(width, 135), color='white')
img_draw = ImageDraw.Draw(image)
ttf = ImageFont.truetype("C:\Windows\Fonts\MSYH.TTC", size=100)
img_draw.text((0, 0), chars, fill='black', font=ttf)
image2 = image.crop((0, 0, width, 45))
# image2 = image.crop((0, 47, width, 49))
# image2 = image.crop((0, 96, width, 135))
image2.show()
# image.save("1.jpg")
