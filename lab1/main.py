import tkinter as tk
from tkinter import filedialog
from Window import Window

def main():
    window = Window()
    window.run()

if __name__ == '__main__':
    main()

# def open_file():
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         selected_file_label.config(text=f"Selected File: {file_path}")
#
# root = tk.Tk()
# root.title("File Selection Example")
#
# browse_button = tk.Button(root, text="Browse", command=open_file)
# browse_button.pack(pady=20)
#
# selected_file_label = tk.Label(root, text="Selected File: None")
# selected_file_label.pack()

