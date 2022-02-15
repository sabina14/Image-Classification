import base64

def decodeImage(imgstring,fileName):
    imgdata=base64.b64decode(imgstring)
    with open(fileName,'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImage(croppedIamgePath):
    with open(croppedIamgePath,'rb') as f:
        return base64.b64encode(f.read())