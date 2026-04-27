from nicegui import ui


def navbar():
    with ui.header().classes("bg-white text-black shadow-md items-center justify-between px-8 py-3"):
        with ui.row().classes("items-center gap-2 p-2 justify-between"):
            ui.button(icon='menu').props("flat round dense")
            ui.label("Zeno Agent").classes("text-xl tracking-tight font-bold")

        with ui.row().classes("items-center gap-2 p-2 justify-between"):
            ui.button(icon='notifications').props("flat round dense")
            ui.button(icon='settings').props("flat round dense")
            ui.button(icon='add').props("flat round dense")
