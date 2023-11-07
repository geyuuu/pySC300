# pySC300
A python interface of [Zolix SC300 control box series(卓立汉光SC300系列控制器)](https://www.zolix.com.cn/prodcon_371_384_447_508.html). 


## Usage

After connecting serial port, print the ports available, and initialize a SC300 instance. 
```python
from sc300 import findCOM, SC300

findCOM()

# Initialize sc300 instance on port XXX
sc=SC300(XXX)

# set speed on X axis
sc.setSpeed('X', 500)

# move 1000 steps on X axis
sc.move(self, 'X', 1000)

```

