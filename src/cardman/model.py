from pathlib import Path

CARDS_DIR = Path("cards")
TEMPLATES_DIR = Path("templates")


class Model:
    cards = []
    templates = []
    card_content = ""

    def __init__(self):
        self.load_card_list()
        self.load_template_list()

    def load_card_list(self):
        self.cards = [p for p in CARDS_DIR.iterdir() if str(p).endswith(".card")]

    def load_template_list(self):
        self.templates = [
            p for p in TEMPLATES_DIR.iterdir() if str(p).endswith(".html")
        ]

    def load_card_content(self, path: Path):
        if not path.is_file():
            print(f"File {path} does not exist.")
            return
        with open(path, "r") as cardfile:
            self.card_content = cardfile.read()
