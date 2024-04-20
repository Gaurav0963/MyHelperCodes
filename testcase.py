'''
Converting leetcode linkedlists testcases to executable functions
'''
import os
from datetime import datetime


class TestCode:
    
    def __init__(self):
        self.FILE_PATH: str = ''
    
    
    def create_path(self) -> None:
        # Changing the directory to desired path
        os.chdir('D:\\')
        # Creating file name
        FILE_NAME = f"{datetime.now().strftime('testcase_%Y-%H_%M_%S')}.txt"
        # Creating a folder named "TestCase" to store the data
        TEST_FILE_DIR = os.path.join(os.getcwd(), "TestCase")
        # Making the directory, if it doesn't already exist
        os.makedirs(TEST_FILE_DIR, exist_ok = True)
        # Creating text file path
        self.FILE_PATH = os.path.join(TEST_FILE_DIR, FILE_NAME)
        
    
    def remove(self, res: list) -> list:
        my_list = []
        # Converting data to string type
        for item in res:
            my_list.append(str(item))
        
        for i, item in enumerate(my_list):
            if item.startswith("["):
                my_list[i] = "(" + item[1:-1] + ")" 
        return(my_list)
            
        
    def main(self, l1: list, l2: list) -> None:
        self.create_path()
        mylist = self.remove(l2)
        text = ''
        with open(self.FILE_PATH, 'w+') as f:
            for i, j in zip(l1, mylist):
                if i == 'get':
                    text = 'print(obj.'+i+j+')'
                else:
                    text = 'obj.'+i+j
                f.write(text.strip())
                f.write('\n')
                


if __name__ == '__main__':
    l=["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
    m = [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[100]]
    obj = TestCode()
    obj.main(l, m)