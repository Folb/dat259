from actuator import Actuator
import sys
import time

class TemperatureActuator(Actuator):
    
    def __init__(self):
        super().setType('temperature')

def main():
    sid = int(sys.argv[1])
    ta = TemperatureActuator()
    ta.setId(sid)
    ta.setActive(False)

    while True:
        cur = ta.isActive()
        ta.requestUpdate()
        if cur != ta.isActive():
            print('Update on: ' + ta)

        time.sleep(5)

if __name__ == '__main__' :main()
