#** engine.py

import time
import threading

class FocusEngine:
    """Gerencia a contagem regressiva em uma thread separada."""
    
    def __init__(self):
        self.running = False
        self.paused = False
        self.remaining_seconds = 0
        self._thread = None

    def start(self, minutes, update_callback, finish_callback):
        self.remaining_seconds = int(minutes * 60)
        self.running = True
        
        # Threading evita que a UI do CustomTkinter trave
        self._thread = threading.Thread(
            target=self._run, 
            args=(update_callback, finish_callback), 
            daemon=True # Fecha a thread se o programa fechar
        )
        self._thread.start()

    def _run(self, update_cb, finish_cb):
        # Mudamos de > 0 para >= 0 para garantir que o 00:00 apareça
        while self.remaining_seconds >= 0 and self.running:
            mins, segs = divmod(self.remaining_seconds, 60)
            update_cb(f"{mins:02d}:{segs:02d}")
            time.sleep(1)
            self.remaining_seconds -= 1
        
        if self.running:
            # Força o display a mostrar 00:00 antes de terminar
            update_cb("00:00")
            finish_cb()

    def stop(self):
        self.running = False