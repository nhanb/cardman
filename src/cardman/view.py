import sys
from pathlib import Path
from tkinter import END, HORIZONTAL, VERTICAL, Grid, Text, Tk, ttk

from cefpython3 import cefpython as cef

from .model import Model


class View:
    model: Model
    pw: ttk.PanedWindow
    cards_tree: ttk.Treeview
    templates_tree: ttk.Treeview
    text_editor: Text
    select_card_callback = None
    select_template_callback = None

    def __init__(self, root: Tk, model: Model):
        self.model = model

        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        # Horizontal PanedWindow
        pw = ttk.PanedWindow(root, orient=HORIZONTAL)
        self.pw = pw
        pw.grid(column=0, row=0, sticky="nesw")

        # Card selection
        cards_frame = ttk.LabelFrame(pw, text="Cards")
        pw.add(cards_frame)
        cards_tree = ttk.Treeview(cards_frame, show="tree", selectmode="browse")
        self.cards_tree = cards_tree
        self.render_card_list()
        cards_tree.bind("<<TreeviewSelect>>", self._on_select_card)
        cards_tree.grid(column=0, row=0, sticky="nesw")
        Grid.rowconfigure(cards_frame, 0, weight=1)
        Grid.columnconfigure(cards_frame, 0, weight=1)

        # Main text editor
        text_editor = Text(pw)
        self.text_editor = text_editor
        text_editor.bind("<Control-a>", self._on_text_ctrl_a)
        pw.add(text_editor)

        # Rightmost vertical paned window
        vpw = ttk.PanedWindow(pw, orient=VERTICAL)
        pw.add(vpw)

        ## Template picker
        templates_frame = ttk.LabelFrame(vpw, text="Templates")
        vpw.add(templates_frame)
        templates_tree = ttk.Treeview(templates_frame, show="tree")
        templates_tree.grid(column=0, row=0, sticky="nsew")
        Grid.rowconfigure(templates_frame, 0, weight=1)
        Grid.columnconfigure(templates_frame, 0, weight=1)
        self.templates_tree = templates_tree
        self.render_template_list()
        templates_tree.bind("<<TreeviewSelect>>", self._on_select_template)

        ## Preview
        preview_frame = ttk.LabelFrame(vpw, text="Preview", height=300, width=300)
        vpw.add(preview_frame)

        style = ttk.Style()
        if sys.platform == "win32":
            style.theme_use("vista")
        elif sys.platform == "darwin":
            style.theme_use("aqua")
        else:
            style.theme_use("clam")

    def render_card_list(self):
        self.cards_tree.delete(*self.cards_tree.get_children())
        for card in self.model.cards:
            self.cards_tree.insert("", "end", text=card.parts[-1], iid=card)

    def render_template_list(self):
        self.templates_tree.delete(*self.templates_tree.get_children())
        for template in self.model.templates:
            self.templates_tree.insert("", "end", text=template.parts[-1], iid=template)

    def render_card_content(self):
        self.text_editor.delete("1.0", END)
        self.text_editor.insert(END, self.model.card_content.rstrip())

    def _on_select_card(self, ev):
        if self.select_card_callback is not None:
            self.select_card_callback(Path(ev.widget.selection()[0]))

    def _on_select_template(self, ev):
        if self.select_template_callback is not None:
            self.select_template_callback(Path(ev.widget.selection()[0]))

    def _on_text_ctrl_a(self, ev):
        self.text_editor.tag_add("sel", "1.0", END)
        return "break"
