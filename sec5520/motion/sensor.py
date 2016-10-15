from gpiozero import MotionSensor

class Sensor:
    def __init__(self):
        self.last_msg_sent_at = 0
        self.pir = MotionSensor(14)

    def on_detect(self, callback):
        while True:
            print("Waiting for Motion...")
            self.pir.wait_for_motion()

            # while is motion, call callback
            print("Calling handler...")
            callback()

            print("Waiting for No Motion...")
            self.pir.wait_for_no_motion()
