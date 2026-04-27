from nicegui import ui, native

from ui.components.navbar import navbar
from ui.pages import home


def root():
    navbar()
    ui.sub_pages({'/': home.content})


def  init_app():
    ui.run(root,native=True, port=native.find_open_port(), title="Zeno Agent")