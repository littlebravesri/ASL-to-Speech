import json
import PIL.Image as Image
from flask import Flask, jsonify, request, render_template, Response
import cv2
import requests
from cv2 import *

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('JavascriptWebCam.html')


@app.route('/test', methods=['GET', 'POST'])
def testfn():
    global cam
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def gen_frames():
    global frame

    while True:
        success, frame = cam.read()
        if not success:
            break
        else:
            success, buffer = cv2.imencode('.jpg', frame)
            frame1 = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame1 + b'\r\n')


@app.route('/res', methods=['GET', 'POST'])
def res():

    global textMsg
    textMsg = ""

    # url = "https://asltotext.cognitiveservices.azure.com/customvision/v3.0/Prediction/4ea8c1a9-126c-4737-bbc0-c5a83d7eae78/classify/iterations/Iteration1/image"
    url = "https://asltotext.cognitiveservices.azure.com/customvision/v3.0/Prediction/59b8ab1e-0154-47de-9bee-ade8414e8fa2/classify/iterations/Iteration1/image"
    
    headers = {
        'Prediction-Key': '',
        'Content-Type': 'application/octet-stream'
    }
    img_counter = 0
    k = 0
    while True:
        k = cv2.waitKey(3000)
        if k == 27:
            break
        else:
            cv2.imwrite("filename.jpg", frame)
            im = cv2.imread("filename.jpg")
            img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            img = cv2.Canny(img, 100, 200)
            cv2.imwrite("filename.jpg", img)
            with open("filename.jpg", 'rb') as f:
                img_data = f.read()

            body = img_data
            response = requests.post(url, headers=headers, data=body)
            # text = response.json()['predictions'][0]['tagName']
            jsonRes = response.json() 
            max = -1
            tagName = ""
            for x in jsonRes['predictions']:
                if (max < x['probability']):
                    max = x['probability']
                    tagName = x['tagName']
            # print(json.dumps(jsonRes, indent=4))

            textMsg = textMsg + " " + tagName
            print(textMsg)
            img_counter = img_counter + 1
            if img_counter == 4:
                break
    cv2.destroyAllWindows()
    cam.release()
    return jsonify(textMsg)

if(__name__ == "__main__"):
        app.run(host="0.0.0.0")
#app.run(debug=True)
