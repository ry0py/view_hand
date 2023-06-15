from ultralytics import YOLO

# Load a model
#model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("./runs/detect/train3/weights/best.pt")  # load a .pt file from disk
# Use the model
results = model("./data/test/708544955.697029.mp4",save=True)  # predict on an image フォルダ形式じゃないといけない&\には対応してないからエラー出るから気を付けて
