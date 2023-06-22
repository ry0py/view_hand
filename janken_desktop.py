import tkinter as tk
from decide_hand import DecideHand #本当はDecideAIHandのみを使いたい
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
        button_lose = tk.Button( text='負けた', command=self.getwin_lose)#getwinに引数与えてやるとなぜか実行される
        button_lose.pack(padx=5, pady=10)
        button_win = tk.Button( text='勝った', command=self.getwin_win)
        button_win.pack(padx=5, pady=10)
        button_draw = tk.Button( text='あいこ', command=self.getwin_draw)
        button_draw.pack(padx=5, pady=10)

    def getwin_lose(self):
        subWindow = tk.Toplevel(self.master)
        subWindow.title('勝敗') # 画面タイトル設定
        subWindow.geometry('500x500')  # 画面サイズ設定
        subWindow.resizable(False, False) # リサイズ設定
        label_sub = tk.Label( subWindow,text=dh.DecideAIHand(battle="lose"), font=('', 30))
        label_sub.pack()
    def getwin_win(self):
        subWindow = tk.Toplevel(self.master)
        subWindow.title('勝敗') # 画面タイトル設定
        subWindow.geometry('500x500')  # 画面サイズ設定
        subWindow.resizable(False, False) # リサイズ設定
        label_sub = tk.Label( subWindow,text=dh.DecideAIHand(battle="win"), font=('', 30))
        label_sub.pack()
        image = PhotoImage() 
        label_3 = Label(frame3, image=image)
        label_3.pack(pady=20)   
    def getwin_draw(self):
        subWindow = tk.Toplevel(self.master)
        subWindow.title('勝敗') # 画面タイトル設定
        subWindow.geometry('500x500')  # 画面サイズ設定
        subWindow.resizable(False, False) # リサイズ設定
        label_sub = tk.Label( subWindow,text=dh.DecideAIHand(battle="draw"), font=('', 30))
        label_sub.pack()

if __name__ == '__main__':
    root = tk.Tk()
    win1 = win(master=root)
    root.mainloop()

        
    