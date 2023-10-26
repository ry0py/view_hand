import tkinter as tk
from decide_hand import DecideHand 
from PIL import ImageTk
import serial

# いらないかも
import cv2
import sys
import os

import os
dh = DecideHand()

class win(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title('じゃんけんゲーム') # 画面タイトル設定
        self.master.geometry('500x500')  # 画面サイズ設定
        self.master.resizable(False, False) # リサイズ設定
        label_1a = tk.Label( text='じゃんけんゲーム', font=('', 30))
        label_1a.pack()
        button_lose = tk.Button( text='お前の勝ち', command=self.getwin_lose)#getwinに引数与えてやるとなぜか実行される
        button_lose.pack(padx=30, pady=50)
        button_win = tk.Button( text='お前の負け', command=self.getwin_win)
        button_win.pack(padx=30, pady=50)
        button_draw = tk.Button( text='以心伝心', command=self.getwin_draw)
        button_draw.pack(padx=30, pady=50)
        self.ser = serial.Serial('COM12',9600)
    def send_serial(self,hand):
        if hand == "scissors":
            self.ser.write(bytes('scissor\n',encoding='ascii'))
            print("scissors")
        elif hand == "paper":
            self.ser.write(bytes('paper\n',encoding='ascii'))
            print("paper")
        elif hand == "rock":
            print(bytes('rock',encoding = 'ascii'))
            self.ser.write(bytes('rock\n',encoding='ascii'))
            print("rock")
        elif hand == "None":
            self.ser.write(b'None')
            print("None")
    def getwin_lose(self):
        subWindow = tk.Toplevel(self.master)
        subWindow.title('お前の勝ち') # 画面タイトル設定
        subWindow.geometry('500x500')  # 画面サイズ設定
        subWindow.resizable(False, False) # リサイズ設定
        janken=dh.DecideAIHand(battle="lose")
        self.send_serial(janken[0])
        if(janken[0]=="None"):
            text = "ちゃんと出せやボケが！！！"
        else:
            text = "なかなかやるな！！！"
        label_sub = tk.Label( subWindow,text=text, font=('', 30))
        label_sub.pack()
        self.image = ImageTk.PhotoImage(file = janken[1]) 
        canvas = tk.Canvas(
            subWindow,
            width = 320,
            height = 190,
            bg = "white",
        )
        canvas.pack()
        canvas.create_image(
            0, 0,
            image=self.image,  # こっちはうまくいく。
            # image=ImageTk.PhotoImage(file="tmp.png"),  # こうするとうまくいかない。
            anchor=tk.NW
        )
    def getwin_win(self):
        subWindow = tk.Toplevel(self.master)
        subWindow.title('俺の負け') # 画面タイトル設定
        subWindow.geometry('500x500')  # 画面サイズ設定
        subWindow.resizable(False, False) # リサイズ設定
        janken = dh.DecideAIHand(battle="win")
        self.send_serial(janken[0])
        if(janken[0]=="None"):
            text = "ちゃんと出せやボケが！！！"
        else:
            text = "ざーーーーこwwww！！！"
        label_sub = tk.Label( subWindow,text=text, font=('', 30))
        label_sub.pack()
        self.image = ImageTk.PhotoImage(file = janken[1]) 
        canvas = tk.Canvas(
            subWindow,
            width = 320,
            height = 190,
            bg = "white",
        )
        canvas.pack()
        canvas.create_image(
            0, 0,
            image=self.image,  # こっちはうまくいく。
            # image=ImageTk.PhotoImage(file="tmp.png"),  # こうするとうまくいかない。
            anchor=tk.NW
        )
    def getwin_draw(self):
        subWindow = tk.Toplevel(self.master)
        subWindow.title('以心伝心') # 画面タイトル設定
        subWindow.geometry('500x500')  # 画面サイズ設定
        subWindow.resizable(False, False) # リサイズ設定
        janken = dh.DecideAIHand(battle="draw")
        self.send_serial(janken[0])
        if(janken[0]=="None"):
            text = "ちゃんと出せやボケが！！！"
        else:
            text = "あいこだな！"
        label_sub = tk.Label( subWindow,text=text, font=('', 30))
        label_sub.pack()
        #画像読み込み(画像は任意の画像へのパスにすること)
        self.image = ImageTk.PhotoImage(file = janken[1]) 
        canvas = tk.Canvas(
            subWindow,
            width = 320,
            height = 190,
            bg = "white",
        )
        canvas.pack()
        canvas.create_image(
            0, 0,
            image=self.image,  # こっちはうまくいく。
            # image=ImageTk.PhotoImage(file="tmp.png"),  # こうするとうまくいかない。
            anchor=tk.NW
        )
if __name__ == '__main__':
    root = tk.Tk()
    win1 = win(master=root)
    root.mainloop()

        
    