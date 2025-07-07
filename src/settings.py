import os

from dotenv import load_dotenv

load_dotenv()

INPUT_COLOR = '\033[32m'
ERROR_COLOR = '\033[31m'
RESET_COLOR = '\033[0m'
OUTPUT_COLOR = '\033[34m'
LANGUAGES = ["python", "php", "c"]
DEVSETUP_LANGUAGES = ["python", "php"]
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
