import json
import requests
import sys
import os

API_KEY = sys.argv[1]


# Send to the Api
def imageColorizeURL(url):
	r = requests.post("https://api.deepai.org/api/colorizer", files={'image': open(url, 'rb')}, headers={'api-key': API_KEY})
	return r.json()["output_url"]

# Download image
def downloadIMG(httpURL, indexURL):
	os.system(f"curl {httpURL} -o output/{indexURL}")

# Get the images in the input area
def getImages():
	dirs = os.listdir("input")
	finalDir = []
	for i in dirs:
		if i.split(".")[1].lower() == "png":
			finalDir.append(i)
		elif i.split(".")[1].lower() == "jpg":
			finalDir.append(i)
		elif i.split(".")[1].lower() == "jpeg":
			finalDir.append(i)
	return finalDir

# Main function
def main():
	images = getImages()
	images.sort()
	for i in images:
		imageurl = imageColorizeURL(f"input/{i}")
		print(i)
		downloadIMG(imageurl, i)

if __name__ == "__main__":
	main()