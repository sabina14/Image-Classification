import numpy as np
from keras.models import load_model
from keras.preprocessing import image

class ImageClassifier:
    def __init__(self,fileName):
        self.fileName=fileName

    def predictimage(self):

        model=load_model('vgg16_modcode.h5')

        imagename=self.fileName
        test_image=image.load_img(imagename, target_size=(224,224))
        test_image=image.img_to_array(test_image)
        test_image=np.expand_dims(test_image, axis=0)
        result= model.predict(test_image)

        if result[0][0]==1:
            prediction='BookStore'
            return[{"image": prediction}]

        elif result[0][1]==1:
            prediction='gym'
            return [{"image": prediction}]

        elif result[0][2] == 1:
            prediction = 'HairSalon'
            return [{"image": prediction}]

        elif result[0][3] == 1:
            prediction = 'House'
            return [{"image": prediction}]

        if result[0][4] == 1:
            prediction = 'restaurant'
            return [{"image": prediction}]

        elif result[0][5] == 1:
            prediction = 'subway'
            return [{"image": prediction}]
        elif result[0][6] == 1:
            prediction = 'Toystore'
            return [{"image": prediction}]
        elif result[0][7] == 1:
            prediction = 'WineCellar'
            return [{"image": prediction}]