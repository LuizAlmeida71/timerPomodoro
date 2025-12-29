#** automation.py
import webbrowser 
import pyautogui
import time 
import os

class MediaController:
    # Rsponsável por interagir com o sistema operacional e navegador.

    @staticmethod 
    def play_youtube(url='https://music.youtube.com/watch?v=4q3khHysVpM&list=LM'): 
        webbrowser.open(url=url)
        # Aumentamos para 15 segundos devido ao seu tempo de carregamento
        time.sleep(15) 
        # Tenta dar o play duas vezes caso a janela não esteja em foco
        pyautogui.press('playpause')
        time.sleep(1)
        pyautogui.press('space') 

    @staticmethod
    def stop_media():
        # Envia o sinal de pausa universal do Windows/MacOs/Linux.
        pyautogui.press('playpause')

    @staticmethod
    def beep():
        # Alternativa para Linux: emite um som de sistema visual e sonoro
        os.system('notify-send "POMODORO" "Hora de voltar ao trabalho!"')
        os.system('paplay /usr/share/sounds/freedesktop/stereo/complete.oga || echo -e "\a"')

    # @staticmethod
    # def beep():
    #     # Emite um sinal sonoro do sistema para alertar o fim do intervalo.
    #     import winsound # Apensar para Windows
    #     winsound.Beep(1000,500)

