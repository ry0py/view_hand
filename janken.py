from flask import Flask, render_template, request
import cv2
from ultralytics import YOLO

app = Flask(__name__)

@app.route('/')
def janken():
    #return "hello"
    return render_template("base.html")
@app.route('/sampleform-post', methods=['Get','POST'])
def sample():
    print('POSTデータ受け取ったので処理します')
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    model = YOLO("./runs/detect/train3/weights/best.pt")
    results = model(frame)
    names = results[0].names
    boxes = results[0].boxes
    names = results[0].names
    if boxes.cls.numel() == 0:
        return "手が検出されませんでした"
    else:
        names.get(int(boxes.cls))
        cls_text = names.get(int(boxes.cls))
        if(cls_text == "paper"):
            return "チョキ"
        if(cls_text == "rock"):
            return "パー"
        if(cls_text == "scissors"):
            return "グー"
        '''
        if boxes.cls.size() == 1:
            names.get(int(boxes.cls))
            cls_text = names.get(int(boxes.cls))
            if(cls_text == "paper"):
                return "チョキ"
            if(cls_text == "rock"):
                return "パー"
            if(cls_text == "scissors"):
                return "グー"
        else:
            return "手が二つあります"
            '''
    '''
    if(not( names.get(boxes) == None)):
        cls_text = names.get(int(boxes))
        if(cls_text == "paper"):
            return "チョキ"
        if(cls_text == "rock"):
            return "パー"
        if(cls_text == "scissors"):
            return "グー"
    else:
        return "None"
    '''
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
