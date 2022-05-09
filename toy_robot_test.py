'''
Copyright Saharawat - Toy Robot
'''

import unittest
from toy_robot import Command, Direction, ToyRobot

class TestToyRobot(unittest.TestCase):
    def test_is_valid_direction(self):
        toy_robot = ToyRobot()
        self.assertEqual(toy_robot.is_valid_direction('NORTH'), True)
        self.assertEqual(toy_robot.is_valid_direction('EAST'), True)
        self.assertEqual(toy_robot.is_valid_direction('SOUTH'), True)
        self.assertEqual(toy_robot.is_valid_direction('WEST'), True)
        self.assertEqual(toy_robot.is_valid_direction('WESTT'), False)
        self.assertEqual(toy_robot.is_valid_direction(''), False)

    def test_is_valid_command(self):
        toy_robot = ToyRobot()
        self.assertEqual(toy_robot.is_valid_command('PLACE'), True)
        self.assertEqual(toy_robot.is_valid_command('LEFT'), True)
        self.assertEqual(toy_robot.is_valid_command('RIGHT'), True)
        self.assertEqual(toy_robot.is_valid_command('MOVE'), True)
        self.assertEqual(toy_robot.is_valid_command('REPORT'), True)
        self.assertEqual(toy_robot.is_valid_command(''), False)

    def test_rotate(self):
        toy_robot = ToyRobot()
        self.assertEqual(toy_robot.get_robot_direction(), Direction.SOUTH)
        toy_robot.rotate(Command.LEFT.name)
        self.assertEqual(toy_robot.get_robot_direction(), Direction.EAST)
        toy_robot.rotate(Command.LEFT.name)
        self.assertEqual(toy_robot.get_robot_direction(), Direction.NORTH)
        toy_robot.rotate(Command.LEFT.name)
        self.assertEqual(toy_robot.get_robot_direction(), Direction.WEST)
        toy_robot.rotate(Command.LEFT.name)
        self.assertEqual(toy_robot.get_robot_direction(), Direction.SOUTH)

        toy_robot.rotate(Command.RIGHT.name)
        self.assertEqual(toy_robot.get_robot_direction(), Direction.WEST)
        toy_robot.rotate(Command.RIGHT.name)
        self.assertEqual(toy_robot.get_robot_direction(), Direction.NORTH)
        toy_robot.rotate(Command.RIGHT.name)
        self.assertEqual(toy_robot.get_robot_direction(), Direction.EAST)
        toy_robot.rotate(Command.RIGHT.name)
        self.assertEqual(toy_robot.get_robot_direction(), Direction.SOUTH)

    def test_can_place(self):
        toy_robot = ToyRobot()
        self.assertEqual(toy_robot.can_place([]), False)
        self.assertEqual(toy_robot.can_place([0]), False)
        self.assertEqual(toy_robot.can_place([0,0]), False)
        self.assertEqual(toy_robot.can_place([0,0,0]), False)
        self.assertEqual(toy_robot.can_place([0,0,'SOUTHNORTH']), False)
        self.assertEqual(toy_robot.can_place([0,0,'SOUTH']), True)
        self.assertEqual(toy_robot.can_place([0,0,'NORTH']), True)
        self.assertEqual(toy_robot.can_place([0,0,'EAST']), True)
        self.assertEqual(toy_robot.can_place([0,0,'WEST']), True)
        self.assertEqual(toy_robot.can_place([1,1,'WEST']), True)
        self.assertEqual(toy_robot.can_place([2,2,'WEST']), True)
        self.assertEqual(toy_robot.can_place([3,3,'WEST']), True)
        self.assertEqual(toy_robot.can_place([4,4,'WEST']), True)
        self.assertEqual(toy_robot.can_place([5,5,'WEST']), False)
        self.assertEqual(toy_robot.can_place([6,6,'WEST']), False) 
        self.assertEqual(toy_robot.can_place([-1,0,'WEST']), False) 
        self.assertEqual(toy_robot.can_place([-1,-1,'WEST']), False) 
        self.assertEqual(toy_robot.can_place([0,-1,'WEST']), False) 

    def test_place_invalid_arguments(self):
        toy_robot = ToyRobot()
        toy_robot.place("")
        self.assertEqual(toy_robot.is_robot_placed(), False)
        toy_robot.place("0")
        self.assertEqual(toy_robot.is_robot_placed(), False)
        toy_robot.place("0,0")
        self.assertEqual(toy_robot.is_robot_placed(), False)
        toy_robot.place("0,0,NORT")
        self.assertEqual(toy_robot.is_robot_placed(), False)
        toy_robot.place("7,0,NORTH")
        self.assertEqual(toy_robot.is_robot_placed(), False)
        toy_robot.place("-1,0,NORTH")
        self.assertEqual(toy_robot.is_robot_placed(), False)

    def test_place_valid_arguments(self):
        toy_robot = ToyRobot()
        toy_robot.place("0,0,NORTH")
        self.assertEqual(toy_robot.is_robot_placed(), True)

    def test_multiple_place_commands(self):
        toy_robot = ToyRobot()
        toy_robot.place("0,0,NORTH")
        self.assertEqual(toy_robot.is_robot_placed(), True)
        toy_robot.place("1,2,SOUTH")
        self.assertEqual(toy_robot.get_current_state(), [1,2,Direction.SOUTH.name])

    def test_can_move(self):
        toy_robot = ToyRobot()
        toy_robot.place("0,0,SOUTH")
        self.assertEqual(toy_robot.can_move(), False)
        toy_robot.place("0,1,SOUTH")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("0,2,SOUTH")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("0,3,SOUTH")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("0,4,SOUTH")
        self.assertEqual(toy_robot.can_move(), True)

        toy_robot.place("1,0,SOUTH")
        self.assertEqual(toy_robot.can_move(), False)
        toy_robot.place("2,0,SOUTH")
        self.assertEqual(toy_robot.can_move(), False)
        toy_robot.place("3,0,SOUTH")
        self.assertEqual(toy_robot.can_move(), False)
        toy_robot.place("4,0,SOUTH")
        self.assertEqual(toy_robot.can_move(), False)

        #test movement from EAST
        toy_robot.place("0,0,EAST")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("1,1,EAST")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("2,2,EAST")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("3,3,EAST")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("4,4,EAST")
        self.assertEqual(toy_robot.can_move(), False)

        #test movement from NORTH
        toy_robot.place("0,0,NORTH")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("0,1,NORTH")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("0,2,NORTH")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("0,3,NORTH")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("0,4,NORTH")
        self.assertEqual(toy_robot.can_move(), False)

        toy_robot.place("0,1,NORTH")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("0,2,NORTH")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("0,3,NORTH")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("0,4,NORTH")
        self.assertEqual(toy_robot.can_move(), False)

        toy_robot.place("1,1,NORTH")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("2,2,NORTH")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("3,3,NORTH")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("4,4,NORTH")
        self.assertEqual(toy_robot.can_move(), False)

        #test movement from WEST
        toy_robot.place("0,0,WEST")
        self.assertEqual(toy_robot.can_move(), False)
        toy_robot.place("1,1,WEST")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("2,2,WEST")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("3,3,WEST")
        self.assertEqual(toy_robot.can_move(), True)
        toy_robot.place("4,4,WEST")
        self.assertEqual(toy_robot.can_move(), True)

    def test_execute_commands_example_1(self):
        toy_robot = ToyRobot()
        toy_robot.execute_commands(["PLACE 0,0,NORTH", "MOVE","REPORT"])
        self.assertEqual(toy_robot.get_current_state(), [0,1,Direction.NORTH.name])

    def test_execute_commands_example_2(self):
        toy_robot = ToyRobot()
        toy_robot.execute_commands(["PLACE 0,0,NORTH", "LEFT","REPORT"])
        self.assertEqual(toy_robot.get_current_state(), [0,0,Direction.WEST.name])

    def test_execute_commands_example_3(self):
        toy_robot = ToyRobot()
        toy_robot.execute_commands(["PLACE 1,2,EAST", "MOVE","MOVE","LEFT", "MOVE", "REPORT"])
        self.assertEqual(toy_robot.get_current_state(), [3,3,Direction.NORTH.name])

    def test_execute_commands_ignore_commands_until_placed(self):
        toy_robot = ToyRobot()
        toy_robot.execute_commands(["LEFT", "RIGHT", "PLACE 1,2,EAST", "MOVE","MOVE","LEFT", "MOVE", "REPORT"])
        self.assertEqual(toy_robot.get_current_state(), [3,3,Direction.NORTH.name])

    def test_execute_commands_multiple_place_commands(self):
        toy_robot = ToyRobot()
        toy_robot.execute_commands(["LEFT", "RIGHT", "PLACE 1,2,EAST", "MOVE","MOVE","LEFT", "PLACE 4,2,EAST", "MOVE", "REPORT"])
        self.assertEqual(toy_robot.get_current_state(), [4,2,Direction.EAST.name])
        
if __name__ == '__main__':
    unittest.main()