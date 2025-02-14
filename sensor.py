from microbit import *
import radio

radio.on()
radio.config(group=1)

# Simulated DS18B20 OneWire Read Function
def read_ds18b20(pin):
    pin.write_digital(0)
    sleep(1)
    pin.write_digital(1)
    sleep(1)
    pin.read_digital()
    sleep(1)
    return 25.0  # Simulated temperature reading

datapin = pin1  # DS18B20 connected to Pin1

while True:
    msg = radio.receive()  # Receive data
    
    if msg:  # Only proceed if a message is received
        temp = read_ds18b20(datapin)  # Get temperature
        signal_strength = -60  # Simulating an RSSI value (since receive_full() is not available)
        
        display.show(abs(signal_strength) // 10)  # Display signal strength as a bar graph
        print("T:" + str(temp) + ", RSSI:" + str(signal_strength))
    sleep(1000)  # Read every second
