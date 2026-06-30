from pylablib.devices import Andor


n_cam = Andor.get_cameras_number_SDK2() #hardware check - if fails, no cameras connected
SDK_ver = Andor.get_SDK2_version() #sw level check - if fails, SDK2 not installed or cannot find

Andor.AndorSDK2.TDeviceInfo() #missing 3 required positional arguments: 'controller_model', 'head_model', and 'serial_number'
Andor.AndorSDK2.TAcqProgress() #'frames_done' and 'cycles_done'
Andor.AndorSDK2.TCycleTimings() #missing 3 required positional arguments: 'exposure', 'accum_cycle_time', and 'kinetic_cycle_time'
Andor.AndorSDK2.lib


mycam = Andor.AndorSDK2Camera(fan_mode="full")
mycam.set_temperature(-10)
# MUST ALWAYS SET TEMP - built in doesn't work currently, look into ini_path?


mycam.get_acquisition_mode() #returns string - currently "cont"

mycam.is_opened() #returns bool

mycam.is_cooler_on() # returns bool - False (possibly because SDK limit)


mycam.start_acquisition()
mycam.acquisition_in_progress() # returns bool
mycam.stop_acquisition()
mycam.is_acquisition_setup()
mycam.pausing_acquisition() #trickier/unclear
mycam.clear_acquisition()
mycam.get_acquisition_parameters()

mycam.get_shutter()

#may notedo anything? - only after temp set!
mycam.is_cooler_on()
mycam.set_cooler()
mycam.set_cooler(0)

mycam.set_fan_mode('full') #options ('full','low','off')
mycam.get_fan_mode() #returns string - current "full" 


mycam.read_oldest_image()
mycam.read_newest_image()
mycam.read_multiple_images()
mycam.is_acquisition_setup()
mycam.get_accum_mode_parameters()


mycam.get_device_info()
mycam.device_info

mycam.apply_settings() #goes with positional argument for settings

mycam.get_acquisition_mode()
mycam.get_acquisition_parameters()
mycam.get_acquisition_progress()
mycam.get_capabilities() #returns info, probably json
mycam.get_buffer_size()
mycam.get_data_dimensions()
mycam.get_exposure()

mycam.get_detector_size()
mycam.get_pixel_size()

mycam.get_full_status()
mycam.get_full_info()
mycam.get_min_shutter_times()

mycam.get_image_mode_parameters()

mycam.get_read_mode()
mycam.get_readout_time()

mycam.get_roi()
mycam.get_roi_limits()

mycam.get_temperature()

mycam.get_temperature_range()
mycam.get_temperature_setpoint()
mycam.get_temperature_status() #"not reached", "not stabilized",  "off", 'stabilized'
mycam.set_temperature()


mycam.get_settings()
mycam.get_all_amp_modes()




mycam.close()