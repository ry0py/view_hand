from ultralytics import YOLO
# Train the model
model = YOLO('./runs/detect/train2/weights/best.pt')
model.train(data='./data/hand.yaml', epochs=100)