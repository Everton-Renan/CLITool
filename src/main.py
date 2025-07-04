import os
from pathlib import Path
from tkinter.filedialog import askdirectory

INPUT_COLOR = '\033[32m'
ERROR_COLOR = '\033[31m'
RESET_COLOR = '\033[0m'
OUTPUT_COLOR = '\033[34m'
LANGUAGES = ["python", "php", "c"]
DEVSETUP_LANGUAGES = ["python", "php"]


class Menu:
    def create(self):
        os.system("cls")
        print("[1] - Create Project")
        print("[2] - Search Project")
        print("[3] - DevSetup")
        print("[4] - Select Path")
        print("[99] - Exit")

    def get_option(self):
        option = " "

        while option not in "1234" and option not in "99":
            option = input(f"{INPUT_COLOR}: {RESET_COLOR}")

        return option

    def select_option(self, option: str):
        if option == "1":
            create_project = CreateProject()
            create_project.create()

        elif option == "2":
            open_project = OpenProject()
            open_project.create()

        elif option == "3":
            dev_setup = DevSetup()
            dev_setup.create()


class CreateProject:
    def create(self):
        os.system("cls")

        while True:
            print("Create Project")
            print("Please provide the programming language and project name.")
            print("[99] - Exit")
            answer = input(f"{INPUT_COLOR}: {RESET_COLOR}")

            if answer == "99":
                return

            result = self.run(answer)
            os.system("cls")
            print(f"{OUTPUT_COLOR}{result}{RESET_COLOR}")

    def run(self, answer: str) -> str:
        try:
            lang = answer.split()[0].lower()
            name = answer.split()[1]
        except IndexError:
            return "Missing programming language or project name."

        if lang not in LANGUAGES:
            return "Unsupported programming language."

        path = Path().parent / f"{name}" / "src"

        if Path(path).exists():
            return "A project with this name already exists."

        if lang == "python":
            os.makedirs(path)
            with open(f"{path}/main.py", "w", encoding="utf8") as file:
                file.write("""if __name__ == "__main__":
    print("Hello World!")
""")
                file.close()
            return "Project created successfully."

        elif lang == "php":
            os.makedirs(path)
            with open(f"{path}/main.php", "w", encoding="utf8") as file:
                file.write("""<?php
echo "Hello World!";
?>""")
                file.close()
            return "Project created successfully."

        elif lang == "c":
            os.makedirs(path)
            with open(f"{path}/main.c", "w", encoding="utf8") as file:
                file.write("""#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("Hello World\\n");
}""")
                file.close()
            return "Project created successfully."

        return "An error occurred. Please restart CLITool."


class OpenProject:
    def create(self):
        os.system("cls")

        while True:
            print("Open Project")
            print("Please provide the project name.")
            print("[99] - Exit")
            answer = input(f"{INPUT_COLOR}: {RESET_COLOR}")

            if answer == "99":
                return

            result = self.run(answer)
            os.system("cls")
            print(f"{OUTPUT_COLOR}{result}{RESET_COLOR}")

    def run(self, answer: str) -> str:
        try:
            name = answer.split()[0]
        except IndexError:
            return "Missing the project name."

        path = Path().parent

        if Path(path).exists():
            os.system(f"powershell -Command cd {path.absolute()}; code {name}")
            return "Project found."
        else:
            return "Project not found."


class DevSetup():
    def create(self):
        os.system("cls")

        while True:
            print("DevSetup")
            print("Please provide the programming language.")
            print("[99] - Exit")
            answer = input(f"{INPUT_COLOR}: {RESET_COLOR}")

            if answer == "99":
                return

            result = self.run(answer)
            os.system("cls")
            print(f"{OUTPUT_COLOR}{result}{RESET_COLOR}")

    def run(self, answer: str) -> str:
        try:
            lang = answer.split()[0]
        except IndexError:
            return "Missing the programming language."

        if lang not in DEVSETUP_LANGUAGES:
            return "Unsupported programming language."

        if lang == "python":

            path = Path(__file__).parent / "requirements.txt"

            if path.exists():
                os.system(f"powershell pip install -r {path}")
                return "Packages installed successfully."
            else:
                return "No requirements.txt found."

        elif lang == "php":

            if os.system("powershell php -S localhost:8000"):
                return "Server up."
            else:
                return "PHP not found."

        return "An error occurred. Please restart CLITool."


if __name__ == "__main__":
    while True:
        menu = Menu()
        menu.create()
        option = menu.get_option()
        menu.select_option(option)

        if option == "99":
            break
