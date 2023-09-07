import numpy as np
import pandas as pd
import dataclasses as dataclass

class FileReader:
    def __init__(self,file_path):
        if not file_path.lower().endswith(('.dat','.txt')):
            raise NameError("File must be a '.dat' or '.txt' extension")
        self.path = file_path
        self.__file_data = self.open_file(self.path)

    def open_file(self,path):
        data=[]
        with open(path,'r') as file_reader:
            for line in file_reader:
                for num in line.split():
                    data.append(float(num))
            return np.array(data,dtype=float)
        #     return [float(num) for line in file for num in line.split()]

    def get_file_object(self):
        return self.__file_data
