# read_button
Simple code to read a button

## read_button.py
Read button press and output state

## read_button2.py
Read button press and light LED

### Connections
#### LED
* GND       ---> LED cathode
* LED anode ---> Resistor
* Resistor  ---> GPIO 17

#### Button
* Prong #1 ---> GPIO 6
* Prong #2 ---> 3.3v

### Running
`sudo ./read_button2.py`
