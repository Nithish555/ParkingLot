import sys
import ParkingSlot
import Ticket
from Vehicle import *


class ParkingLot:
	"""
	This is a class for parking lot.
	It will have all the functionality require to operate the parking lot.
	"""
	__instance = None

	class __ParkingInstance:
	    def __init__(self, name):
	    	self.__name = name

	    	# slot information.
	    	self.slots = {}

	    	# Currently parked vehicles information
	    	self.car_list = []
	

	def __init__(self, name="Parking_Lot"):
	   	if not ParkingLot.__instance:
	   		ParkingLot.__instance = ParkingLot.__ParkingInstance(name)
	   	else:
	   		ParkingLot.__instance.__name = name


	def __getattr__(self, name):
		return getattr(self.__instance, name)
	

	def create_parking_lot(self, no_of_slot):
		"""
		Function to create parking slots.
		"""
		try:
			for slot_number in range(1, int(no_of_slot) + 1):
				self.slots[slot_number] = ParkingSlot.ParkingSlot(slot_number=slot_number)

		except Exception as e:
			print("Exception {} occurred while initiating parking lot.".format(e))

		print("Created a parking lot with {} slots".format(no_of_slot))
		


	def __get_next_available_slot(self):
		"""
		Function to get next available slot
		"""

		available_slots = filter(lambda slot: slot.is_available(), self.slots.values())
		if not available_slots:
		    return None

		return sorted(available_slots, key=lambda slot: slot.get_slot_number())[0]


	def park(self, reg_number, age):
		"""
		Function to create a new vehicle and park it
		"""

		if not self.__is_parking_created():
			print("Parking not created yet.")
			return
		obj_vehicle = Car(registration_number=reg_number)
		self.park_new_vehicle(obj_vehicle, age)


	def park_new_vehicle(self, vehicle, age):
		"""
		Function to park the vehicle recieved from park function
		"""

		# Check if parking lot is full or have space
		if self.__is_full():
			try:
				slot = self.__get_next_available_slot()
				if slot:
					slot.park_vehicle(vehicle)

				ticket = Ticket.Ticket(vehicle, slot, age)
				slot.generate_ticket(ticket)

				self.car_list.append(vehicle)

				print('Car with vehicle registration number "{}" has been parked at slot number {}'.format(vehicle.get_reg_number(),slot.get_slot_number()))
			except Exception as e:
				print("Exception {} while parking vehicle".format(e))
		else:
			print("Sorry, parking lot is full.")



	def __is_full(self):
		"""
		Function to check the parking lot is full
		"""

		for slot in self.slots.values():
			if slot.is_available():
				return True

		return False

	def __is_parking_created(self):
		"""
		Function to check the parking lot is created or not
		"""

		if not self.slots:
			return False
		else:
			return True

	def leave(self, slot_num):
		"""
		Function to release the slot
		"""

		if not self.__is_parking_created():
			print("Parking not created yet.")
			return

		try:
			slot = self.slots[int(slot_num)]
			if not slot.is_available():
				ticket_assigned = slot.get_generated_ticket()
				slot = ticket_assigned.get_slot()
				age = ticket_assigned.get_driver_age()
				registration_number = slot.get_parked_vehicle().get_reg_number()
				self.car_list.remove(slot.get_parked_vehicle())
				slot.empty_slot()
				print('Slot number {}  vacated, the car with vehicle registration number "{}" left the space, the driver of the car was of age {} '.format(slot_num, registration_number, age))
			else:
				print("No vehicle parked at slot {}.".format(slot_num))
		except Exception as e:
			print("Exception {} while leaving".format(e))


	def status(self):
		"""
		Function to print the status of parking lot.
		"""

		if not self.__is_parking_created():
			print("There is no Parking created yet.")
			return

		print("Slot No. \t Registration No. \t age")
		for slot in self.slots.values():
			if not slot.is_available():
				vehicle = slot.get_parked_vehicle()
				ticket = slot.get_generated_ticket()
				print("{} \t \t {} \t \t {}".format(slot.get_slot_number(),
					  vehicle.get_reg_number(), ticket.get_driver_age()))


	def exit(self):
		sys.exit()


	
	def vehicle_registration_number_for_driver_of_age(self, age):
		"""
		Function to get the vehicle registration numbers for driver of age 
		"""

		if not self.__is_parking_created():
			print("There is no Parking created yet.")
			return

		list_vehicle_reg = []
		try:
			for slot in self.slots.values():
				if not slot.is_available():
					ticket = slot.get_generated_ticket()
					if ticket.get_driver_age() == age:
						list_vehicle_reg.append(slot.get_parked_vehicle().get_reg_number())

		except Exception as e:
			print("Exception {} while getting cars with ages".format(e))

		if(len(list_vehicle_reg)==0):
			print("There is no vehical registration number found for this particular age")
		else:
			registaration_number = str(list_vehicle_reg)[1:-1]
			print("These are the vehicle registartion numbers found for this particular age "+registaration_number)


	def slot_number_for_car_with_number(self, vehicle_reg_num):
		"""
		Function to get the slot number for car with registration number
		"""

		if not self.__is_parking_created():
			print("Parking not created yet.")
			return

		try:
			for slot in self.slots.values():
				if not slot.is_available():
					vehicle = slot.get_parked_vehicle()
					if vehicle.get_reg_number() == vehicle_reg_num:
						print("The slot number for the vehicle registration number is", slot.get_slot_number())
						break
			else:
				print("The vehicle registration number is not found")
		except Exception as e:
			print("Exception {} while getting slots with registration number".format(e))


	def slot_numbers_for_driver_of_age(self, age):
		"""
		Function to get the slot numbers for driver of age
		"""
		if not self.__is_parking_created():
			print("Parking not created yet.")
			return

		list_slot_number = []
		try:
			for slot in self.slots.values():
				if not slot.is_available():
					ticket = slot.get_generated_ticket()
					if ticket.get_driver_age() == age:
						list_slot_number.append(slot.get_slot_number())
			
		except Exception as e:
			print("Exception {} while getting slots with ages".format(e))
		
		if(len(list_slot_number)==0):
			print("There is no slot number found for this particular age")
		else:
			slot_number = str(list_slot_number)[1:-1]
			print("These are the slot numbers found for this particular age " + slot_number)


