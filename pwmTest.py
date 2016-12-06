import mraa
import time
class pwmTest:

    def __init__(self):
        self.pwmA1 = mraa.Pwm(18)
        self.pwmA1.period_ms(2)
        self.pwmA1.enable(True)

        self.pwmA2 = mraa.Pwm(19)
        self.pwmA2.period_ms(2)
        self.pwmA2.enable(True)

        self.pwmB1 = mraa.Pwm(20)
        self.pwmB1.period_ms(1000000)
        self.pwmB1.enable(True)

        self.pwmB2 = mraa.Pwm(21)
        self.pwmB2.period_ms(1000000)
        self.pwmB2.enable(True)
        self.wheelBack()

        self.led1 = mraa.Gpio(1)
        self.led1.dir(mraa.DIR_OUT)
        self.led1Swicher = False
        # self.shak()
    def ledSwich(self):
        self.led1Swicher = not self.led1Swicher
        if (self.led1Swicher):
            self.led1.write(1)
        else:
            self.led1.write(0)
        
    def B1(self,i):
        self.pwmB1.write(i)
    def B2(self,i):
        self.pwmB2.write(i)
    def stop(self):

        self.pwmA2.write(0)
        self.pwmA1.write(0)
        # time.sleep(0.5)
    def wheelBack(self):
        self.pwmB2.write(0)
        self.pwmB1.write(0)
        # time.sleep(0.1)

        # self.shak()

    def shak(self):
        self.right()
        # time.sleep(0.1)
        self.left()
        # time.sleep(0.1)
    def left(self):

        self.pwmB2.write(0)
        self.pwmB1.write(1)
        # time.sleep(0.1)
        # self.wheelBack()

    def right(self):
        self.pwmB2.write(1)
        self.pwmB1.write(0)
        # time.sleep(0.1)
        # self.wheelBack()

    def back(self):
        self.pwmA1.write(1)
        self.pwmA2.write(0)

    def forwake(self):
        self.pwmA1.write(0)
        self.pwmA2.write(1)

    def go(self,motor1status,motor2status):
        if motor1status == 0 :
            self.stop()
        if motor1status == 1 :
            self.forwake()
        if motor1status == 2 :
            self.back()
        if motor2status == 0 :
            self.wheelBack()
        if motor2status == 1 :
            # self.shak()
            self.left()
        if motor2status == 2 :
            # self.shak()
            self.right()

        # self.stop()
def main():

    pwm = pwmTest()
    # while 1:
        # pwm.right()
if __name__ == "__main__":
    main()
