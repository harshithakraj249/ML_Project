#!/usr/bin/python
import face_recognition
import cv2
import numpy as np
import base64

def face_comparision(known_face_encodings, known_face_names, frame):
    rgb_small_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
    
        face_names.append(name)

    try:
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top = top
            right = right
            bottom = bottom
            left = left
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        return frame
        
    except:
        return frame    
    
    '''for (top, right, bottom, left), name in zip(face_locations, face_names):
        top = top
        right = right
        bottom = bottom
        left = left

    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    return frame'''
