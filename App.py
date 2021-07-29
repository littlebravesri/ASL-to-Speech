import json
import PIL.Image as Image
from flask import Flask, jsonify, request, render_template, Response
#import cv2
import requests

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('JavascriptWebCam.html')


@app.route('/res', methods=['GET', 'POST'])
def res():

    global textMsg
    textMsg = ""

    url = "https://asltotext.cognitiveservices.azure.com/customvision/v3.0/Prediction/59b8ab1e-0154-47de-9bee-ade8414e8fa2/classify/iterations/Iteration2/image"

    headers = {
        'Prediction-Key': 'c5bfffe88b5c4831a30502b4a5fa7921',
        'Content-Type': 'application/octet-stream'
    }
    img_counter = 0
    k = 0
    #while True:
        #k = cv2.waitKey(1000)
        #if k == 27:
         #   break
        #else:
            #cv2.imwrite("filename.jpg", frame)
            #im = cv2.imread("filename.jpg")
            #img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            #img = cv2.Canny(img, 100, 200)
            #cv2.imwrite("filename.jpg", img)
            #with open("filename.jpg", 'rb') as f:
             #   img_data = f.read()

            #body = img_data
            #response = requests.post(url, headers=headers, data=body)
            ## text = response.json()['predictions'][0]['tagName']
            #jsonRes = response.json()
            #max = -1
            #tagName = ""
            #for x in jsonRes['predictions']:
             #   if (max < x['probability']):
              #      max = x['probability']
               #     tagName = x['tagName']
            ## print(json.dumps(jsonRes, indent=4))

#            textMsg = textMsg + " " + tagName
 #           print(textMsg)
  #          img_counter = img_counter + 1
   #         if img_counter == 4:
    #            break
   # cv2.destroyAllWindows()
    #cam.release()
    return "Hello World"


# app.run(debug=True)
