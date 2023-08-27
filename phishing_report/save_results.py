import os
import sys
sys.path.append(os.path.abspath(os.curdir))
from decorators.decorators import add_date

class SaveResults():

    def __init__(self,file_name:str=None,path:str=None) -> None:
        self.__location = path if path else os.path.abspath(os.curdir) + '/phishing_report/'
        self.__file_name = file_name if file_name else "suspicious_urls.txt"
        print(os.path.abspath(os.curdir))

    @add_date
    def write_result(self,message:str=None):
        with open(file=self.__location + self.__file_name,mode='a') as file:
            file.write(str(message) + "\n")

if __name__ == "__main__":
    write = SaveResults()
    write.write_result(message="test message")
