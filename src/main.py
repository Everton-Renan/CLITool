
import argparse
from pathlib import Path
import os
import sys
from tkinter.filedialog import askdirectory

INPUT_COLOR = '\033[32m'
ERROR_COLOR = '\033[31m'
RESET_COLOR = '\033[0m'
OUTPUT_COLOR = '\033[34m'

class Menu:
    def create(self):
        print("[1] - Create Project")
        print("[2] - Search Project")
        print("[3] - Status")
        print("[4] - DevSetup")
        print("[99] - Exit")

    def get_option(self):
        option = " "

        while option not in "1234" and option not in "99":
            option = input(": ")

        return option

class CreateProject:
   def __init__(self, lang, name):
        self.lang = lang
        self.name = name

   def create(self):
        if self.lang == "python":
            path = Path().parent / f"{self.name}" / "src"
            os.makedirs(path)



if __name__ == "__main__":
    while True:
        menu = Menu()
        menu.create()
        option = menu.get_option()

        create_project = CreateProject("python", "CLITool")
        create_project.create()

        if option == "99":
            break
        print("Option: ", option)