import requests
import cv2

url = "https://www.google.co.jp/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
file_name = "google.jpg"

response = requests.get(url)
image = response.content

with open(file_name, "wb") as a:
    a.write(image)

img = cv2.imread('google.jpg')
cv2.imshow("google",img)
cv2.waitKey(0)