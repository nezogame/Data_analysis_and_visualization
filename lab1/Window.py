import tkinter as tk
from tkinter import ttk
class BaseWindow:
    def __init__(self,data):
        self.__root = tk.Tk()
        self.__data = data
        self.__root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def __ne__(self, __o: object) -> bool:
        return super().__ne__(__o)

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()

    def __hash__(self) -> int:
        return super().__hash__()

    def __sizeof__(self) -> int:
        return super().__sizeof__()

    def get_data(self):
        return self.__data

    def set_data(self,data):
        try:
            self.__data = data
        except Exception as e:
            print(self.__class__.__repr__()+"\nException message "+e)

    def get_root(self):
        return self.__root

    def set_root(self, tk):
        self.__root = tk
    def on_closing(self):
        self.__root.withdraw()
