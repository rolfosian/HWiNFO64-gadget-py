1. Launch HWiNFO64 with sensors
2. Go to Sensor Settings
3. Go to HWiNFO Gadget tab
4. Tick `Enable reporting to Gadget` and `Report value in Gadget` on the entries desired.
5. Click OK
6. Test by running main.py directly

*Note: It will hit an exception on trying to open the registry key if HWiNFO64 isn't running with sensors.*

Example output
```
{
  "CPU [#0]: AMD Ryzen 7 7800X3D": {
    "Core Clocks": "4,528.1 MHz",
    "Total CPU Usage": "7.6 %"
  },
  "CPU [#0]: AMD Ryzen 7 7800X3D: Enhanced": {
    "CPU (Tctl/Tdie)": "52.1 \u00b0C",
    "CPU Die (average)": "50.1 \u00b0C",
    "CPU Package Power": "27.088 W"
  },
  "GPU [#0]: NVIDIA GeForce RTX 4080: ASUS TUF RTX 4080 GAMING OC": {
    "GPU Temperature": "41.5 \u00b0C",
    "GPU Memory Junction Temperature": "46.0 \u00b0C",
    "GPU Hot Spot Temperature": "52.7 \u00b0C",
    "GPU Core Voltage": "0.930 V",
    "GPU Power": "16.683 W",
    "GPU Clock": "255.0 MHz",
    "GPU Memory Clock": "101.2 MHz",
    "GPU Effective Clock": "772.3 MHz",
    "GPU Core Load": "4.0 %",
    "GPU Memory Allocated": "2,367 MB"
  }
}
```