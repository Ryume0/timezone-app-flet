import flet as ft


class TimePanel(ft.Container):
    def __init__(self, bgcolor: str, content: ft.Control):
        super().__init__(
            bgcolor=bgcolor,
            content=content,
            alignment=ft.Alignment.CENTER,
            expand=True,
            border_radius=10,
        )


class TimeDisplay(ft.Card):
    def __init__(self, val: str):
        super().__init__(content=ft.Text(val), bgcolor=ft.Colors.GREY_400)

    def time_update(self, val: str):
        self.content = ft.Text(val)
