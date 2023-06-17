from ultralytics import YOLO
import cv2
# Load a model

model = YOLO("./runs/detect/train3/weights/best.pt")  # インスタンスを生成してる(C++のインスタンスの生成とはやり方が違う) 
# Use the model

results = model("./data/test/S__44785668.jpg",show = True)# predict on an image フォルダ形式じゃないといけない&\には対応してないからエラー出るから気を付けて
#results = model(0,show=True)  # webカメラで撮影した画像を検出する場合はこっち

# 以下3つでラベルを取得できる
names = results[0].names
boxes = results[0].boxes.cls
cls_text = names.get(int(boxes))

print(cls_text)

'''
while True:
    cv2.imshow("frame",frame)
    res_plotted = results[0].plot()
    #cv2.imshow("result",res_plotted)
    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break
'''