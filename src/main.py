from datetime import time

import flet as ft

from components import TimeDisplay, TimePanel


def main(page: ft.Page):
    page.title = "Timezone app"

    time_picker = ft.TimePicker(
        # hour_format=ft.TimePickerHourFormat.H24,
        value=time(hour=12, minute=00),
        on_change=lambda e: time_text.time_update(str(time_picker.value)),
    )
    inp = ft.Button(
        "Input time",
        on_click=lambda: page.show_dialog(time_picker),
    )
    time_text = TimeDisplay("12:00")
    left_col = ft.Column(
        controls=[inp, time_text],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    left_cont = TimePanel(ft.Colors.GREY_300, left_col)
    right_cont = TimePanel(ft.Colors.GREY_500, ft.Text("tescik"))
    page.add(
        ft.Container(
            content=ft.Row(controls=[left_cont, right_cont]),
            alignment=ft.Alignment.CENTER,
            expand=True,
            padding=100,
        )
    )


if __name__ == "__main__":
    ft.run(main)
