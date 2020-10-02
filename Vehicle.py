from enum import Enum

# Enum for vehicle type, can use for extending support for other type of vehicle.
class VehicleType(Enum):
	CAR, MOTORBIKE = 1, 2


# Base Vehicle class
class Vehicle():
	def __init__(self, registration_number, vehical_type):
		self.__reg_number = registration_number
		self.__type = vehical_type

	def get_reg_number(self):
		return self.__reg_number


# Child Car class, it is inheriting Vehicle class.
class Car(Vehicle):
	def __init__(self, registration_number):
		super().__init__(registration_number, VehicleType.CAR)