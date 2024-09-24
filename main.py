import flet as ft
import os
from ui.components.sidebar import build_sidebar
from ui.components.log_viewer import build_log_viewer
from ui.components.control_buttons import build_control_buttons
from logging_handler.handler import setup_logger, simulate_logging
import threading
from flask import Flask, request, jsonify
import requests

# Inicializa o Flask
flask_app = Flask(__name__)

# Variável global para armazenar a referência do log_viewer
log_viewer_reference = None
logs = []  # Lista para armazenar os logs

@flask_app.route('/')
def index():
    return "Servidor Flask está funcionando! Acesse /log para enviar logs."

API_URL = "http://127.0.0.1:5001/logs"

@flask_app.route('/log', methods=['POST'])
def receive_log():
    data = request.json
    flask_app.logger.info(f"Dados recebidos: {data}")
    log_message = data.get('message')
    if log_message and log_viewer_reference:
        log_viewer_reference.value += f"\n{log_message}"  # Adiciona o log na interface
        logs.append(log_message)  # Armazena o log na lista
        return {"status": "success"}, 200
    if not log_viewer_reference:
        flask_app.logger.error("log_viewer_reference não está inicializado.")
        return {"status": "error"}, 400

@flask_app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs), 200  # Retorna os logs como JSON

def start_flask_server():
    flask_app.run(port=5001)

def main(page: ft.Page):
    global log_viewer_reference  # Tornar a referência global
    page.title = "Log Viewer"
    page.theme_mode = ft.ThemeMode.DARK

    logger_status = ft.Row([
        ft.Text("Logger Status: ", size=16, color=ft.colors.WHITE),
        ft.Text("Stopped", size=16, color=ft.colors.RED)
    ])
    
    log_viewer_reference = build_log_viewer(page.theme_mode)  # Atribui a referência
    sidebar = build_sidebar(logger_status, page, log_viewer_reference)
    
    logger = setup_logger(log_viewer_reference, page)
    stop_event = threading.Event()

    def start_logging(e):
        logger_status.controls[1].value = "Running"
        logger_status.controls[1].color = ft.colors.GREEN
        stop_event.clear()
        thread = threading.Thread(target=simulate_logging, args=(logger, stop_event))
        thread.start()
        page.update()

    def stop_logging(e):
        logger_status.controls[1].value = "Stopped"
        logger_status.controls[1].color = ft.colors.RED
        stop_event.set()
        page.update()

    control_buttons = build_control_buttons(start_logging, stop_logging)
    
    def update_layout():
        
        print(f"Current window width: {page.window_width}")  # Para depuração
            
        if page.window_width < 600:
            # Sidebar em cima se a largura for menor que 600
            main_content = ft.Column([
                sidebar,  # Sidebar em cima
                control_buttons,
                log_viewer_reference
            ], expand=True)
        else:
            # Sidebar ao lado se a largura for maior ou igual a 600
            main_content = ft.Row([
                sidebar,
                ft.Column([
                    control_buttons,
                    log_viewer_reference
                ], expand=True)
            ], expand=True)

        page.clean()  
        page.add(main_content)  
        page.update()  


    update_layout()
    page.on_resize = lambda _: update_layout()

# Inicia o servidor Flask em uma thread
flask_thread = threading.Thread(target=start_flask_server, daemon=True)
flask_thread.start()
# Início do aplicativo Flet
if __name__ == "__main__":
    ft.app(target=main)
    # ft.app(target=main, view=ft.AppView.WEB_BROWSER)

"""Enviar logs"""
# curl -X POST http://127.0.0.1:5001/log -H "Content-Type: application/json" -d '{"message": "Log de teste recebido 1"}'

"""Buscar logs"""
# curl http://127.0.0.1:5001/logs 

