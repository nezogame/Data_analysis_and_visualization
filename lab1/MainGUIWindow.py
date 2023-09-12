import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from FileReader import FileReader
from random import randrange
from Controller import create_frequency_table
from Controller import create_table_tab

class Window:
    __IMG = Image.open("img\\browse-document-icon.png")
    __IMG = __IMG.resize((22, 22), Image.LANCZOS)
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Data analysis")
        self.root.geometry("500x600")
        self.root.config(background="#272822")
        self.root.resizable(False,False)
        self.browse_img =  ImageTk.PhotoImage(self.__IMG)
        self.question_inscription = tk.Label(self.root,text="Hello dude, do you want some magic???",font=25).place(x=60,y=30)
        self.inviting_inscription = tk.Label(self.root,text="If your answer is yes just select an option",font=25).place(x=60,y=65)
        self.frequency_chekbox = tk.Label(self.root,text="Build frequency table").place(x=60,y=130)
        self.frequency_chekbox = tk.Label(self.root,text="Split frequencies table into classes").place(x=60,y=160)
        self.frequency_chekbox = tk.Label(self.root,text="3").place(x=60,y=190)
        self.frequency_chekbox = tk.Label(self.root,text="4").place(x=60,y=220)
        self.frequency_chekbox = tk.Label(self.root,text="5").place(x=60,y=250)
        self.frequency_chekbox = tk.Label(self.root,text="6").place(x=60,y=280)
        self.frequency_chekbox = tk.Label(self.root,text="7").place(x=60,y=310)
        self.frequency_chekbox = tk.Label(self.root,text="8").place(x=60,y=340)
        self.frequency_chekbox = tk.Label(self.root,text="9").place(x=60,y=370)
        self.file_path_field  = tk.Entry(self.root,width=200,bg="#D3D3D3")
        self.file_path_field.place(x=50,y=460, height=22,width=340)
        self.error_label = tk.Label(self.root,
                                             text="Selected file is wrong it should be .DAT or .TXT\n chose in data_lab1,2 folder",
                                             font="Arial 15")
        self.btn_get_path = tk.Button(self.root, image=self.browse_img,
                                      command=lambda :self.browse_files(self.file_path_field)).place(x=400,y=460, height=22)
        self.btn_submit = tk.Button(self.root, text="Submit", justify="center", command=lambda : self.submit_selected(self.file_path_field.get()))
        self.btn_submit.place(x=380,y=490)

    def run(self):
        self.root.mainloop()

    def browse_files(self, entry_field):
        path = filedialog.askopenfilename()
        entry_field.delete(0,tk.END)
        entry_field.insert(0,path)

    def submit_selected(self,file_path):
        try:
            file_reader = FileReader(file_path)
        except NameError as e:
            # self.file_path_field.config({"background": "#D3D3D3"})
            self.display_error_frong_file()
            print(e)
        else:
            self.hide_error_frong_file()
            create_table_tab(file_reader.get_file_object())

    def hide_error_frong_file(self):
        self.error_label.place_forget()
        self.file_path_field.config(highlightthickness=0)
    def display_error_frong_file(self):
        self.file_path_field.config(highlightbackground = "red",highlightcolor="red",highlightthickness=2)
        self.error_label.place(x=40, y=520)