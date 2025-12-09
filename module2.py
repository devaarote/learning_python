import time
import module1
from importlib import reload

module1.add(a=1,b=2)
time.sleep(2)
reload(module1) 