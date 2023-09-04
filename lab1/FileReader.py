class FileReader:
    def __init__(self,file_path):
        if not file_path.lower().endswith(('.dat','.txt')):
            raise NameError("File must be a '.dat' or '.txt' extension")
        self.path = file_path
        self.file_object = self.open_file(self.path)

    def open_file(self,path):
        with open(path,'r') as reader:
            return reader.readlines()

    def print_all_data(self):
        print(self.file_object)
