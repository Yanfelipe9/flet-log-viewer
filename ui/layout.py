import flet as ft
from ui.components.sidebar import build_sidebar
from ui.components.control_buttons import build_control_buttons
from logging_handler.handler import setup_logger, simulate_logging
import threading

def build_ui(page):
    page.title = "Log Viewer"
    page.theme_mode = ft.ThemeMode.DARK

    logger_status = ft.Text("Logger Status: Stopped", size=16, color=ft.colors.WHITE)

    log_viewer = ft.TextField(
        value="Logs will appear here...",
        multiline=True,
        expand=True,
        read_only=True,
        text_style=ft.TextStyle(color=ft.colors.WHITE),
    )

    # Funções de logging
    stop_event = threading.Event()

    def start_logging(e):
        logger_status.value = "Logger Status: Running"
        logger_status.color = ft.colors.GREEN
        stop_event.clear()
        # Iniciar simulação de logging aqui...

        page.update()

    def stop_logging(e):
        logger_status.value = "Logger Status: Stopped"
        logger_status.color = ft.colors.RED
        stop_event.set()
        page.update()

    control_buttons = build_control_buttons(start_logging, stop_logging)

    # Construindo a barra lateral
    sidebar = build_sidebar(logger_status, page, log_viewer)

    # Layout principal
    main_content = ft.Column([
        control_buttons,
        log_viewer
    ], expand=True)

    # Adicionando tudo ao layout
    page.add(ft.Row([
        sidebar,
        main_content
    ]))

    return log_viewer, logger_status, control_buttons
