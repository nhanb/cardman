from tkinter import HORIZONTAL, VERTICAL, Grid, Text, Tk, ttk

from .model import Model


class View:
    model: Model
    pw: ttk.PanedWindow

    def __init__(self, root: Tk, model: Model):
        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        # Top-level horizontal PanedWindow
        pw = ttk.PanedWindow(root, orient=HORIZONTAL)
        pw.grid(column=0, row=0, sticky="nesw")

        # Card selection
        cards_tree = ttk.Treeview(pw, show="tree")
        for card in model.cards:
            cards_tree.insert("", 0, text=card["name"])
        pw.add(cards_tree)

        # Main text editor
        text_editor = Text(pw)
        pw.add(text_editor)

        # Rightmost vertical paned window
        vpw = ttk.PanedWindow(pw, orient=VERTICAL)
        pw.add(vpw)

        ## Template picker
        templates_tree = ttk.Treeview(vpw, show="tree")
        for template in model.templates:
            templates_tree.insert("", 0, text=template)
        vpw.add(templates_tree)

        ## Preview
        preview_frame = ttk.LabelFrame(vpw, text="Preview:", height=300, width=300)
        vpw.add(preview_frame)

        # Housekeeping
        style = ttk.Style()
        style.theme_use("clam")
        self.model = model
        self.pw = pw
