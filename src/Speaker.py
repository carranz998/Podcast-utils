import win32com.client as wincl
import winsound


class Speaker:

    def __init__(self):
        self.engine = wincl.Dispatch("SAPI.SpVoice")

    @staticmethod
    def beep(frequency, duration):
        winsound.Beep(frequency,  duration)

    def final_sound(self):
        [self.beep(432, 1000) for _ in range(3)]

    def speak(self, message):
        self.engine.Speak(message)
