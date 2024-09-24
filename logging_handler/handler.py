import random
import logging
import time
from flet import TextField, Page
from datetime import datetime
from app_utils.utils import format_date

# Classe personalizada de manipulador de logs que envia as mensagens para a UI
class UILogHandler(logging.Handler):
    def __init__(self, log_viewer: TextField, page: Page):
        super().__init__()
        self.log_viewer = log_viewer  # Área de visualização dos logs
        self.page = page  # Página para atualizar a UI

    def emit(self, record):
        # Usar a função format_date para substituir o asctime pelo formato desejado
        record.asctime = format_date(datetime.now())
        log_entry = self.format(record)  # Formatar a mensagem de log
        timestamp = format_date(datetime.now())  # Usando função utilitária para formatação
        self.log_viewer.value += f"\n{timestamp} {log_entry}" 
        self.page.update()  # Atualiza a UI
        
    def add_log(self, log_message):
        self.log_viewer.value += f"\n{format_date(datetime.now())} {log_message}"
        self.page.update()

def setup_logger(log_viewer: TextField, page: Page):
    """Configura o logger para enviar logs para a interface do usuário."""
    logger = logging.getLogger("AppLogger")
    logger.setLevel(logging.INFO)  # Define o nível de log como INFO

    # Criar o manipulador de logs personalizado que envia logs para a UI
    ui_handler = UILogHandler(log_viewer, page)

    # O Formatter já adiciona a data e o horário do log automaticamente
    formatter = logging.Formatter('- %(levelname)s - %(message)s')
    ui_handler.setFormatter(formatter)  # Define o formato da mensagem de log

    logger.addHandler(ui_handler)  # Adiciona o manipulador ao logger
    return logger

def generate_bet_log():
    """Gera uma mensagem de log para uma transação simulada de aposta."""
    bet_types = ["Aposta simples", "Aposta combinada", "Aposta ao vivo"]
    outcomes = ["Ganhou", "Perdeu", "Cancelada"]

    # Simular um log de uma transação de aposta esportiva
    user_id = random.randint(1000, 9999)  
    bet_type = random.choice(bet_types) 
    outcome = random.choice(outcomes)  
    bet_amount = round(random.uniform(10, 500), 2)  

    # Retorna a mensagem de log formatada
    return f"Usuário {user_id} fez uma {bet_type} de R${bet_amount}. Resultado: {outcome}."

def generate_warning_log():
    user_id = random.randint(1000, 9999)
    return f"Aviso: Usuário {user_id} tentou fazer uma aposta inválida."

def generate_error_log():
    user_id = random.randint(1000, 9999)
    return f"Erro: A aposta do usuário {user_id} não pôde ser processada."

def generate_critical_log():
    return "Crítico: O sistema de apostas está fora do ar!"

def simulate_logging(logger, stop_event):
    """Simula a geração de logs de forma contínua, até que o evento de parada seja acionado."""
    while not stop_event.is_set():  
        # log_message = generate_bet_log() 
        # logger.info(log_message)  
        level = random.choice(['info', 'warning', 'error', 'critical'])
        
        if level == 'info':
            log_message = generate_bet_log()  
            logger.info(log_message)  
        elif level == 'warning':
            log_message = generate_warning_log()  
            logger.warning(log_message)  
        elif level == 'error':
            log_message = generate_error_log()  
            logger.error(log_message) 
        elif level == 'critical':
            log_message = generate_critical_log()  
            logger.critical(log_message)  
            
        time.sleep(1)  
