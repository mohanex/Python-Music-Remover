import time
from pycaw.pycaw import AudioUtilities



def is_audio_playing():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.State == 1:  # State == 1 means the audio session is active
            return True
    return False

while True:
    if is_audio_playing():
        print("Audio is currently playing.")
    else:
        print("No audio is playing.")
    time.sleep(1)