class Spacecraft:
    def __init__(self, position, direction):#intialization
        self.position = position
        self.direction = direction

    def execute_command(self, command):
            #This method takes a single argument, command, which is a character indicating the action to be executed.
                                       #Based on the command, it calls the corresponding method to perform the action.
        if command == 'f':             # handle the spacecraft's movement in different directions (forward and backward,left,right,up and down).
            self.move_forward()
        elif command == 'b':
            self.move_backward()
        elif command == 'r':
            self.turn_right()
        elif command == 'l':
            self.turn_left()
        elif command == 'u':
            self.turn_up()
        elif command == 'd':
            self.turn_down()

    def move_forward(self):
        if self.direction == 'N':
            self.position = (self.position[0], self.position[1] + 1, self.position[2])
        elif self.direction == 'S':
            self.position = (self.position[0], self.position[1] - 1, self.position[2])
        elif self.direction == 'E':
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif self.direction == 'W':
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
        elif self.direction == 'Up':
            self.position = (self.position[0], self.position[1], self.position[2] + 1)
        elif self.direction == 'Down':
            self.position = (self.position[0], self.position[1], self.position[2] - 1)

    def move_backward(self):
        if self.direction == 'N':
            self.position = (self.position[0], self.position[1] - 1, self.position[2])
        elif self.direction == 'S':
            self.position = (self.position[0], self.position[1] + 1, self.position[2])
        elif self.direction == 'E':
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
        elif self.direction == 'W':
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif self.direction == 'Up':
            self.position = (self.position[0], self.position[1], self.position[2] - 1)
        elif self.direction == 'Down':
            self.position = (self.position[0], self.position[1], self.position[2] + 1)

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'
       

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'

    def turn_up(self):
       
        if self.direction in ['N', 'E', 'W', 'S']:
            self.direction = 'U'
        elif self.direction == 'D':
            self.direction = 'S'
        elif self.direction == 'U':
            self.direction = 'N'

    def turn_down(self):
       
        if self.direction in ['N', 'E', 'W', 'S']:
            self.direction = 'D'
        elif self.direction == 'U':
            self.direction = 'N'
        elif self.direction == 'D':
            self.direction = 'S'
