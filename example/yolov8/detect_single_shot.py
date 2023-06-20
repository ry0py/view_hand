from ultralytics import YOLO
import cv2
# Load a model

model = YOLO("./runs/detect/train2/weights/best.pt")  # インスタンスを生成してる(C++のインスタンスの生成とはやり方が違う) 
# Use the model
cap = cv2.VideoCapture(0)
#frameには画像が入る
ret, frame = cap.read()

results = model(frame,show =True)  # frameでも検出してくれる
masks = results[0].masks  # Masks object

# 以下3つでラベルを取得できる
names = results[0].names
boxes = results[0].boxes
#boxes.clsはTensor型というもの
'''
numel()は要素数を返す
size()は行列のサイズを返す
'''
if boxes.cls.numel() == 0:
    print(boxes.cls)
else:
    print(names.get(int(boxes.cls)))
'''
if(names.get(boxes) == None):
    cls_text = None
else:
    cls_text = names.get(int(boxes)) # 何も検出されてないときエラーが出てしまう
'''
#print(cls_text)

'''
while True:
    cv2.imshow("frame",frame)
    res_plotted = results[0].plot()
    #cv2.imshow("result",res_plotted)
    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break
'''