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
        cur = ts.getActive()
        ts.requestUpdate()
        if cur != ts.getActive():
            print('Update on: ' + ts)

        time.sleep(5)

if __name__ == '__main__' :main()
