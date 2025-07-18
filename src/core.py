import os
import subprocess
import webbrowser
from pathlib import Path
from tkinter.filedialog import askdirectory, askopenfilename

import requests

from settings import (DEVSETUP_LANGUAGES, ERROR_COLOR, GITHUB_TOKEN,
                      INPUT_COLOR, LANGUAGES, OUTPUT_COLOR, RESET_COLOR)

path = ""


class Menu:
    def create(self, result: str | None):
        subprocess.run(["cls"], shell=True, check=True)
        if result != '' and result is not None:
            print(f"{ERROR_COLOR}{result}{RESET_COLOR}")
        print("[1] - Create Project")
        print("[2] - Search Project")
        print("[3] - DevSetup")
        print("[4] - Select Path")
        print("[5] - GitStatus")
        print("[6] - DocSearch")
        print("[7] - APITester")
        print("[99] - Exit")

    def get_option(self):
        option = " "

        while option not in "1234567" and option not in "99":
            option = input(f"{INPUT_COLOR}{path}: {RESET_COLOR}")

        return option

    def select_option(self, option: str):
        result = ""

        if option == "1":
            create_project = CreateProject()
            result = create_project.create()

        elif option == "2":
            open_project = OpenProject()
            result = open_project.create()

        elif option == "3":
            dev_setup = DevSetup()
            result = dev_setup.create()

        elif option == "4":
            global path
            path = askdirectory()

        elif option == "5":
            gitstatus = GitStatus()
            gitstatus.create()

        elif option == "6":
            doc_search = DocSearch()
            doc_search.create()

        elif option == "7":
            api_tester = APITester()
            api_tester.create()

        return result


class CreateProject:
    def create(self):
        subprocess.run(["cls"], shell=True, check=True)

        if path == "":
            return "Please, select a valid path."

        while True:
            print("Create Project")
            print("Please provide the programming language and project name.")
            print("[99] - Exit")
            answer = input(f"{INPUT_COLOR}{path}: {RESET_COLOR}")

            if answer == "99":
                return

            result = self.run(answer, path)
            subprocess.run(["cls"], shell=True, check=True)
            print(f"{OUTPUT_COLOR}{result}{RESET_COLOR}")

    def run(self, answer: str, path: str) -> str:
        try:
            lang = answer.split()[0].lower()
            name = answer.split()[1]
        except IndexError:
            return "Missing programming language or project name."

        if lang not in LANGUAGES:
            return "Unsupported programming language."

        path += fr"\{name}\src"

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
        subprocess.run(["cls"], shell=True, check=True)

        if path == "":
            return "Please, select a valid path."

        while True:
            print("Open Project")
            print("Please provide the project name.")
            print("[99] - Exit")
            answer = input(f"{INPUT_COLOR}{path}: {RESET_COLOR}")

            if answer == "99":
                return

            result = self.run(answer, path)
            subprocess.run(["cls"], shell=True, check=True)
            print(f"{OUTPUT_COLOR}{result}{RESET_COLOR}")

    def run(self, answer: str, path: str) -> str:
        try:
            name = answer.split()[0]
        except IndexError:
            return "Missing the project name."

        project_path = Path(path + f"\\{name}")

        if project_path.exists():
            subprocess.run(["powershell.exe", "-Command",
                           f"code {project_path}"], shell=False, check=True)
            return "Project found."
        else:
            return "Project not found."


class DevSetup():
    def create(self):
        subprocess.run(["cls"], shell=True, check=True)

        if path == "":
            return "Please, select a valid path."

        while True:
            print("DevSetup")
            print("Please provide the programming language.")
            print("[99] - Exit")
            answer = input(f"{INPUT_COLOR}{path}: {RESET_COLOR}")

            if answer == "99":
                return

            result = self.run(answer, path)
            subprocess.run(["cls"], shell=True, check=True)
            print(f"{OUTPUT_COLOR}{result}{RESET_COLOR}")

    def run(self, answer: str, path: str) -> str:
        try:
            lang = answer.split()[0]
        except IndexError:
            return "Missing the programming language."

        if lang not in DEVSETUP_LANGUAGES:
            return "Unsupported programming language."

        if lang == "python":

            requirements_path = Path(path) / "requirements.txt"
            venv = Path(path) / "venv"
            pip = Path(path) / "venv" / "Scripts" / "pip.exe"

            if requirements_path.exists():
                subprocess.run(["python", "-m", "venv", venv])
                subprocess.run(
                    [f"{pip}", "install", "-r", requirements_path], check=True)

                return "Packages installed successfully."
            else:
                return "No requirements.txt found."

        elif lang == "php":

            try:
                if os.system("powershell php -S localhost:8000") == 0:
                    return "Server up."
                else:
                    return "PHP not found."
            except KeyboardInterrupt:
                return "Server down."

        return "An error occurred. Please restart CLITool."


