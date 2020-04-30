class Model:
    cards = []

    def __init__(self):
        self.cards = [
            {"name": "foo.card", "content": "foo"},
            {"name": "bar.card", "content": "bar"},
        ]
        self.templates = ["template1", "template2"]
