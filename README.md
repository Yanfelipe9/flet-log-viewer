# Log Viewer

## Descrição

O Log Viewer é uma aplicação que permite visualizar logs em tempo real com uma interface interativa. A aplicação utiliza Flask para gerenciar a API e Flet para a interface do usuário, proporcionando uma experiência de visualização de logs simples e eficiente.

## Funcionalidades

- Visualização de logs em tempo real.
- Controle do status do logger (iniciar/parar).
- Responsividade para diferentes tamanhos de tela.
- Interface intuitiva e fácil de usar.

## Tecnologias Utilizadas

- **Frontend:** Flet
- **Backend:** Flask

## Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes do Python)

## Siga as etapas abaixo para configurar e executar o projeto em sua máquina local.

1. **Clone o Repositório**:
      ```
   git clone https://github.com/Yanfelipe9/flet-log-viewer.git
   cd flet-log-viewer
     ```
2. **Crie um ambiente virtual:**:
  ```
  python -m venv venv
  ```
3. **Ative o ambiente virtual:**:
  No Windows (Git Bash)
  ```
  source venv/Scripts/activate
  ```
  No Windows (cmd)
  ```
  venv\Scripts\activate
  ```
  PowerShell
  ```
  .\venv\Scripts\Activate.ps1
  ```
4. **Instale as dependências:**:
  ```
  pip install -r requirements.txt
  ``` 
5. **Execute a aplicação:**:
  ```
  python main.py
  ``` 
6. **Acesse a aplicação: Abra seu navegador e vá para http://127.0.0.1:5001 para visualizar a interface do Log Viewer.**

## Enviando e Obtendo Logs

**Para enviar logs, você pode usar um comando curl (Acesse http://127.0.0.1:5001/logs) para vizualizar os logs enviados por esse comando**
  ```
  curl -X POST http://127.0.0.1:5001/log -H "Content-Type: application/json" -d '{"message": "Log de teste recebido 1"}'

  ```

**Para buscar logs, use:**
  ```
  curl http://127.0.0.1:5001/logs
  ``` 
## Executável

Baixe o executácel por aqui [Link](https://github.com/Yanfelipe9/flet-log-viewer/releases/download/v1.0/main.exe)
