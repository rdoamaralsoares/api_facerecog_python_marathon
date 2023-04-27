#Defining my class Face
import face_recognition

class Face:
    def __int__(self):
        pass

    def compare_face(self, image1, image2):
        print("---- Lets compare Faces using face_recognition lib -----")
        # Load CNH.jpeg and detect faces
        image = face_recognition.load_image_file(image1)
        face_locations = face_recognition.face_locations(image)
        # Get the single face encoding out of CNH
        face_location = face_locations[0]  # Only use the first detected face
        face_encodings = face_recognition.face_encodings(image, [face_location])
        ricardo_known_face_encoding_1 = face_encodings[0]  # Pull out the one returned face encoding

        print("Loaded: ", image1)

        # Load the image with unknown to compare
        image = face_recognition.load_image_file(image2)  # Load the image we are comparing
        unknown_face_encodings = face_recognition.face_encodings(image)
        print("Loaded: ", image2)
        # The known face encodings (can be only 1 - less is faster)
        matches = face_recognition.compare_faces([ricardo_known_face_encoding_1], unknown_face_encodings[0])

        # return True or False if faces recognized.
        return matches[0]

