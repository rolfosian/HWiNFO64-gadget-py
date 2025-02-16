from winreg import OpenKey, EnumValue, HKEY_CURRENT_USER
key_path = r"SOFTWARE\HWiNFO64\VSB"
def get_hardware_stats():
    hwinfo = {}
    
    with OpenKey(HKEY_CURRENT_USER, key_path) as key:
        index = 0
        curr_m = None
        curr_label = None
        
        while True:
            try:
                value_name, value_data, _ = EnumValue(key, index)
                index += 1
                
                if value_name.startswith('Sensor'):
                    curr_m = value_data
                    if curr_m not in hwinfo:
                        hwinfo[curr_m] = {}
                    continue
                
                if value_name.startswith('Label'):
                    curr_label = value_data
                
                if value_name.startswith('Value') and 'Raw' not in value_name:
                    hwinfo[curr_m][curr_label] = value_data
            except OSError:
                break
    
    return hwinfo

if __name__ == "__main__":
    from json import dumps
    print(dumps(get_hardware_stats(), indent=2))