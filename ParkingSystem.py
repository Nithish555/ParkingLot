import os
import ParkingLot
import sys


class ParkingSystem(object):
    """
    Class will be used to controll the parking lot. 
    """
    def __init__(self):
        self.parking_lot = ParkingLot.ParkingLot()


    def parsing_input_file(self, input_file):
        """
        Function to parse the input file and read command.
        """
        if not os.path.exists(input_file):
            print("Given file {} does not exist".format(input_file))

        file_obj = open(input_file)
        try:
            while True:
                line = file_obj.readline()
                if line.endswith('\n'):
                    line = line[:-1]
                if line == '':
                    break
                self.__command(line)
                print()
        except StopIteration:
            self.__command("exit")
            file_obj.close()
        except Exception as e:
            print("Exception {} while processing the input file.".format(e))
        return


    def __command(self, interactive_input):
        """
        Function to execute command.
        """
        inputs = interactive_input.split()
        command = inputs[0].lower()
        params = inputs[1:]
        if command == 'park':
            del params[1]
        if hasattr(self.parking_lot, command):
            command_function = getattr(self.parking_lot, command)
            command_function(*params)
        else:
            print("Enter valid command, for details read README file.")


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        obj_parking_controller = ParkingSystem()
        obj_parking_controller.parsing_input_file(args[1])
    elif len(args) == 1:
        obj_parking_controller = ParkingSystem()
        # Default Input file
        obj_parking_controller.parsing_input_file("Input.txt")
    else:
        print("Enter the valid command")
