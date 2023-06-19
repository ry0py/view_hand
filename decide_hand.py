import cv2
from ultralytics import YOLO

class DecideHand:
    def Detect(self): #->torch.Tensor
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        model = YOLO("./runs/detect/train3/weights/best.pt")
        results = model(frame)
        return results[0]
    def GetBoxes(self):#->torch.Tensor
        return self.Detect().boxes
    def GetNames(self):#->torch.Tensor
        return self.Detect().names
    def IsDetect(self)->bool: #検出できてるか判断したいだけなのに検出の処理もしてしまって重くなってそう
        if self.GetBoxes().cls.numel() == 1:
            return True
        else:
            return False
    def CountHandNum(self)->int:
        return self.GetBoxes().cls.numel()
    def GetHand(self)->str:
        return self.DecideHand()
    def DecideViewHand(self)->str:
        names = self.GetNames()
        boxes = self.GetBoxes()
        if self.IsDetect() == False:
            return "None"
        else:
            cls_text = self.Detect().names.get(int(self.Detect.boxes.cls))
            return cls_text
    def DecideAIHand(self)->str: #こいつを使えばいい
        cls_text = self.DecideViewHand()
        if(cls_text == "paper"):
            return "チョキ"
        if(cls_text == "rock"):
            return "パー"
        if(cls_text == "scissors"):
            return "グー"
        if(cls_text == "None"):
            #return "None"
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