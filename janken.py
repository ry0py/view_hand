from flask import Flask, render_template, request
import cv2
from ultralytics import YOLO

app = Flask(__name__,static_folder='./templates/images')

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
        answer = "手が検出されませんでした"
        return render_template("result_none.html", answer=answer)
    else:
        names.get(int(boxes.cls))
        cls_text = names.get(int(boxes.cls))
        if(cls_text == "paper"):
            answer = "チョキ"
            return render_template("result_scissors.html", answer=answer)
        if(cls_text == "rock"):
            answer = "パー"
            return render_template("result_paper.html", answer=answer)
        if(cls_text == "scissors"):
            answer = "グー"
            return render_template("result_rock.html", answer=answer)
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
