from flask_restful import Api, Resource
from flask import Flask, render_template, jsonify, request, make_response,url_for, redirect, Response
from werkzeug.utils import secure_filename
from flask_cors import CORS 
from random import *
from PIL import Image
from pathlib import Path
from io import BytesIO
import base64
import os
import final_face
from final_face import *
from train_model import *
from camera import VideoCamera
import click

import uuid

UPLOAD_FOLDER = "/home/harshitha/ML_Flask/server/uploads"
MODEL_PATH = "/home/harshitha/ML_Flask/server/trained_model.txt"
FILENAME = ""

final_face_dict = {}
known_face_encodings = []
known_face_names = []


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "./uploads"
CORS(app)                   #Flask's cross-domain issues

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload',methods=['POST']) # The method should be consistent with the front end
def upload():
    if request.method == 'POST':
        file = request.files['files']
        filename = secure_filename(file.filename)
        global FILENAME
        FILENAME = filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        vid_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        folder_path = final_face.get_unique(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_list = []
        dirs = os.listdir(folder_path)
        for dir in dirs:
            head, tail = os.path.split(vid_path)
            imn = os.path.splitext(tail)[0]
            dir = imn+"/"+dir 
            image_list.append(dir)
        image_list.sort()
        # print(image_list)
        print("success")
        persons = image_list
        total = len(image_list)
        messages =[
        {'persons':persons,
        'total':total}
        ]
        return jsonify(messages)
        # return render_template("tagging1.html", persons=image_list, total=len(image_list))
        # return redirect(url_for('result'))
     # fileExt = filename.split('.')[1]
        # autoGenFilename = uuid.uuid4()
        # newfilename = str(autoGenFilename)+'.'+ fileExt
        # file.save(Path(app.config['UPLOAD_FOLDER'], newfilename))

# @app.route('/result',methods=['GET'])
# def result():
#     return "uploaded successfully"
       
# @app.route('/train',methods=['GET','POST'])
# def train():
#     if request.method == "POST":

#         total = request.form["total"]
#         image_dict = {}
#         flag = False

#         for i in range(int(total)):
#             textid = "person"+str(i)
#             imageid = "image"+str(i)
#             textname = request.form[textid]
#             if textname.strip()!="":
#                 image_dict[textname.lower()] = request.form[imageid]

#         final_face_dict["known_face_encodings"] = known_face_encodings
#         final_face_dict["known_face_names"] = known_face_encodings
#         cval, face_dict = prepare_embedding_model(image_dict, MODEL_PATH)
#         print("returned trained dict:\n", face_dict)

#         final_face_dict.update(face_dict)
#         print("main train dict:\n", final_face_dict)


#         if prepare_embedding_model(image_dict, MODEL_PATH):
#             flag = True

#         if flag:
#             return Response(gen(VideoCamera(os.path.join(app.config['UPLOAD_FOLDER'], FILENAME), MODEL_PATH)),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

# def gen(camera):
#     for frame_num in camera.frame_numbers:
#         frame = camera.get_frame(frame_num)
#         yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
if __name__ == "__main__":
    app.run(host="localhost",port=8000,debug=True)