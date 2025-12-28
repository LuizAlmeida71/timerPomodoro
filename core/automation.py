import webbrowser 
import pyautogui
import time 

class MediaController:
    # Rsponsável por interagir com o sistema operacional e navegador.

    @staticmethod 
    def play_youtube(url='https://music.youtube.com/watch?v=4q3khHysVpM&list=LM'): 
        # Abre o nevegador apenas se já não estiver aberto.
        webbrowser.open(url=url)
        # Delay para garantir que a página carregou antes do comando de mídia.
        time.sleep(5)
        pyautogui.press('playpause') 

    @staticmethod
    def stop_media():
        # Envia o sinal de pausa universal do Windows/MacOs/Linux.
        pyautogui.press('playpause')

    # @staticmethod
    # def beep():
    #     # Emite um sinal sonoro do sistema para alertar o fim do intervalo.
    #     import winsound # Apensar para Windows
    #     winsound.Beep(1000,500)

# 🔽 Aqui você chama os métodos para rodar de verdade
if __name__ == "__main__":
    MediaController.play_youtube() 
    time.sleep(10) # espera 10 segundos
    MediaController.stop_media()
    #MediaController.beep()