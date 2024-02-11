from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


#the sound goes from -66 to 0db, with every 6db the sound doubles 
#I need to find out a way to calculate the differencian equation between db and pc volume
volume.SetMasterVolumeLevel(-38.0, None)
