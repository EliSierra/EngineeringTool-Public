import odrive
import math
import enum
from odrive.enums import *
from odrive.utils import *
import time

odrv = odrive.find_any()
odrv.config.dc_bus_overvoltage_trip_level = 50
odrv.config.dc_bus_undervoltage_trip_level = 40
odrv.config.dc_max_positive_current = math.inf
odrv.config.dc_max_negative_current = -math.inf
odrv.axis0.config.motor.motor_type = MotorType.HIGH_CURRENT # type: ignore
odrv.axis0.config.motor.pole_pairs = 4
odrv.axis0.config.motor.torque_constant = 0.13232
odrv.axis0.config.motor.current_soft_max = 18
odrv.axis0.config.motor.current_hard_max = 33.4
odrv.axis0.config.motor.calibration_current = 10
odrv.axis0.config.motor.resistance_calib_max_voltage = 20
odrv.axis0.config.calibration_lockin.current = 10
odrv.axis0.motor.motor_thermistor.config.enabled = False
odrv.axis0.controller.config.control_mode = ControlMode.VELOCITY_CONTROL
odrv.axis0.controller.config.input_mode = InputMode.VEL_RAMP
odrv.axis0.controller.config.vel_limit = 10
odrv.axis0.controller.config.vel_limit_tolerance = 1.4
odrv.axis0.config.torque_soft_min = -0.476
odrv.axis0.config.torque_soft_max = 0.476
odrv.axis0.trap_traj.config.accel_limit = 50
odrv.axis0.controller.config.vel_ramp_rate = 50
odrv.can.config.protocol = Protocol.NONE
odrv.axis0.config.enable_watchdog = False
odrv.axis0.config.encoder_bandwidth = 100
odrv.hall_encoder0.config.enabled = True
odrv.axis0.config.load_encoder = EncoderId.HALL_ENCODER0
odrv.axis0.config.commutation_encoder = EncoderId.HALL_ENCODER0
odrv.config.enable_uart_a = False

