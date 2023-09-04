import tkinter as tk

from Window import Window


def main():
    # Create the main application window
    root = tk.Tk()

    # Create an instance of the PopupWindow class
    window = Window(root)

    # Start the main tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
