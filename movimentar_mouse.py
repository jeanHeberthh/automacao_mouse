import platform
import pyautogui
import time
import random
import pygetwindow as gw
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Intervalo entre as execuções (em segundos)
INTERVALO_SEGUNDOS = 120  # 2 minutos

def obter_posicao_teams():
    """Obtém a posição e dimensões da janela do Microsoft Teams."""
    try:
        janelas = gw.getWindows()  # Busca todas as janelas abertas
        for janela in janelas:
            if "Microsoft Teams" in janela.title:  # Verifica se o título contém "Microsoft Teams"
                return janela.left, janela.top, janela.width, janela.height
        return None
    except Exception as e:
        logging.error(f"Erro ao obter a posição da janela do Teams: {e}")
        return None

def evitar_bloqueio_tela():
    """Simula a pressão de uma tecla para evitar o bloqueio da tela."""
    try:
        tecla = "shift" if platform.system() == "Windows" else "ctrl"
        pyautogui.press(tecla)
        logging.info("🔄 Tecla pressionada para evitar bloqueio de tela.")
    except Exception as e:
        logging.error(f"Erro ao pressionar a tecla: {e}")

def movimentar_mouse_no_teams():
    """Move o mouse aleatoriamente dentro da janela do Teams para simular atividade."""
    while True:
        try:
            posicao = obter_posicao_teams()

            if posicao:
                x, y, largura, altura = posicao

                # Gera uma posição aleatória dentro da janela do Teams
                novo_x = random.randint(x + 10, x + largura - 10)
                novo_y = random.randint(y + 10, y + altura - 10)

                # Move o mouse para essa posição
                pyautogui.moveTo(novo_x, novo_y, duration=0.5)
                logging.info(f"🖱️ Mouse movido para ({novo_x}, {novo_y}) dentro do Teams.")

                # Simula o pressionamento de uma tecla
                evitar_bloqueio_tela()
            else:
                logging.warning("⚠️ Microsoft Teams não encontrado. O mouse não foi movido.")

            # Aguarda antes de repetir
            time.sleep(INTERVALO_SEGUNDOS)

        except Exception as e:
            logging.error(f"Erro na movimentação do mouse: {e}")
            time.sleep(10)  # Aguarda um pouco antes de tentar novamente

if __name__ == "__main__":
    logging.info("🔵 Movimentação do mouse iniciada... O Teams permanecerá online e a tela não bloqueará!")
    movimentar_mouse_no_teams()
