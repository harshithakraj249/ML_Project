import face_recognition
import cv2
import numpy as np
import os
import shutil
#import imquality.brisque as brisque
import PIL.Image
from pathlib import Path

def process_video(video_path, video_name):
	cascPath = "haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(cascPath)
	cap = cv2.VideoCapture(video_path)
	total_frames = cap.get(7)
	frame_numbers = []
	for i in range(1,int(total_frames)):
	    if i==1:
	        frame_numbers.append(i)
	    elif i%10==0:
	        frame_numbers.append(i)

	#print(frame_numbers)
	counter = 0
	for frame_num in frame_numbers:
	    cap.set(1, frame_num)
	    ret, frame = cap.read()
	    # cv2.imshow("frame", frame)
	    # cv2.waitKey(0)
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    # cv2.imshow("gray", gray)
	    # cv2.waitKey(0)
	    file_path = "/home/harshitha/ML_Flask/server/all_faces/" + video_name + "/"
	    if not os.path.exists(file_path):
	    	os.makedirs(file_path)	    
	    #rgb_small_frame = frame[:, :, ::-1]
	    try:
	        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=10, minSize=(105, 105))
	        #face_locations = face_recognition.face_locations(frame)
	        # Display the results
	        for (x, y, w, h) in faces:
	        	filename = file_path + str(counter) + ".jpg"
	        	# Draw a box around the face
	        	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	        	crop_img = frame[y : y+h, x : x+w]
	        	#cv2.imshow('Video', crop_img)
	        	#cv2.imshow('Video', frame)
	        	#cv2.waitKey(1)
	        	cv2.imwrite(filename, crop_img)
	        	counter = counter + 1
	    except Exception as e:
	    	print(str(e))
	    	continue

	# Release handle to the webcam
	cap.release()
	cv2.destroyAllWindows()
	#identify_unique(file_path)
	return file_path

def identify_unique(uimgs_path, vid_name):
	i = 0
	uni_img = "/home/harshitha/ML_Flask/server/unique_faces/" + vid_name 
	os.system("rm -rf "+uni_img)
	# if os.path.exists(uni_img):
	# 	dirss = os.listdir(uni_img)
	# 	print(len(dirss))
	# 	if(len(dirss) >= 1):
	# 		for imf in dirss:
	# 			shutil.rmtree(uni_img)
	# 			print("removed..........", uni_img)
	if not os.path.exists(uni_img):
		os.makedirs(uni_img)
	#directorym_in_str = "/home/amithsb/projs/fd/face_recog/auto_face_detection/trainset/A/"
	directorym = os.fsencode(uimgs_path)
	#print("entering folder for main img ")
	for file in os.listdir(directorym):
	    filename = uimgs_path + str(i) + ".jpg"
	    #filename = os.fsdecode(file)
	    # head, tail = os.path.split(os.path.join('/home/amithsb/projs/fd/face_recog/auto_face_detection/trainset/A', filename))
	    # imn_main=os.path.splitext(tail)[0]
	    #print(filename)
	    if(os.path.isfile(filename)):
	        #print("exists")
	        if filename.endswith("jpg") or filename.endswith(".png"):
	            # Load images.
	            try:
	                image_1 = face_recognition.load_image_file(os.path.join(uimgs_path, filename))
	                image_1_face_encoding = face_recognition.face_encodings(image_1)[0]
	            except IndexError:
	                i = i+1
	                continue
	            # image_1 = face_recognition.load_image_file(os.path.join('/home/amithsb/projs/fd/face_recog/auto_face_detection/trainset/A', filename))
	            # image_1_face_encoding = face_recognition.face_encodings(image_1)[0]

	            known_face_encodings = [
	                    image_1_face_encoding
	                ]

	            known_face_names = [
	                    "A"
	                ]

	            face_locations = []
	            face_encodings = []
	            face_names = []


	            
	            #print("The main image:")
	            img_main = cv2.imread(os.path.join(uimgs_path, filename))
	            #cv2.imshow("main_img", img_main)
	            #cv2.waitKey(0)
	            directory_in_str = uimgs_path
	            directory = os.fsencode(directory_in_str)
	            #print("entering folder for comp")
	            for file in os.listdir(directory):
	                filenames = os.fsdecode(file)
	                # head, tail = os.path.split(os.path.join('/home/amithsb/projs/fd/face_recog/auto_face_detection/trainset/A', filenames))
	                # imn=os.path.splitext(tail)[0]
	                # #print(imn)
	                # if(imn == imn_main):
	                #     break
	                if filenames.endswith("jpg") or filenames.endswith(".png"):
	                    #print("all imgs")
	                    frame = cv2.imread(os.path.join(uimgs_path, filenames))
	                    face_locations = face_recognition.face_locations(frame)
	                    face_encodings = face_recognition.face_encodings(frame, face_locations)
	                    face_names = []
	                    #print("The img from folder is:")
	                    #print(filenames)
	                    for face_encoding in face_encodings:
	                        # See if the face is a match for the known face(s)
	                        #print("matching faces now")
	                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
	                        name = "Unknown"
	                    
	                        # If a match was found in known_face_encodings, just use the first one.
	                        if True in matches:
	                            #print("match found....removing")
	                            src = os.path.join(uimgs_path, filenames)
	                            #dest = '/home/amithsb/projs/fd/face_recog/auto_face_detection/trainset/B/'
	                            #cv2.imshow('move_img', frame)
	                            #destii = shutil.copy(src, dest)
	                            
	                            dest = "/home/harshitha/ML_Flask/server/unique_faces/" + vid_name + "/" + str(i)
	                            #directory = '/home/kenny/gist'
	                            if not os.path.exists(dest):
	                            	os.makedirs(dest)
	                            destii = shutil.move(src, dest)
	                            #move_repeated(src, dest)
	                            #os.remove(os.path.join('/home/amithsb/projs/fd/face_recog/auto_face_detection/faces', filename))
	                        face_names.append(name)
	                        #print(face_names)
	                        break
	            #cv2.destroyAllWindows()
	        i = i+1
	    else:
	        #print("not there")
	        i = i+1   
	#print("Done")
	dest_folder = "/home/harshitha/ML_Flask/server/unique_faces/"+vid_name+"/"
	final_img_folder = "/home/harshitha/ML_Flask/server/static/"+vid_name+"/"
	#get_unique(dest_folder, final_img_folder)
	return dest_folder, final_img_folder

