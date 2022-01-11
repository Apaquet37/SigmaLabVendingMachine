import time
import picamera

val = 0
effects = ["pastel", "solarize", "colorswap", "watercolor", "denoise"]

with picamera.PiCamera() as camera:
	for x in effects:
		print("Starting to take image")
		camera.resolution = (1024, 768)
		camera.start_preview()
		y = effects[val]
		camera.image_effect = y
		camera.annotate_text = y 
		time.sleep(2)
		camera.capture(str(val)+effects[val]+".jpg")
		print("Done")
		val = val+1
	else:
		camera.close() 
		print("Finished")
