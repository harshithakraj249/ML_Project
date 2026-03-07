import cv2
import numpy as np
import _pickle as pickle
from detection_face import *

class VideoCamera(object):
    #def __init__(self, video_file, model_file, model_dict):
    def __init__(self, video_file, model_file):
        self.video = cv2.VideoCapture(video_file)
        self.total_frames = self.video.get(7)
        self.frame_numbers = self.prepare(self.total_frames)
        self.known_face_encodings = self.prepare_face_data(model_file)["encodings"]
        self.known_face_names = self.prepare_face_data(model_file)["names"]
            
    def __del__(self):
        self.video.release()

    def prepare(self, total_frames):
        frame_numbers = []
        for i in range(1,int(total_frames)):
            if i==1:
                frame_numbers.append(i)
            elif i%5==0:
                frame_numbers.append(i)
        return frame_numbers

    def prepare_face_data(self, model):
        known_face_encodings = []
        known_face_names = []
        face_data = {}
        data = None
        Data = None
        with open(model, 'rb') as file:
            data = file.read()
        Data = pickle.loads(data)
        known_face_encodings = Data["known_face_encodings"]
        known_face_names = Data["known_face_names"]
        face_data["names"] = known_face_names
        face_data["encodings"] = known_face_encodings
        print("face_data:\n", face_data)
        return face_data

    
    def get_frame(self,frame_num):
        self.video.set(1, frame_num)
        success, image = self.video.read()
        if success:
            detected_image = face_comparision(self.known_face_encodings, self.known_face_names, image)
            ret, jpeg = cv2.imencode('.jpeg', detected_image)
            return jpeg.tobytes()
        else:
            return False


# print("inside model_dict:\n", model_dict)
#         self.video = cv2.VideoCapture(video_file)
#         self.total_frames = self.video.get(7)
#         self.frame_numbers = self.prepare(self.total_frames)
#         #final_face_data = self.prepare_face_data(model_dict)
#         self.known_face_encodings = self.prepare_face_data(model_file)["encodings"]
#         self.known_face_names = self.prepare_face_data(model_file)["names"]
#         # self.known_face_encodings = final_face_data["face_encodings"]
#         # self.known_face_names = final_face_data["face_names"]



# def prepare_face_data(self, model):
    #     face_encodings = []
    #     face_names = []
    #     face_data = {}
    #     print("model:\n", model)
    #     data = None
    #     Data = None
    #     with open(model, 'rb') as file:
    #         data = file.read()
    #     Data = pickle.loads(data)
    #     known_face_encodings = Data["face_encodings"]
    #     known_face_names = Data["face_names"]
    #     face_data["face_encodings"] = known_face_encodings
    #     face_data["face_names"] = known_face_names
    #     print("face_data:\n", face_data)
    #     return face_data