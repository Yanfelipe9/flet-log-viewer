import flet as ft

def build_control_buttons(start_logging, stop_logging):
    # Botão para iniciar o logging
    start_button = ft.ElevatedButton("Start Logging", on_click=start_logging)
    # Botão para parar o logging
    stop_button = ft.ElevatedButton("Stop Logging", on_click=stop_logging)
    
    # Retorna os botões em uma linha
    return ft.Row([start_button, stop_button], alignment=ft.MainAxisAlignment.CENTER)
