from winreg import OpenKey, EnumValue, HKEY_CURRENT_USER

KEY_PATH = r"SOFTWARE\HWiNFO64\VSB"
SENSOR = "Sensor"
LABEL = "Label"
VALUE = "Value"
RAW = "Raw"

def get_hardware_stats() -> dict:
    hwinfo = {}
    
    with OpenKey(HKEY_CURRENT_USER, KEY_PATH) as key: # this will throw if you dont have HWINFO64 running with sensors and gadget entries enabled so maybe wrap in try except
        index = 0
        curr_master = None
        curr_label = None
        
        while True:
            try:
                value_name, value_data, _ = EnumValue(key, index)
                index += 1
                
                if value_name.startswith(SENSOR):
                    curr_master = value_data
                    if curr_master not in hwinfo:
                        hwinfo[curr_master] = {}
                    continue
                
                if value_name.startswith(LABEL):
                    curr_label = value_data
                
                if value_name.startswith(VALUE) and RAW not in value_name:
                    hwinfo[curr_master][curr_label] = value_data
                    
            except OSError:
                break
    
    return hwinfo

if __name__ == "__main__":
    from json import dumps
    print(dumps(get_hardware_stats(), indent=2))