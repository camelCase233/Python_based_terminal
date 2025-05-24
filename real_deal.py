import os
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
            if self.args.change_dir == "..":
                if str(Path.home()) == content:
                    print("Can't go beyond home dir")
                    return
                prev_dir = os.path.dirname(self.current_directory)
                with open('current_dir.txt', 'w') as file:
                    file.write(prev_dir)
                return
            new_path = file_system.current_directory/Path(self.args.change_dir)
            if new_path.is_file():
                print("The path is a file, not a directory")
                return
            
            elif not new_path.exists():
                print("The path does not exist")
                return
            
            with open('current_dir.txt', 'w') as file:
                file.write(str(new_path))
            print("The path has been changed <3")

class mkdir(file_system):
    def __init__(self):
        super().__init__()
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-mkdir", "--make_directory", type=str)
        self.args = self.parser.parse_args()
    
    def run(self):
        if self.args.make_directory:
            new_dir = file_system.current_directory/Path(self.args.make_directory)
            if new_dir.exists():
                print("This directory already exists")
                return
            new_dir.mkdir(parents=True, exist_ok=True)
            print("The directory has been made")

if __name__ == "__main__":
    cmd = cd()
    cmd.run()
