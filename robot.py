import pikitlib
import time
from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging
logging.basicConfig(level=logging.DEBUG)

import robotmap

LEFT_HAND = 0
RIGHT_HAND = 1

class MyRobot(pikitlib.TimedRobot):
    def robotInit(self):

        self.leftBackMotor = pikitlib.SpeedController(robotmap.BACK_LEFT)
        self.leftFrontMotor = pikitlib.SpeedController(robotmap.FRONT_LEFT)
        self.rightBackMotor = pikitlib.SpeedController(robotmap.BACK_RIGHT)
        self.rightFrontMotor = pikitlib.SpeedController(robotmap.FRONT_RIGHT)

        self.left = pikitlib.SpeedControllerGroup(self.leftBackMotor, self.leftFrontMotor)
        self.right = pikitlib.SpeedControllerGroup(self.rightBackMotor, self.rightFrontMotor )

        self.myRobot = pikitlib.DifferentialDrive(self.left, self.right)

        self.DEADZONE = 0.4

        NetworkTables.initialize()
        self.driver = pikitlib.XboxController(0)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass
        
    def deadzone(self, val, deadzone):
        if abs(val) < deadzone:
            return 0
        return val

    def teleopPeriodic(self):
        forward = 0.5 * self.driver.getY(LEFT_HAND)
        rotation_value = -0.5 * self.driver.getX(RIGHT_HAND)
        self.myRobot.arcadeDrive(forward, rotation_value)

if __name__ == "__main__":
    pikitlib.run(MyRobot)

