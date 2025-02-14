from microbit import *
import radio
import machine, onewire, ds18x20

# Setup Radio
radio.on()
radio.config(group=1)

# Setup DS18B20 Temperature Sensor on Pin0
datapin = machine.Pin(0)
ds = ds18x20.DS18X20(onewire.OneWire(datapin))
roms = ds.scan()

# Function to get temperature
def get_temperature():
    ds.convert_temp()
    sleep(750)  # Wait for conversion
    for rom in roms:
        return ds.read_temp(rom)  # Return first sensor reading
    return None

while True:
    msg = radio.receive()  # Check for a signal from Micro:bit 2
    
    if msg:
        temp = get_temperature()  # Get temperature
        signal_strength = radio.receive_full()[1]  # RSSI value
        
        # Display signal strength as a bar graph
        display.show(abs(signal_strength) // 10)

        # Print data to the serial console
        print(f"T:{temp:.1f}, RSSI:{signal_strength}")

    sleep(1000)  # Read every second
