from ultralytics import YOLO
# Train the model
model = YOLO('yolov8n.pt')
model.train(data='./data/hand.yaml', epochs=150)