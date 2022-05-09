'''
Copyright Saharawat - Toy Robot
'''

'''
                  W  
                S   N
                  E  
 
            x  y->
              __ __ __ __ __
           x |__|__|__|__|__|0
           x |__|__|__|__|__|1
           x |__|__|__|__|__|2
           x |__|__|__|__|__|3
           x |__|__|__|__|__|4
              0  1  2  3  4
'''

from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Command(Enum):
    PLACE = 0
    MOVE = 1
    LEFT = 2
    RIGHT = 3
    REPORT = 4

class ToyRobot:
    def __init__(self):
        self.table_size = 5
        self.robot_direction = Direction.SOUTH #any default, does not matter.
        self.commands = [] #list of commands , N number of commands, 

        self.robot_x = int(0) #default x position, 
        self.robot_y = int(0) #defautl y postion
        self.robot_placed = False #

    def read_commands(self):
        with open('input.txt') as f:
            self.commands = f.read().splitlines()

    def execute_commands(self, commands = []):
        if (len(commands) == 0):
            self.read_commands()
        else:
            self.commands = commands
        for command in self.commands:
            command_tokens = command.split(" ")
            self.execute_command(command_tokens)

    def execute_command(self, command_tokens):
        command = command_tokens[0]
        if not self.is_valid_command(command):
            print(f"Not a valid command {command}")
            return

        if command == Command.PLACE.name:
            self.place(command_tokens[1])
        elif (command == Command.LEFT.name or command == Command.RIGHT.name):
            if self.robot_placed:
                self.rotate(command)
            else:
                print (f'command: {command} ignored as robot not placed yet')
        elif command == Command.MOVE.name:
            if self.robot_placed:
                if self.can_move():
                    self.move()
                else: 
                    print (f'command: {command} ignored as not a valid move.')
            else:
                print (f'command: {command} ignored as robot not placed yet.')
        elif command == Command.REPORT.name:
            if self.robot_placed:
                self.report()
        else:
            print (f'command: {command} as not a valid command')

    def place(self, params):
        place_params = params.split(",")
        if (self.can_place(place_params)):
            self.robot_x = int(place_params[0])
            self.robot_y = int(place_params[1])
            self.robot_direction = Direction[place_params[2]]
            self.robot_placed = True
        else:
            print ("can't place robot, not valid arguments (position or direction")

    def rotate(self, command):
        if command == Command.LEFT.name:
            new_direc = self.robot_direction.value + 3
        else:
             new_direc = self.robot_direction.value + 1
        new_direc = (new_direc % 4)
        self.robot_direction = Direction(new_direc)

    def can_move(self):
        if (self.robot_direction == Direction.SOUTH):
            return int(self.robot_y) - 1 >= 0
        if (self.robot_direction == Direction.EAST):
            return int(self.robot_x) + 1 < self.table_size
        if (self.robot_direction == Direction.NORTH):
            return int(self.robot_y) + 1 < self.table_size
        if (self.robot_direction == Direction.WEST):
            return int(self.robot_x) - 1 >= 0
        return False

    def move(self):
        if (self.robot_direction == Direction.SOUTH):
            self.robot_y = int(self.robot_y) - 1
        if (self.robot_direction == Direction.NORTH):
            self.robot_y = int(self.robot_y) + 1
        if (self.robot_direction == Direction.EAST):
            self.robot_x = int(self.robot_x) + 1
        if (self.robot_direction == Direction.WEST):
            self.robot_x = int(self.robot_x) - 1

    def report(self):
        output = [self.robot_x, self.robot_y, self.robot_direction.name]
        output = ",".join([str(x) for x in output])
        print(f"output: {output}")

    def can_place(self, place_params):
        ret = False
        if len(place_params) ==  3:
            x = int(place_params[0])
            y = int(place_params[1])
            direction = place_params[2]
            ret = self.is_valid_position(x,y) and self.is_valid_direction(direction)

        return ret

    def is_valid_direction(self, direction):
        return direction in Direction._member_names_

    def is_valid_command(self, command):
        return command in Command._member_names_

    def is_valid_position(self, x,y):
        return (x >=0 and x < self.table_size) and (y >=0 and y < self.table_size)

    def get_robot_direction(self):
        return self.robot_direction

    def set_robot_direction(self, direction): #used for unit testing
        self.robot_direction = direction

    def is_robot_placed(self): #used for unit testing
        return self.robot_placed

    def get_current_state(self): #used for unit testing
        return [self.robot_x,self.robot_y,self.robot_direction.name]


if __name__ == "__main__":
    toy_robot = ToyRobot()
    toy_robot.execute_commands()