from flask import Flask,request,jsonify,render_template
import os
from flask_cors import CORS, cross_origin
from common.utils import decodeImage
from predict import ImageClassifier



app=Flask(__name__)

CORS(app)

class UI:
    def __init__(self):
        self.fileName='inputImage.jpg'
        self.classifier=ImageClassifier(self.fileName)

@app.route("/",methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
@cross_origin()
def predictRoute():
    image=request.json['image']
    decodeImage(image,fr_end.fileName)
    result=fr_end.classifier.predictimage()
    return jsonify(result)

if __name__== "__main__":
    fr_end=UI()

    app.run(host='127.0.0.1',port=5000,debug=True)