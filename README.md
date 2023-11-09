# pySC300
A python interface of [Zolix SC300 control box series(卓立汉光SC300系列控制器)](https://www.zolix.com.cn/prodcon_371_384_447_508.html). 

SC300 series controls up to three stepper motors. pySC300 is based on its serial communication protocol.

## Usage

After connecting serial port, print the ports available, and initialize a SC300 instance. 
```python
from sc300 import findCOM, SC300

findCOM()

# Initialize sc300 instance on port N
sc=SC300(N)

# Find more commands in sc300.py
# Set speed on X axis. Return 'OK' if success.
sc.setSpeed('X', 500)

# Move 1000 steps on X axis
sc.move(self, 'X', 1000)

# Set the initial speed of X axis to 0
sc.setInit('X', 0)

# Set the acceleration of X axis to 100
sc.setAcc('X', 100)

# Get the position of Y axis. Return a int position
position_y = sc.getPosition('Y')

# Find more commands in sc300.py
```

