import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread(r"C:\Users\lohit\PycharmProjects\TextRecognition\Images\example1.jpeg")

text = pytesseract.image_to_string(img)
print(text)

cv2.imshow("Img", img)

#cv2.waitkey(0)

