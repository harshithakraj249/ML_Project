from wand.image import Image as wi
import os
import pytesseract
import sys
import cv2
import imageio
import numpy as np
from PIL import Image, ImageOps

proj_dir = os.path.dirname(os.path.abspath(__file__))
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pdf_file_content = []


def pdf_to_image(filepath, language_value):
    outputDir = 'ima/'
    PDF_file = wi(filename=filepath, resolution=400)
    ImageSequence = 0

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    for img in PDF_file.sequence:
        Image1 = wi(image=img)
        f = 'ima/Image' + language_value + str(ImageSequence) + ".jpg"
        Image1.save(filename=f)
        pdf_file_content.append(GetText(f, language_value))
        ImageSequence += 1

    print('-----------------------------------')
    print('pdf_file_content:', pdf_file_content)
    return pdf_file_content


def GetText(image_path, language_value):
       f = imageio.imread(image_path, as_gray=True)
       bg = bg_detect(f,127)
       if(bg == 'light'):
              image = cv2.imread(image_path)
              gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
              # check to see if we should apply thresholding to preprocess the image
              gray = cv2.GaussianBlur(gray, (5,5), 0)
              # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
              text = pytesseract.image_to_string(gray, config = '--psm 12', lang = language_value)
       else:
              im = Image.open(image_path)
              im_invert = ImageOps.invert(im)
              head, tail = os.path.split(image_path)
              imn=os.path.splitext(tail)[0]
              im_invert.save('/home/harshitha/Downloads/flask/static/inverted/' + imn + '.jpeg', quality=95)
              image_to_ocr = cv2.imread('/home/harshitha/Downloads/flask/static/inverted/' + imn + '.jpeg')
              grayi = cv2.cvtColor(image_to_ocr, cv2.COLOR_BGR2GRAY)
              grayi = cv2.GaussianBlur(grayi, (5,5), 0)
              text = pytesseract.image_to_string(grayi, config = '--psm 12', lang = language_value)
       return text

def bg_detect(img, thrshld):
   is_light = np.mean(img) > thrshld
   return 'light' if is_light else 'dark'
