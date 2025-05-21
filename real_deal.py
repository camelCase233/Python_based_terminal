# import os
from pathlib import Path
import argparse
# import sys

with open('current_dir.txt', 'r') as file:
    content = file.read()
    file.seek(0)



class file_system:
    current_directory = Path(content)
    def __init__(self):
        pass


class ls(file_system):
    def __init__(self):
        super().__init__()
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-ls", "--list", action="store_true")
        self.args = self.parser.parse_args()

    def run(self):
        if not file_system.current_directory.exists():
            return(f"The path {file_system.current_directory} doesn't exist")
        elif file_system.current_directory.is_file():
            return(f"{self.curr_dir} is a file")
        elif self.args.list:
            for file in file_system.current_directory.iterdir():
                print(file.name)
                
        else:
            pass

class cd(file_system):
    def __init__(self):
        super().__init__()
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-cd", "--change_dir", type=str)
        self.args = self.parser.parse_args()
    
    def run(self):
        if self.args.change_dir:
            new_path = file_system.current_directory/Path(self.args.change_dir)
            if new_path.is_file():
                print("The path is a file, not a directory")
            
            elif not new_path.exists():
                print("The path does not exist")
            
            with open('current_dir.txt', 'w') as file:
                file.write(str(new_path))
            print("The path has been changed <3")


if __name__ == "__main__":
    cmd = cd()
    result = cmd.run()

