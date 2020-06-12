import sounddevice as sd
import numpy as np
from pynput.keyboard import Key, Controller


keyboard = Controller()
def detect_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    if int(volume_norm) > 15:
        keyboard.press(Key.f6)
    elif int(volume_norm) < 4:
        keyboard.release(Key.f6)

voice = sd.Stream(callback=detect_sound)
voice.start()