from flask import Flask, render_template, Response,  request, session, redirect, url_for, send_from_directory, flash,jsonify
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image
import os
import sys
import cv2
import ocr_detect
from flask_cors import CORS 

class GetText(object):
    
    def __init__(self, file):
        self.file = pytesseract.image_to_string(Image.open(proj_dir + '/images/' + file))

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["ALLOWED_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF", "PDF"]
UPLOAD_FOLDER = '/home/harshitha/ML_Flask/ocr/static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['UPLOAD_FOLDER'] = '/home/harshitha/ML_Flask/ocr/static/pdf/'
CORS(app)

@app.route("/")
def index():
  return render_template("index.html")

@app.route('/upload_file', methods=['POST'])
def upload_file():
      detected_text=None
      if request.method == 'POST':
            if 'files' not in request.files:
                  return 'There is no files in form'
      f = request.files['files']
      language_value = request.form['selectedlanguage']
      pdf_img_value = request.form['pdf_img']
      
      # create a secure filename
      filename = secure_filename(f.filename)
      # save file to /static/uploads
      filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      f.save(filepath)
      if pdf_img_value == "pdf_to_img":
            detected_text = ocr_detect.pdf_to_image(filepath, language_value)
      else:
            detected_text = ocr_detect.GetText(filepath, language_value)
      message=[
        {'filepath':filename,
         'Extracted_text':detected_text}
      ]
      print(detected_text)
      print(filepath)
      #return(detected_text)
      return jsonify(message)

if __name__ == '__main__':
      app.run(port=3000, debug=True)
