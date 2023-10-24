import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0" # これやったらcapが早くなった
import cv2
from ultralytics import YOLO
import random
from typing import Tuple
import time


class DecideHand:
    def __init__(self):
        self.names = None
        self.boxes = None
        self.cls_text = None
        self.model = YOLO("./runs/detect/train2/weights/best.pt")
    def Detect(self)->None:  # ->torch.Tensor
        self.cap = cv2.VideoCapture(0)
        ret, frame =self.cap.read()
        results = self.model.predict(frame,show = True,conf = 0.5) # 閾値を設定
        self.names = results[0].names
        self.boxes = results[0].boxes
        self.result_path = results[0].path
        self.cap.release()

    def IsDetect(self) -> bool:  # たくさんあっても同じ手ならtrue帰す
        print(self.boxes.cls)
        if self.boxes.cls.numel() == 0:
            return False
        else:
            return len(set(self.boxes.cls.tolist()))==1
        # if self.boxes.cls.numel() == 1:
        #     return True
        # else:
        #     return False

    def CountHandNum(self) -> int:
        return self.boxes.cls.numel()

    def DecideViewHand(self) -> None:
        self.Detect()
        if self.IsDetect():
           self.cls_text = self.names.get(int(self.boxes.cls))
        else:
            self.cls_text = "None"
    def ViewHandImage(self) -> None:
        cv2.imshow("frame", self.result_path[0])

    def Win(self)->Tuple[str,str]:
        if(self.cls_text == "paper"):
            return "scissors","./templates/images/scissors.png"
        elif(self.cls_text == "rock"):
            return "paper","./templates/images/paper.png"
        elif(self.cls_text == "scissors"):
            return "rock","./templates/images/rock.png"
        else:
            return "None", "./templates/images/error.png"
    
    def Lose(self)->Tuple[str,str]:
        if(self.cls_text == "paper"):
            return "rock","./templates/images/rock.png"
        elif(self.cls_text == "rock"):
            return "scissors","./templates/images/scissors.png"
        elif(self.cls_text == "scissors"):
            return "paper", "./templates/images/paper.png"
        else:
            return "None", "./templates/images/error.png"
    
    def Draw(self)->Tuple[str,str]:
        if(self.cls_text == "paper"):
            return "paper","./templates/images/paper.png"
        elif(self.cls_text == "rock"):
            return "rock","./templates/images/rock.png"
        elif(self.cls_text == "scissors"):
            return "scissors","./templates/images/scissors.png"
        else:
            return "None", "./templates/images/error.png"
    
    def Random(self)->str:
        random_hand = random.randrange(3)
        if(random_hand == 0):
            return "scissors"
        elif(random_hand == 1):
            return "rock"
        elif(random_hand == 2):
            return "paper"
        else:
            return "None"

    def DecideAIHand(self,battle = "win") -> Tuple[str,str]:  # こいつを使えばいい
        self.DecideViewHand()
        if(battle == "win"):
            return self.Win()
        if(battle == "lose"):
            return self.Lose()
        if(battle == "draw"):
            return self.Draw()
        ''' randomだけ出力UIを変えないといけない
        if(battle == "random"):
            return self.Random()
        '''
        '''
        if boxes.cls.size() == 1:
            names.get(int(boxes.cls))
            cls_text = names.get(int(boxes.cls))
            if(cls_text == "paper"):
                return "scissors"
            if(cls_text == "rock"):
                return "paper"
            if(cls_text == "scissors"):
                return "rock"
        else:
            return "手が二つあります"
            '''
def main():
    dh = DecideHand()
    dh.DecideAIHand()
if __name__ == "__main__":
    main() 