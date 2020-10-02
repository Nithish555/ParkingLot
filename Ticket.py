import ParkingSlot


class Ticket():
	"""
	Class represent the ticket format and attributes
	"""

	def __init__(self, vehicle, slot, age):
		self.__vehicle = vehicle
		self.__alloted_slot = slot
		self.__driver_age = age

	def get_slot(self):
		return self.__alloted_slot
		
	def get_driver_age(self):
		return self.__driver_age

