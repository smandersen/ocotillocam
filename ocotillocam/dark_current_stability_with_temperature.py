from pylablib.devices import Andor
import numpy as np
import math

n_cam = Andor.get_cameras_number_SDK2() #hardware check - if fails, no cameras connected
SDK_ver = Andor.get_SDK2_version() #sw level check - if fails, SDK2 not installed or cannot find

mycam = Andor.AndorSDK2Camera(fan_mode="full") #temp doesn't always work on init
mycam.set_temperature(-10)
mycam.set_cooler()
n_pixels = math.prod(mycam.get_data_dimensions())
pre_amp_gain = mycam.get_preamp_gain()


default_base_mean_level = 2859
default_ccd_sensitivity = 6.10

#loop - set temp, and wait
mycam.get_temperature_setpoint()
mycam.get_temperature()
mycam.get_temperature_status()
#some clever status message

#take exposure
mycam.setup_image_mode()
mycam.set_acquisition_mode('single')
mycam.set_exposure(0)#bias!
mycam.setup_shutter('closed') #closed for darks


#mycam.setup_acquisition(nframes=1,mode='single')

#mycam.is_acquisition_setup() #check ready to go
mycam.start_acquisition()
mycam.acquisition_in_progress() #would need to wait - maybe need to use for async?
#mycam.get_readout_time()
mycam.get_status()

mycam.stop_acquisition()
data_out,info = mycam._read_frames([0,1],return_info=True)
print(data_out)
#remove read noise!
read_noise = np.mean(data_out[0])


exposure_time = 10
mycam.set_exposure(exposure_time)

mycam.start_acquisition()
mycam.acquisition_in_progress() #would need to wait - maybe need to use for async?
#mycam.get_readout_time()
mycam.get_status()

mycam.stop_acquisition()
data_out,info = mycam._read_frames([0,1],return_info=True)
dark_current = data_out[0]- read_noise
np.sum(dark_current*6.1/10)/n_pixels #this is close -- finish troubleshooting








