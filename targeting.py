import SimpleCV
import create2api
import time
import json

display = SimpleCV.Display()
cam = SimpleCV.Camera()
normaldisplay = False

bot = create2api.Create2()
#Start the Create2
bot.start()
#Put the Create2 into 'safe' mode so we can drive it
bot.safe()

while display.isNotDone():
	if display.mouseRight:
		normaldisplay = not(normaldisplay)
		print "Display Mode:", "Normal" if normaldisplay else "Segmented"

	img = cam.getImage()
	dist = img.hueDistance((255,0,0)).dilate(2).binarize(60)

	segmented = dist
	blobs = segmented.findBlobs()

	if blobs:
		max_area = 0
		max_blob = {}
		for blob in blobs:
			if blob.isRectangle():
				if blob.area() > max_area:
					max_area = blob.area()
					max_blob = blob
		bot.drive_straight(0)
		if max_blob:
			if max_blob.area() > 30:
				max_blob.drawHull()
				segmented.drawCircle((max_blob.x, max_blob.y), 5, SimpleCV.Color.BLUE, 2)
				errory = max_blob.y - 370
				errorx = max_blob.x - 700
				Py = 0.2
				Px = 0.2

				difference = errorx*Px
				speed = Py*errory
				bot.drive_direct(speed - difference, speed+difference)

	if normaldisplay:
		img.show()
	else:
		segmented.show()

bot.destroy()
