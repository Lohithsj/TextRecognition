import cv2
import pytesseract
import re
from datetime import datetime


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread(r"C:\Users\lohit\PycharmProjects\TextRecognition\Images\sidecar.jpg")

text = pytesseract.image_to_string(img)
print(text)

date_match = re.search(r'\d{2}/\d{2}/\d{4}',text)

result = datetime.strptime(date_match.group(), '%d/%m/%Y').date()


print("Extracted date from image is " + str(result))

cv2.imshow("Img", img)

cv2.waitKey(0)

