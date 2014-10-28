#!/Users/Aankit/Documents/RememberForget/forget/bin/python

import os, cv2, random
from PIL import Image, ImageChops

path = './memorial/'


files = os.listdir(path)
fileTypes = [file[-3:] for file in files]

#let's mix them
def mix(canvas, paint):
	img1 = cv2.imread(path + canvas)
	w1, h1, c1 = img1.shape
	#im2 = cv2.resize(im2, (width, height))
	img2 = cv2.imread(path + paint)
	w2, h2, c2 = img2.shape
	chunkSize = random.randint(1,100)	#can play around with these
	numChunks = random.randint(0,1000/chunkSize)	#can play around with these
	print 'mix: number of chunks:%d' %numChunks
	for i in range(numChunks):
		startX = random.randint(0,w2-chunkSize)
		startY = random.randint(0,h2-chunkSize)
		chunk = img2[startX:startX+chunkSize, startY:startY+chunkSize]
		replaceX = random.randint(0,w1-chunkSize)
		replaceY = random.randint(0,h1-chunkSize)
		img1[replaceX:replaceX+chunkSize, replaceY:replaceY+chunkSize] = chunk
		chunkSize = random.randint(1,100)
		print 'another chunk'
	cv2.imwrite(path + canvas, img1)
	print 'saved'

def difference(canvas, paint):
	img1 = Image.open(path + canvas)
	width, height = img1.size
	img2 = Image.open(path + paint)
	img2 = img2.resize((width, height), Image.ANTIALIAS)
	print 'difference: resize without issue'
	img1 = ImageChops.difference(img1, img2)
	img1.save(path + canvas)
	print 'saved'

forgetters = [mix, mix, mix, mix, difference]
#let's subtract them
for i in range(len(files)):
	print 'file number: %d' %i
	if fileTypes[i] == 'jpg' or fileTypes[i] == 'png':
		x = random.randint(0,len(files)-1)
		if fileTypes[x] == 'jpg' or fileTypes[x]:
			random.choice(forgetters)(files[i], files[x])
		else:
			continue
	else:
		continue



