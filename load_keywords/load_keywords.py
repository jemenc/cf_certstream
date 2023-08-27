
import os
import csv
from .keywords import Keywords

class LoadKeyworsFromFile(Keywords):

    def __init__(self,file_name:str="Keywords.csv") -> None:
        super().__init__()
        self.__current_path = os.path.abspath(os.curdir) + '/load_keywords/'
        self.__file_name = file_name
        self.__keys = list()
        self.load_keywords()

    @property
    def current_path(self):
        return self.__current_path

    @property
    def file_name(self):
        return self.__file_name

    @property
    def keys(self) -> list:
        return self.__keys

    @keys.setter
    def keys(self,keyword:str=None):
        if keyword:
            self.__keys.append(keyword)
    
    #overwrite abstract method
    def load_keywords(self):
        with open(file=self.current_path + self.file_name,newline="") as file:
            reader = csv.reader(file,delimiter=',')
            for row in reader:
                self.__keys.append(row[0])
                
    #overwrite abstract method
    def save_keyword(self,value:str=None):
        with open(file=self.current_path + self.file_name,mode='a',newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow([value])

    #overwrite abstract method
    def delete_keyword(self):
        pass


if __name__ == "__main__":
    keyword = LoadKeyworsFromFile()
    keyword.save_keyword(value='ayudabdcl')
    print(keyword.keys)