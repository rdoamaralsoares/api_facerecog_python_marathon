from flask import Flask, jsonify, request
from faces import Face

app = Flask(__name__)

face = Face()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/face_encoding", methods=['POST'])
def face_encoding():
    try:
        loaded1 = request.files.get('image1', '')
        loaded2 = request.files.get('image2', '')

        resp = face.compare_face(loaded1, loaded2).tolist()

        success = {
            "treated": True,
            "comparison": resp,
            "id": request.form.get('id')
        }
        return jsonify(success)
    except:
        success = {
            "treated": False,
            "id": request.form.get('id'),
            "reason": "Undefined"
        }
        return jsonify(success)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=4001, debug=True)