class GitStatus():
    def create(self):
        subprocess.run(["cls"], shell=True, check=True)

        while True:
            print("GitHub Status")
            print("Please provide the username.")
            print("[99] - Exit")
            answer = input(f"{INPUT_COLOR}: {RESET_COLOR}")

            if answer == "99":
                return

            result = self.run(answer)
            subprocess.run(["cls"], shell=True, check=True)

            if not isinstance(result, str):
                print(f"{OUTPUT_COLOR}Name: {str(result['name'])}\n"
                      f"Followers: {str(result['followers'])}\n"
                      f"Public Repositories: {str(result['public_repositories'])}\n"
                      f"Private Repositories: {str(result['private_repositories'])}{RESET_COLOR}")
            else:
                print(f"{result}")

    def run(self, answer: str):
        try:
            username = answer.split()[0]
        except IndexError:
            return "Missing the username."

        github_client = GitHubClient()
        response = github_client.get_user(username)

        if isinstance(response, str):
            return response
        else:
            try:
                private_repositories = str(response["total_private_repos"])
            except KeyError:
                private_repositories = "None"

            user = {
                "name": str(response["name"]),
                "followers": str(response["followers"]),
                "public_repositories": str(response["public_repos"]),
                "private_repositories": private_repositories
            }

            return user


class GitHubClient():
    def __init__(self):
        self.token = GITHUB_TOKEN
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28"
        }

    def get_user(self, username: str):
        if not self.token:
            return "Error: GITHUB_TOKEN is missing. Make sure it is set in your .env file."

        try:
            response = requests.get(f"https://api.github.com/users/{username}",
                                    headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            return error

        except requests.exceptions.ConnectionError as error:
            return error

        return response.json()


class DocSearch():
    def create(self):
        subprocess.run(["cls"], shell=True, check=True)

        while True:
            print("DocSearch")
            print("Please provide the programming language and the term.")
            print("The term does not need to be sent to the C language.")
            print("[99] - Exit")
            answer = input(f"{INPUT_COLOR}: {RESET_COLOR}")

            if answer == "99":
                return

            result = self.run(answer)
            subprocess.run(["cls"], shell=True, check=True)
            print(f"{OUTPUT_COLOR}{result}{RESET_COLOR}")

    def run(self, answer: str):
        try:
            lang = answer.split()[0].lower()
            if not lang == "c":
                term = answer.split()[1].lower()
        except IndexError:
            return "Missing programming language or term."

        if lang not in LANGUAGES:
            return "Unsupported programming language."

        if lang == "python":
            webbrowser.open(
                f"https://docs.python.org/3/search.html?q={term}")
            return "Browser started."
        elif lang == "php":
            webbrowser.open(
                f"https://www.php.net/search.php#gsc.q={term}")
            return "Browser started."
        elif lang == "c":
            webbrowser.open("https://devdocs.io/c/")
            return "Browser started."


class APITester():
    def create(self):
        subprocess.run(["cls"], shell=True, check=True)

        while True:
            print("APITester")
            print("Please, select the api file.")
            print("[1] - Select File")
            print("[99] - Exit")

            answer = input(f"{INPUT_COLOR}: {RESET_COLOR}")

            if answer == "99":
                return

            if answer != "1":
                subprocess.run(["cls"], shell=True, check=True)
                continue

            file_path = Path(askopenfilename())
            result = self.run(file_path)
            subprocess.run(["cls"], shell=True, check=True)
            if isinstance(result, dict):
                self.beautiful_print(result)
            else:
                print(f"{OUTPUT_COLOR}{result}{RESET_COLOR}")

    def run(self, file_path: Path):
        if not file_path.exists():
            return "Please, select a valid API file."

        with file_path.open("r", encoding="utf8") as file:
            file_content = file.readlines()
            headers = dict()
            url = ""

            for line in file_content:
                line = line.strip()
                if line.startswith("-h "):
                    try:
                        split_line = line.split(": ", 1)
                        key = split_line[0]
                        key = key[3:]
                        value = split_line[1]
                        headers[key] = value
                    except IndexError:
                        return f"Invalid header format: {line}."

                elif line.startswith("https"):
                    url = line.strip()

        if not url:
            return "Missing the URL."

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            return error

        except requests.exceptions.ConnectionError as error:
            return error

        except Exception as error:
            return error

        try:
            return response.json()
        except ValueError:
            return response.text

    def beautiful_print(self, obj: dict):
        for k, v in obj.items():
            print(f"{OUTPUT_COLOR}{k}: {v}{RESET_COLOR}")
