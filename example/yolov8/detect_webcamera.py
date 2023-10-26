from ultralytics import YOLO
import cv2
# Load a model
model = YOLO("./runs/detect/train2/weights/best.pt")  # インスタンスを生成してる(C++のインスタンスの生成とはやり方が違う) 
# Use the model
results = model(0,show=True)  # webカメラで撮影した画像を検出する場合はこっち
