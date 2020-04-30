from tkinter import HORIZONTAL, VERTICAL, Grid, Text, Tk, ttk

from .model import Model


class View:
    model: Model
    pw: ttk.PanedWindow
    cards_tree: ttk.Treeview

    def __init__(self, root: Tk, model: Model):
        self.model = model

        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        # Top-level horizontal PanedWindow
        pw = ttk.PanedWindow(root, orient=HORIZONTAL)
        self.pw = pw
        pw.grid(column=0, row=0, sticky="nesw")

        # Card selection
        cards_tree = ttk.Treeview(pw, show="tree", selectmode="browse")
        self.cards_tree = cards_tree
        self.render_card_list()
        cards_tree.bind("<<TreeviewSelect>>", self.on_select_card)
        pw.add(cards_tree)

        # Main text editor
        text_editor = Text(pw)
        pw.add(text_editor)

        # Rightmost vertical paned window
        vpw = ttk.PanedWindow(pw, orient=VERTICAL)
        pw.add(vpw)

        ## Template picker
        templates_tree = ttk.Treeview(vpw, show="tree")
        self.templates_tree = templates_tree
        self.render_template_list()
        cards_tree.bind("<<TreeviewSelect>>", self.on_select_template)
        vpw.add(templates_tree)

        ## Preview
        preview_frame = ttk.LabelFrame(vpw, text="Preview:", height=300, width=300)
        vpw.add(preview_frame)

        style = ttk.Style()
        style.theme_use("clam")

    def render_card_list(self):
        for card in self.model.cards:
            self.cards_tree.insert("", "end", text=card.parts[-1], iid=card)

    def render_template_list(self):
        for template in self.model.templates:
            self.templates_tree.insert("", "end", text=template.parts[-1], iid=template)

    def on_select_card(self, ev):
        print("selection is", ev.widget.selection())

    def on_select_template(self, ev):
        print("selection is", ev.widget.selection())
