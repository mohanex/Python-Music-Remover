from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from lib.Sound_playing import audio_playing

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


#the sound goes from -66 to 0db, with every 6db the sound doubles 
#I need to find out a way to calculate the differencian equation between db and pc volume

def main():
    while True :
        #print(volume.GetVolumeRange())
        print(audio_playing.is_playing())
        if audio_playing.is_playing():
            volume.SetMasterVolumeLevel(-65.0, None)
        else :
            volume.SetMasterVolumeLevel(0.0, None)

#volume.SetMasterVolumeLevel(-66.0, None)






# %% 

if __name__ == '__main__':
    print("Python music remover is running.\n")
    main()


# %% 