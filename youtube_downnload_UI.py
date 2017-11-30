from tkinter import *
from pytube import YouTube
import threading

class GUIDemo(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        #print(type(master))
        #self.master = master
        self.display = StringVar()
        master.title("Youtube download")
        self.display.set("等待轉換!!")
        self.btnText = StringVar()
        self.btnText.set("確定")
        self.createWidgets()
 
    def createWidgets(self):

        self.inputText = Label(self)
        self.inputText["text"] = "youtube網址:"
        self.inputText.grid(row=0, column=0)
        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField.grid(row=0, column=1, columnspan=6)

        #self.nameText = Label(self)
        #self.nameText["text"] = "檔案名字:"
        #self.nameText.grid(row=1, column=0)
        #self.nameField = Entry(self)
        #self.nameField["width"] = 50
        #self.nameField.grid(row=1, column=1, columnspan=6)

        def function_transfer():
            youtube_adr = self.inputField.get()            
            print ("index1",youtube_adr)
            DownloadClass(url = youtube_adr,dis = self.display).start() # 啟動執行緒 
            

        self.btnTrans = Button(self)
        self.btnTrans["textvariable"] = self.btnText
        self.btnTrans.grid(row=2, column=0, columnspan=7)
        self.btnTrans["command"] = function_transfer
 
        self.displayText = Label(self)
        self.displayText["textvariable"] = self.display
        self.displayText.grid(row=3, column=0, columnspan=7)

class DownloadClass (threading.Thread): # 繼承 Thread 類別
    def __init__(self,url=None,dis=None):
        threading.Thread.__init__(self)
        self.url = url
        self.dis = dis
        self.dis.set("開始轉換!!")

    def run(self): # 覆載 (Override) Thread 類別的方法(函數)
        try:
            yt_data = YouTube(self.url)
            sls = yt_data.streams.filter(subtype='mp4').first()
            sls.download()
            self.dis.set("轉換結束!")
        except:
            self.dis.set("轉換失敗!")
        print ("finish!!")


if __name__ == '__main__':
    root = Tk()
    root.title("Youtube 下載器")
    app = GUIDemo(master=root)
    app.mainloop()