import os
import sys
import json
import face_recognition
import _pickle as pickle

path = "/home/harshitha/ML_Flask/server/static"

def prepare_embedding_model(image_name, model_path):
    modelDict = {}

    known_face_encodings = []
    known_face_names = []
    modelDict["known_face_encodings"] = known_face_encodings
    modelDict["known_face_names"] = known_face_names
    print("ini train dict:\n", modelDict)

    for key, value in image_name.items():
        image_path = path + "/" + value
        image = face_recognition.load_image_file(image_path)
        image_face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(image_face_encoding)
        known_face_names.append(key)

    modelDict["known_face_encodings"] = known_face_encodings
    modelDict["known_face_names"] = known_face_names
    print("trained dict:\n", modelDict)

    if not os.path.exists(model_path):
        with open("trained_model.txt", 'wb') as file:
            file.write(pickle.dumps(modelDict))
    else :
        with open("trained_model.txt", 'wb') as file:
            file.write(pickle.dumps(modelDict))

    return True, modelDict
