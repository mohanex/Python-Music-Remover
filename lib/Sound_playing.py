import time
from pycaw.pycaw import AudioUtilities


class audio_playing :
    def is_playing():
        #cleawhile True :
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.State == 1:  # State == 1 means the audio session is active
                print("Audio is currently playing.")
                return True
        print("No audio is playing.")
        return False

"""
    while True:
        if is_playing():
            print("Audio is currently playing.")
        else:
            print("No audio is playing.")
        time.sleep(1)"""