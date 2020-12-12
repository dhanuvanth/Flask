import urllib.request

img = urllib.request.urlretrieve('https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/WALL-Eposter.jpg/220px-WALL-Eposter.jpg','raw_Image/1.jpeg')
print(img)

# from PIL import Image
# import requests
# from io import BytesIO
# import cv2

# url = 'https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/WALL-Eposter.jpg/220px-WALL-Eposter.jpg'
# response = requests.get(url)
# img = Image.open(BytesIO(response.content))
# print(img)