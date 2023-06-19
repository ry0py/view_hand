import cv2
from ultralytics import YOLO


class DecideHand:

    def Detect(self)->None:  # ->torch.Tensor
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        model = YOLO("./runs/detect/train3/weights/best.pt")
        results = model(frame)
        self.names = results[0].names
        self.boxes = results[0].boxes
        cap.release()

    def IsDetect(self) -> bool:  # 検出できてるか判断したいだけなのに検出の処理もしてしまって重くなってそう
        if self.boxes.cls.numel() == 1:
            return True
        else:
            return False

    def CountHandNum(self) -> int:
        return self.boxes.cls.numel()

    def DecideViewHand(self) -> str:
        self.Detect()
        if self.IsDetect() == False:
            return "None"
        else:
            cls_text = self.names.get(int(self.boxes.cls))
            return cls_text

    def DecideAIHand(self) -> str:  # こいつを使えばいい
        cls_text = self.DecideViewHand()
        if(cls_text == "paper"):
            return "チョキ"
        if(cls_text == "rock"):
            return "パー"
        if(cls_text == "scissors"):
            return "グー"
        if(cls_text == "None"):
            hand_num = self.CountHandNum()
            return "手が" + str(hand_num) + "つあります"
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
