import flet as ft
from ui.components.theme_button import build_theme_button

def build_sidebar(logger_status,page,log_viewer):
    sidebar_content = ft.Column([
        ft.Text("App Version: 1.0", color=ft.colors.WHITE),
        logger_status,
        build_theme_button(page,log_viewer)
    ], expand=False)

    sidebar = ft.Container(
        sidebar_content,
        width="20%",
        bgcolor=ft.colors.BLACK87,
        padding=10
    )

    return sidebar


