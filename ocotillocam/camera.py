from basecam import BaseCamera, CameraEvent, CameraSystem, Exposure

#pll.par["devices/dlls/andor_sdk2"] = "path/to/dlls"
from pylablib.devices import Andor
import numpy as np
from typing import List


class OcotilloCamera(BaseCamera):

    def __init__(self):
        self.status = "disconnected"
        self.exposure.exptime = 10E-3 #need to set up/inherit exposure class
        self.temperature_set_point = -10
        #continually update with actual?

    async def _connect_internal(self):

        self.status = "connected"
        self.cam = Andor.AndorSDK2Camera(fan_mode="full") #assumes only one andor connected - otherwise need to index
        
        #confirm?
        self._initialize_settings

    async def _initialize_settings(self):
        self.cam.set_temperature(self.temperature_set_point)
        self.current_temperature = self.cam.get_temperature
        self.current_temperature_status = self.cam.get_temperature_status

        self.cam.set_exposure(self.exposure.exptime)


#AndorSDK2Camera.get_all_amp_modes() and AndorSDK2Camera.get_max_vsspeed(). Afterwards, you can set them using AndorSDK2Camera.set_amp_mode() and AndorSDK2Camera.set_vsspeed().

    async def _status_internal(self):
        device = self._device


        

    async def _expose_internal(self, exposure: Exposure, **kwargs) -> Exposure:
        #to do: steps for cancelling an inprogress exposure

        self.cam.set_exposure(exposure.exptime)
        img = self.cam.snap()
        exposure.data = img
        return 


    async def _disconnect_internal(self):
        self.cam.close()
        self.status = "disconnected"


class OcotilloCameraSystem(CameraSystem[OcotilloCamera]):
    camera_class = OcotilloCamera
    __version__ = '0.0.0' #todo: add versioning for either Andor SDK and/or pylablib

    def __init__(self,simulation_mode,*args,**kwargs):
        #self.camera_class: Type[OcotilloCamera] = kwargs.pop("camera_system",OcotilloCamera)
        #super().__init__(*args,**kwargs)

        self.simulation_mode = simulation_mode
        self.lib: Andor.type | None = None

    def setup(self):
        self.lib = Andor


    def list_available_cameras(self) -> List[str]:
        #if self.lib is None:
        #    return []
        Andor.get_cameras_number_SDK2()


