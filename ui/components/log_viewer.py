import flet as ft

def build_log_viewer(theme_mode):
    # Cor do texto com base no tema
    text_color = ft.colors.BLACK if theme_mode == ft.ThemeMode.LIGHT else ft.colors.WHITE

    log_viewer = ft.TextField(
        value="Logs will appear here...",
        multiline=True,
        expand=True,
        read_only=True,
        text_style=ft.TextStyle(color=text_color),  # Define a cor do texto
    )

    return log_viewer

