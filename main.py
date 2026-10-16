import flet as ft


def main(page: ft.Page):
    test = ft.Text("Test", size=50, data=123)

    page.add(ft.Container(content=test, alignment=ft.Alignment.CENTER, expand=True))


ft.run(main)
