import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from FileReader import FileReader


class Window:
    IMG = Image.open("img\\browse-document-icon.png")
    IMG = IMG.resize((22, 22), Image.LANCZOS)
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Data analysis")
        self.root.geometry("500x500")
        # Set window background color
        self.root.config(background="#272822")
        self.root.resizable(False,False)
        self.browse_img =  ImageTk.PhotoImage(self.IMG)
        self.question_inscription = tk.Label(self.root,text="Hello dude, do you want some magic???",font=25).place(x=100,y=30)
        self.inviting_inscription = tk.Label(self.root,text="If your answer is yes just ",font=25).place(x=100,y=65)
        self.file_path_field  = tk.Entry(self.root,width=200)
        self.file_path_field.place(x=50,y=325, height=22,width=340)
        self.btn_get_path = tk.Button(self.root, image=self.browse_img,
                                      command=lambda :self.browse_files(self.file_path_field)).place(x=400,y=325, height=22)
        self.btn_submit = tk.Button(self.root, text="Submit", justify="center", command=lambda : self.print(self.file_path_field.get()))
        self.btn_submit.place(x=380,y=355)

    def run(self):
        self.root.mainloop()

    def browse_files(self, entry_field):
        path = filedialog.askopenfilename()
        entry_field.delete(0,tk.END)
        entry_field.insert(0,path)

    def print(self,file_path):
        file_reader = FileReader(file_path)
        file_reader.print_all_data()