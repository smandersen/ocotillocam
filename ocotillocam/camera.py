from basecam import BaseCamera, CameraEvent, CameraSystem, Exposure

#pll.par["devices/dlls/andor_sdk2"] = "path/to/dlls"
from pylablib.devices import Andor
import numpy as np


class OcotilloCamera(BaseCamera):

    def __init__(self):
        self.status = "disconnected"
        self.exposure = 10E-3

    def _connect_internal(self):

        self.status = "connected"
        self.cam = Andor.AndorSDK2Camera() #assumes only one andor connected

#AndorSDK2Camera.get_all_amp_modes() and AndorSDK2Camera.get_max_vsspeed(). Afterwards, you can set them using AndorSDK2Camera.set_amp_mode() and AndorSDK2Camera.set_vsspeed().

    def _status_internal():

    def _expose_interal(self):
        img = cam.snap()
        return img


    def _disconnect_internal(self):
        self.cam.close()
        self.status = "disconnected"


class OcotilloCameraSystem(CameraSystem[OcotilloCamera]):
    camera_class = OcotilloCamera
    self.__version__ = '0'

    def __init__(self,*args,**kwargs):

    def setup(self):
        self.lib = 

    def list_available_camears(self) -> LIst[str]:
        if self.lib is None:
            return []
        Andor.get_cameras_number_SDK2()


