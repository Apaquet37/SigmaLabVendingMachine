import PIL.Image as image
import os

digits = []
for i in os.listdir("PhoneCamera"): #iterate through file names in directory
    digits.append(image.open("PhoneCamera/" + i)) #append the image object created by image.open

print(digits)
