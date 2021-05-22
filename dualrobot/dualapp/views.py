from django.shortcuts import render, HttpResponseRedirect
from gpiozero import OutputDevice, LED, AngularServo, PWMOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory

#Define the factories
factory = PiGPIOFactory(host='192.168.0.21')
factory2 = PiGPIOFactory(host='192.168.0.18')

# Define both robots
en_1 = PWMOutputDevice(12, pin_factory=factory)
en_2 = PWMOutputDevice(26, pin_factory=factory)
motor_in1 = OutputDevice(13,  pin_factory = factory)
motor_in2 = OutputDevice(21,  pin_factory = factory)
motor_in3 = OutputDevice(17,  pin_factory = factory)
motor_in4 = OutputDevice(27,  pin_factory = factory)

pin1 = OutputDevice(7,  pin_factory = factory2)
pin2 = OutputDevice(8,  pin_factory = factory2)
pin3 = OutputDevice(9,  pin_factory = factory2)
pin4 = OutputDevice(10,  pin_factory = factory2)

#Define the eyes
linus_eye = LED(16, pin_factory=factory)
torvalds_eye = LED(25, pin_factory=factory2)

# Define the servo
angular_servo = AngularServo(22, min_angle=-90, max_angle=90, pin_factory=factory)
angular_servo2 = AngularServo(23, min_angle=-90, max_angle=90, pin_factory=factory)

# Create your views here.
def index(request):
    return render(request, 'dualapp/button_dpad.html', {})

def torvaldsForward(request):
    pin1.on()
    pin2.off()
    pin3.on()
    pin4.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def torvaldsBackward(request):
    pin1.off()
    pin2.on()
    pin3.off()
    pin4.on()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def torvaldsLeft(request):
    pin1.off()
    pin2.on()
    pin3.on()
    pin4.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def torvaldsRight(request):
    pin1.on()
    pin2.off()
    pin3.off()
    pin4.on()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def stop(request):
    pin1.off()
    pin2.off()
    pin3.off()
    pin4.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def directionone(request):
    motor_in1.on()
    motor_in2.off()
    motor_in3.on()
    motor_in4.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def directiontwo(request):
    motor_in1.off()
    motor_in2.on()
    motor_in3.off()
    motor_in4.on()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def directionthree(request):
    motor_in1.on()
    motor_in2.off()
    motor_in3.off()
    motor_in4.on()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def directionfour(request):
    motor_in1.off()
    motor_in2.on()
    motor_in3.on()
    motor_in4.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def stoptwo(request):
    motor_in1.off()
    motor_in2.off()
    motor_in3.off()
    motor_in4.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def eyeon(request):
    linus_eye.on()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def eyeoff(request):
    linus_eye.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def torvaldson(request):
    torvalds_eye.on()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def torvaldsoff(request):
    torvalds_eye.off()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def minus90(request):
    angular_servo.angle = -90
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def minus45(request):
    angular_servo.angle = -45
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def zero(request):
    angular_servo.angle = 0
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def positive45(request):
    angular_servo.angle = 45
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def positive90(request):
    angular_servo.angle = 90
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def pwmThirty(request):
    en_1.value = 0.3
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def pwmFifty(request):
    en_1.value = 0.5
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def pwmFull(request):
    en_1.value = 1
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def minus902(request):
    angular_servo2.angle = -90
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def minus452(request):
    angular_servo2.angle = -45
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def zero2(request):
    angular_servo2.angle = 0
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def positive452(request):
    angular_servo2.angle = 45
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def positive902(request):
    angular_servo2.angle = 90
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def pwmThirty2(request):
    en_2.value = 0.3
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def pwmFifty2(request):
    en_2.value = 0.5
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def pwmFull2(request):
    en_2.value = 1
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))