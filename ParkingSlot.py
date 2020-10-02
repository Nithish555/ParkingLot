from Vehicle import *
import Ticket


class ParkingSlot():
	"""
	Class represent every slot of parking lot.
	Slot have three things.
	1. Slot information.
	2. Vehicle parked.
	3. Assigned ticket information.
	"""
	
	def __init__(self, slot_number, vehicle_type=VehicleType.CAR, ticket=None):
		self.__slot_number = slot_number
		self.__vehicle = None
		self.__is_available = True
		self.__ticket = ticket


	def generate_ticket(self, ticket):
		self.__ticket = ticket


	def get_generated_ticket(self):
		return self.__ticket


	def empty_slot(self):
		self.__vehicle = None
		self.__is_available = True


	def get_parked_vehicle(self):
		return self.__vehicle


	def park_vehicle(self, vehicle):
		self.__vehicle = vehicle
		self.__is_available = False


	def set_availablity(self, is_available):
		self.__is_available = is_available


	def is_available(self):
		return self.__is_available


	def get_slot_number(self):
		return self.__slot_number
