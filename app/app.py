from flask import Flask, render_template, request
from keras.preprocessing import image
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import VGG16
from keras.models import load_model
import numpy as np
app = Flask(__name__)

code = {0:'failure',1:'noraml',2:'Covid',3:'lung atama'}

model = load_model('/app/model/best_model.h5')

def getcode(n):
    for x, y in code.items():
        if n == y:
            return x

@app.route('/', methods = ['GET'])
def showt():
    status = {'author_name':'admin',
            'status':'working'}
            
    return status

@app.route('/predict', methods = ['POST'])
def predict():
    img_file = request.files['imagefile']
    img_path = '/app/images/' + img_file.filename
    img_file.save(img_path)
    img = load_img(img_path, target_size=(299, 299))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)    
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction, axis=1)
    class_name = code[class_index[0]]
    
    return {'class_name': class_name}

if __name__ =='__main__':
    app.run(host='0.0.0.0',port = 4000, debug = True)
