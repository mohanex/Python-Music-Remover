import pyaudio
import time


def is_audio_playing():
    audio = pyaudio.PyAudio()
    for i in range(audio.get_device_count()):
        device_info = audio.get_device_info_by_index(i)
        if device_info.get('maxInputChannels') > 0 or device_info.get('maxOutputChannels') > 0:
            return True
    return False


while True:
    time.sleep(0.5)
    if is_audio_playing():
        print("Audio is playing.")
    else:
        print("No audio playing.")