def get_unique(video_path):
	print(video_path)
	head, tail = os.path.split(video_path)
	imn = os.path.splitext(tail)[0]
	stored_img_path = process_video(video_path, imn)
	unique_folder, final_img_folder = identify_unique(stored_img_path, imn)
	os.system("rm -rf "+final_img_folder)
	# if os.path.exists(final_img_folder):	
	# 	dirss = os.listdir(final_img_folder)
	# 	print(len(dirss))
	# 	if(len(dirss) >= 1):
	# 		for imfs in dirss:
	# 			shutil.rmtree(final_img_folder)
				#print("removed..........", imf)
	# final_img_folder,  = "/home/amithsb/projs/fd/face_recog/auto_face_detection/final_faces_imgs/"
	if not os.path.exists(final_img_folder):
		os.makedirs(final_img_folder)
	k = 0 
	dirs = os.listdir(unique_folder)
	dirs.sort()
	#print(dirs)

	for dir in dirs:
		#for sub_dict in os.listdir(directorym):
		#print(sub_dict.decode("utf-8"))
		#dict_name = str(i)
		#print("\n dict_name:", dir)
		sub_directory = os.path.join(unique_folder, dir)
		#while (i == 0):
		sub_dirs = os.listdir(sub_directory)
		sub_dirs.sort()
		#print(sub_dirs)
		for file in sub_dirs:
			# print("here")
			imgs_path = unique_folder + dir + "/"
			filename = file
			#filename = str(i) + ".jpg"
			src_uni = os.path.join(imgs_path, filename)
			dsti = final_img_folder + str(k) + ".jpg"
			if not os.path.exists(final_img_folder):
				os.makedirs(final_img_folder)
			#shutil.rmtree(final_img_folder)
			final_dest = shutil.move(src_uni, dsti)
			#i = i + 1
			k = k + 1
			break
	return final_img_folder


# vid_path = "/home/amithsb/projs/fd/face_recog/auto_face_detection/crowd_test.mp4"
# stored_img_path = process_video(vid_path)
# unique_folder = identify_unique(stored_img_path)
# # unique_folder = "/home/amithsb/projs/fd/face_recog/auto_face_detection/trainset/"
# final_img_folder = "/home/amithsb/projs/fd/face_recog/auto_face_detection/final_faces_imgs/"
# final_imgs = get_unique(unique_folder, final_img_folder)
# print(" Done ")
