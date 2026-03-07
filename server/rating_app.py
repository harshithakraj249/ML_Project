# -*- coding: utf-8 -*-
#!flask/bin/python
from werkzeug.utils import secure_filename
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, current_app, send_from_directory, flash
import click
import io
from train_model import *

app = Flask(__name__)
MODEL_PATH = "/home/harshitha/ML_Flask/server/trained_model.txt"

imList = ["images/1.jpg","images/2.jpg","images/3.jpg","images/4.jpg"]

@app.route("/")
def index():	
	return render_template("index1.html", persons=imList)

@app.route('/train',methods=['GET','POST'])
def train():
	if request.method == "POST":
		image_dict = {}
		flag = False
		name1 = request.form["person0"]
		if name1.strip()!="":
			image_dict[name1.lower()] = request.form["image0"]

		name2 = request.form["person1"]
		if name2.strip() != "":
			image_dict[name2.lower()] = request.form["image1"]

		name3 = request.form["person2"]	
		if name3.strip() != "":
			image_dict[name3.lower()] = request.form["image2"]

		name4 = request.form["person3"]
		if name4.strip() != "":
			image_dict[name4.lower()] = request.form["image3"]

		if prepare_embedding_model(image_dict):
			flag = True

		if flag:
			return render_template("test_video.html")

@app.route('/test_face',methods=['GET','POST'])
def test_face():
	video_file = request.files['video']
	filename = secure_filename(video_file.filename)
	video_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	return Response(gen(VideoCamera(os.path.join(app.config['UPLOAD_FOLDER'], filename), MODEL_PATH)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def gen(camera):
    for frame_num in camera.frame_numbers:
        frame = camera.get_frame(frame_num)
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
		

@click.command()
@click.option('--port', '-p', default=5000, help='listening port')
def run(port):
    app.run(debug=True, host="0.0.0.0", port=port)
 
if __name__ == "__main__":
    run()


