from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

def setup_hub(hub:InventorHub):
    """ Need to change the shutdown button to left and right at same time otherwise
    it will shutdown when the center button is pressed. Currently not possible to do 
    in the block interface"""
    hub.system.set_stop_button([Button.LEFT, Button.RIGHT])

def drive_base_reset(drive_base:DriveBase):
    drive_base.reset()