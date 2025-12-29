#** app.py

import customtkinter as ctk
import sys
import os

# Ajuste para o executável encontrar a pasta core
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

from core.engine import FocusEngine
from core.automation import MediaController

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("MyPomodoro")
        self.geometry("450x600")
        ctk.set_appearance_mode("dark")

        self.engine = FocusEngine()
        self.is_break = False
        self._setup_ui()

    def _setup_ui(self):
        self.label_status = ctk.CTkLabel(self, text="Configure sua sessão", font=("Roboto", 20))
        self.label_status.pack(pady=20)

        self.frame_config = ctk.CTkFrame(self)
        self.frame_config.pack(pady=10, padx=20, fill="x")

        # --- CORREÇÃO AQUI: Slider de Tempo de Estudo ---
        self.label_info_foco = ctk.CTkLabel(self.frame_config, text="Tempo de Estudo: 20 min")
        self.label_info_foco.pack()
        
        # Cria um slider de 5 a 60 minutos
        self.slider_foco = ctk.CTkSlider(self.frame_config, from_=5, to=60, number_of_steps=11, command=self.update_foco_label)
        self.slider_foco.set(20) # Valor inicial
        self.slider_foco.pack(pady=10)

        # --- Slider de Intervalo ---
        self.label_info_pausa = ctk.CTkLabel(self.frame_config, text="Intervalo: 5 min")
        self.label_info_pausa.pack()
        
        self.slider_pausa = ctk.CTkSlider(self.frame_config, from_=1, to=20, number_of_steps=19, command=self.update_pausa_label)
        self.slider_pausa.set(5)
        self.slider_pausa.pack(pady=10)

        # Mostrador do Timer
        self.label_timer = ctk.CTkLabel(self, text="20:00", font=("Roboto", 80, "bold"))
        self.label_timer.pack(pady=30)

        self.btn_action = ctk.CTkButton(self, text="INICIAR JORNADA", height=50, command=self.toggle_session)
        self.btn_action.pack(pady=20)

    # --- LÓGICA QUE CORRIGE O VALOR ESTÁTICO ---
    def update_foco_label(self, value):
        mins = int(value)
        self.label_info_foco.configure(text=f"Tempo de Estudo: {mins} min")
        # Se o timer não estiver rodando, atualiza o mostrador grande também
        if not self.engine.running:
            self.label_timer.configure(text=f"{mins:02d}:00")

    def update_pausa_label(self, value):
        self.label_info_pausa.configure(text=f"Intervalo: {int(value)} min")

    def update_display(self, time_str):
        self.label_timer.configure(text=time_str)

    def toggle_session(self):
        self.is_break = False
        self.label_status.configure(text="FOCO ATIVO", text_color="#1f538d")
        self.btn_action.configure(state="disabled")
        
        # Pega o valor que você escolheu no slider
        tempo = int(self.slider_foco.get()) 
        
        # Manda esse valor para o motor iniciar
        self.engine.start(tempo, self.update_display, self.on_focus_end)

    def on_focus_end(self):
        self.is_break = True
        self.label_status.configure(text="HORA DO DESCANSO", text_color="#2eb872")
        MediaController.play_youtube()
        
        # Pega o valor do slider de pausa
        pausa_mins = int(self.slider_pausa.get())
        self.engine.start(pausa_mins, self.update_display, self.on_break_end)

    def on_break_end(self):
        MediaController.stop_media()
        MediaController.beep()
        self.label_status.configure(text="SESSÃO FINALIZADA", text_color="#e63946")
        self.btn_action.configure(state="normal", text="RECOMEÇAR")

if __name__ == "__main__":
    app = App()
    app.mainloop()