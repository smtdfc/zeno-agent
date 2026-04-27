from nicegui import ui


def chat_message(message: str, role: str = "user") -> None:
    align = 'justify-end' if role == "user" else 'justify-start'
    color = 'bg-teal-500 text-white' if role == "user" else 'bg-white text-black shadow-sm'

    with ui.row().classes(f'w-full {align}'):
        ui.label(message).classes(
            f'{color} p-3 rounded-2xl max-w-[70%] whitespace-pre-wrap break-words block'
        )


def content():
    ui.add_css('''
    .nicegui-sub-pages {
        align-items: stretch;
        width: 100%;
    }
    ''')

    with ui.column().classes(' items-center no-wrap shadow-none  box-border'):

        scroll = ui.scroll_area().classes('w-[90%] max-w-[900px]  h-[60vh] box-border')

        with scroll:
            history_container = ui.column().classes(
                'w-full gap-4 box-border '
            )
            bottom = ui.element('div')


        async def send_message():
            text = message_input.value.strip()
            if not text:
                return

            with history_container:
                chat_message(message_input.value, role="user")

            message_input.value = ''

            await ui.run_javascript(
                'setTimeout(() => { window.scrollTo(0, document.body.scrollHeight); }, 50)'
            )
            # ui.timer(0.01, lambda: scroll.scroll_to(percent=1.0))

            await bottom.run_method('scrollIntoView', {'behavior': 'smooth'})
        with ui.element("div").classes('''
                fixed bottom-5 z-50 rounded-3xl
                w-[90%] max-w-[900px] mx-auto left-0 right-0 
                bg-teal-50 shadow-2xl border border-teal-200 p-4
            '''):

            message_input = ui.textarea(
                placeholder="Ask Agent ..."
            ).props("borderless autogrow")\
             .classes("resize-none ring-0 flex-grow text-base overflow-y-auto min-h-[100px] max-h-[30vh]")

            with ui.row().classes("w-full items-end p-2 justify-between"):
                ui.button(icon='attach_file').props("flat round dense")

                ui.button(icon='send', on_click=send_message)\
                    .props("flat round dense")

        # enter để gửi
        message_input.on('keydown.enter', send_message)