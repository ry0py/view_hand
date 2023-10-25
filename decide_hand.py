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
    def Detect(self)->None:  # ->torch.Tensor
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        model = YOLO("./runs/detect/train3/weights/best.pt")
        results = model(frame,show = True)
        self.names = results[0].names
        self.boxes = results[0].boxes
        self.result_path = results[0].path
        cap.release()

    def IsDetect(self) -> bool:  # 検出できてるか判断したいだけなのに検出の処理もしてしまって重くなってそう
        if self.boxes.cls.numel() == 1:
            return True
        else:
            return False

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
            return "チョキ","./templates/images/scissors.png"
        elif(self.cls_text == "rock"):
            return "パー","./templates/images/paper.png"
        elif(self.cls_text == "scissors"):
            return "グー","./templates/images/rock.png"
        else:
            return "None", "./templates/images/error.png"
    
    def Lose(self)->Tuple[str,str]:
        if(self.cls_text == "paper"):
            return "グー","./templates/images/rock.png"
        elif(self.cls_text == "rock"):
            return "チョキ","./templates/images/scissors.png"
        elif(self.cls_text == "scissors"):
            return "パー", "./templates/images/paper.png"
        else:
            return "None", "./templates/images/error.png"
    
    def Draw(self)->Tuple[str,str]:
        if(self.cls_text == "paper"):
            return "パー","./templates/images/paper.png"
        elif(self.cls_text == "rock"):
            return "グー","./templates/images/rock.png"
        elif(self.cls_text == "scissors"):
            return "チョキ","./templates/images/scissors.png"
        else:
            return "None", "./templates/images/error.png"
    
    def Random(self)->str:
        random_hand = random.randrange(3)
        if(random_hand == 0):
            return "チョキ"
        elif(random_hand == 1):
            return "グー"
        elif(random_hand == 2):
            return "パー"
        else:
            return "None"

    # これを呼ぶだけでいい
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
                return "チョキ"
            if(cls_text == "rock"):
                return "パー"
            if(cls_text == "scissors"):
                return "グー"
        else:
            return "手が二つあります"
            '''
def main():
    start_time = time.time()
    dh = DecideHand()
    print("DecideHand time: ", time.time() - start_time) # 0
    print(dh.DecideAIHand(battle = "win")) #ここが少し時間がかかる
    print("DecideHand time_after: ", time.time() - start_time) # 2.0
if __name__ == "__main__":
    main()
