import os
from pathlib import Path
import argparse
import sys

class file_system:
    def __init__(self):
        self.curr_dir = Path(os.getcwd())


class ls(file_system):
    def __init__(self):
        super().__init__()
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-ls", "--list", action="store_true")
        self.args = self.parser.parse_args()

    def run(self):
        if not self.curr_dir.exists():
            print(f"The path {self.curr_dir} doesn't exist")
        elif self.curr_dir.is_file():
            print(f"{self.curr_dir} is a file")
        elif self.args.list:
            for file in self.curr_dir.iterdir():
                print(file.name)
                
        else:
            pass

if __name__ == "__main__":
    cmd = ls()
    result = cmd.run()

