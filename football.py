from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import maindf as mdf

def input_text():
	with open('loc.csv', 'r') as f:
		next(f)
		lines = f.read().splitlines()
		img = Image.open('football.jpg')
		print(len(lines))
		for x in range(0, len(lines)):
			words = lines[x].split(",")
			print(words[0],words[1],words[2])
			draw = ImageDraw.Draw(img)
			font = ImageFont.truetype('arial.ttf', 30)
			draw.text((int(words[1]), int(words[2])) , (str(words[0])) , (0,0,0), font=font)

	img.save('football.jpg')

input_text()