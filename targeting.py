import SimpleCV
import create2api
import time
import json

display = SimpleCV.Display()
cam = SimpleCV.Camera()
normaldisplay = False

#bot = create2api.Create2()
#Start the Create2
#bot.start()
#Put the Create2 into 'safe' mode so we can drive it
#bot.safe()

while display.isNotDone():
	if display.mouseRight:
		normaldisplay = not(normaldisplay)
		print "Display Mode:", "Normal" if normaldisplay else "Segmented"

	img = cam.getImage()
	dist = img.hueDistance((255,255,0)).dilate(2).binarize(60)

	segmented = dist
	blobs = segmented.findBlobs()

	if blobs:
		max_area = 0
		max_blob = {}

		blobs = blobs[len(blobs)-2:]
		#bot.drive_straight(0)
		for blob in blobs:
			if blob.area() > 30:
				blob.drawHull()
				segmented.drawCircle((blob.x, blob.y), 5, SimpleCV.Color.BLUE, 2)

		blob1 = blobs[0]
		blob2 = blobs[1]

		distance = abs(blob1.x - blob2.x)
		offest = 0.5*(blob1.x + blob2.x)
		print (distance, offest)

	if normaldisplay:
		img.show()
	else:
		segmented.show()

#bot.destroy()
