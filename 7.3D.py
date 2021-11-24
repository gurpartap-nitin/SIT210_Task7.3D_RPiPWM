from gpiozero import DistanceSensor
from time import sleep
from gpiozero import PWMLED

pwm = PWMLED(21)
echo = 17
trigger = 27
distance = DistanceSensor(echo, trigger)
while True:
    
    cal_distance = distance.distance*100
    print('Distance: ',  cal_distance)
    sleep(0.2)
    
    if cal_distance < 50.0 and  cal_distance > 40.0:
        pwm.value = 0.2
        sleep(0.2)
        
    elif cal_distance < 40.0 and cal_distance > 30.0:
        pwm.value = 0.5
        sleep(0.2)
        
    elif cal_distance < 30.0 and cal_distance > 15.0:
        pwm.value = 0.7
        sleep(0.2)
        
    elif cal_distance < 15.0 and  cal_distance > 0.0:
        pwm.value = 1
        sleep(0.2)
    else:
        pwm.value = 0
        sleep(0.2)