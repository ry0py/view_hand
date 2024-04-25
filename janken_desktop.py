import tkinter as tk
from decide_hand import DecideHand 
from PIL import ImageTk
import serial

# いらないかも
import cv2
import sys
import os

import os

import time
dh = DecideHand()

class win(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title('じゃんけんゲーム') # 画面タイトル設定
        self.master.geometry('1540x960')  # 画面サイズ設定
        self.master.resizable(False, False) # リサイズ設定
        label_1a = tk.Label( text='じゃんけんゲーム', font=('', 80))
        label_1a.pack()
        button_lose = tk.Button( text='君の勝ち', command=self.getwin_lose,font=('', 60))#getwinに引数与えてやるとなぜか実行される
        button_lose.pack(padx=40, pady=50)
        button_win = tk.Button( text='君の負け', command=self.getwin_win,font=('', 60))
        button_win.pack(padx=40, pady=50)
        button_draw = tk.Button( text='以心伝心', command=self.getwin_draw,font=('', 60))
        button_draw.pack(padx=40, pady=50)
        # self.ser = serial.Serial('COM12',9600)
    def send_serial(self,hand):
        if hand == "scissors":
            # self.ser.write(bytes('scissors\n',encoding='ascii'))
            print("scissors")
        elif hand == "paper":
            # self.ser.write(bytes('paper\n',encoding='ascii'))
            print("paper")
        elif hand == "rock":
            # self.ser.write(bytes('rock\n',encoding='ascii'))
            print("rock")
        elif hand == "None":
            # self.ser.write(b'None')
            print("None")
    def getwin_lose(self):
        subWindow = tk.Toplevel(self.master)
        subWindow.title('お前の勝ち') # 画面タイトル設定
        subWindow.geometry('1540x960')  # 画面サイズ設定
        subWindow.resizable(False, False) # リサイズ設定
        janken=dh.DecideAIHand(battle="lose")
        self.send_serial(janken[0])
        if(janken[0]=="None"):
            text = "見えないです"
        else:
            text = "なかなかやるね"
        label_sub = tk.Label( subWindow,text=text, font=('', 30))
        label_sub.pack()
        self.image = ImageTk.PhotoImage(file = janken[1]) 
        canvas = tk.Canvas(
            subWindow,
            width = 1080,
            height = 1080,
            bg = "white",
        )
        canvas.pack()
        canvas.create_image(
            0, 0,
            image=self.image,  # こっちはうまくいく。
            # image=ImageTk.PhotoImage(file="tmp.png"),  # こうするとうまくいかない。
            anchor=tk.NW
        )
        self.master.after(5000,subWindow.destroy)
    def getwin_win(self):
        subWindow = tk.Toplevel(self.master)
        subWindow.title('俺の負け') # 画面タイトル設定
        subWindow.geometry('1540x960')  # 画面サイズ設定
        subWindow.resizable(False, False) # リサイズ設定
        janken = dh.DecideAIHand(battle="win")
        self.send_serial(janken[0])
        if(janken[0]=="None"):
            text = "見えないです。"
        else:
            text = "いえーーい！！！"
        label_sub = tk.Label( subWindow,text=text, font=('', 30))
        label_sub.pack()
        self.image = ImageTk.PhotoImage(file = janken[1]) 
        canvas = tk.Canvas(
            subWindow,
            width =1080,
            height = 1080,
            bg = "white",
        )
        canvas.pack()
        canvas.create_image(
            0, 0,
            image=self.image,  # こっちはうまくいく。
            # image=ImageTk.PhotoImage(file="tmp.png"),  # こうするとうまくいかない。
            anchor=tk.NW
        )
        self.master.after(5000,subWindow.destroy)
    def getwin_draw(self):
        subWindow = tk.Toplevel(self.master)
        subWindow.title('以心伝心') # 画面タイトル設定
        subWindow.geometry('1540x960')  # 画面サイズ設定
        subWindow.resizable(False, False) # リサイズ設定
        janken = dh.DecideAIHand(battle="draw")
        self.send_serial(janken[0])
        if(janken[0]=="None"):
            text = "見えないです。"
        else:
            text = "あいこだね"
        label_sub = tk.Label( subWindow,text=text, font=('', 30))
        label_sub.pack()
        #画像読み込み(画像は任意の画像へのパスにすること)
        self.image = ImageTk.PhotoImage(file = janken[1]) 
        canvas = tk.Canvas(
            subWindow,
            width = 1080,
            height = 1080,
            bg = "white",
        )
        canvas.pack()
        canvas.create_image(
            0, 0,
            image=self.image,  # こっちはうまくいく。
            # image=ImageTk.PhotoImage(file="tmp.png"),  # こうするとうまくいかない。
            anchor=tk.NW
        )
        self.master.after(5000,subWindow.destroy)
if __name__ == '__main__':
    root = tk.Tk()
    win1 = win(master=root)
    root.mainloop()

        
    