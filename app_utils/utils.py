from datetime import datetime

# Função para formatar uma data em uma string legível
def format_date(date: datetime) -> str:
    return date.strftime("%d/%m/%Y %H:%M:%S")


