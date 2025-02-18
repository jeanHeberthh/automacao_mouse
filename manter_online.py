import pyautogui
import time
import random

def movimentar_mouse():
    while True:
        # Obtém a posição atual do mouse
        x, y = pyautogui.position()

        # Movimenta o mouse para uma posição ligeiramente diferente
        deslocamento_x = random.randint(-5, 5)
        deslocamento_y = random.randint(-5, 5)
        pyautogui.moveTo(x + deslocamento_x, y + deslocamento_y, duration=0.5)

        # Aguarda 5 minutos antes do próximo movimento
        time.sleep(120)

if __name__ == "__main__":
    print("Movimentação do mouse iniciada... O Teams permanecerá online 🚀")
    movimentar_mouse()
