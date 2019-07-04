from PIL import Image, ImageTk, ImageDraw
from os import listdir

allFiles =listdir("C:\\abc")

for i in allFiles:
	img = Image.open("C:\\abc\\" + i)
	pilImage = img.resize((28,28), Image.ANTIALIAS)
	pilImage.save("C:\\abd\\"+i)