choosing python over c++
    c++ is my primary langauge that I use for developing my games, but I have been recently learning python 
    and using python for in-house automation tools etc, so thought 
    it will be good practive and learning exercise (along with writing unit tests)
    for c++ coding I use gtest as per my current dev framwork

    Job description also mention ptyhon : Work with a varied tech stack ( Python, Javascript, Typescript)

python version : Python 3.9.0

how to run toy robot challange and unit test on command console (some screen shots also attached)
py toy_robot.py 
py toy_robot_test.py 


inputs commands are taken from a text file input.txt when running the robot test app normally. sample snapshot of input.txt
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT

inputs can also be feed directly to execute_commands API (used for unit testing purpose at the moment) example like below, 
toy_robot = ToyRobot()
toy_robot.execute_commands(["PLACE 1,2,EAST", "MOVE","MOVE","LEFT", "MOVE", "REPORT"])