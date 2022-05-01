import sys

direction = ['N', 'E', 'S', 'W']

# For each L go back one index
# For each R go forward one index


class Rover:
    #Constructor
    def __init__(self, x, y, borderX, borderY, currentDirection):
        self.x = x
        self.y = y
        self.direction = currentDirection
        self.borderX = borderX
        self.borderY = borderY

    def moveForward(self):
        if self.direction == 'N':
            #Checks if rover is on N border before move
            if self.y == self.borderY:
                print("Rover trying to go outside of N bounds")
            else:
                self.y += 1

        elif self.direction == 'E':
            #Checks if rover is on E border before move
            if self.x == self.borderX:
                print("Rover trying to go outside of E bounds")
            else:
                self.x += 1

        elif self.direction == 'S':
            #Checks if rover is on S border before move
            if self.y == 0:
                print("Rover trying to go outside of S bounds")
            else:
                self.y += -1

        elif self.direction == 'W':
            #Checks if rover is on W border before move
            if self.x == 0:
                print("Rover trying to go outside of W bounds")
            else:
                self.x += -1


    def turnLeft(self):
        self.direction = direction[(direction.index(self.direction) - 1) % len(direction)]

    
    def turnRight(self):
        self.direction = direction[(direction.index(self.direction) + 1) % len(direction)]
        

if __name__ == "__main__":
    
    numLines = 0
    #Checks if there is a command line argument
    if len(sys.argv) > 1:
        inputFile = sys.argv[1]

        data = []
        for line in open(inputFile):
            numLines += 1
            #Appends each line of input file to data array
            data.append(line.strip())

        numRovers = (numLines - 1) // 2

        #String indexs for each value needed
        boundaryX = data[0][8:9]
        boundaryY = data[0][10:11]

        for i in range(numRovers):

            name = data[2 + 2*i][:6]
            coordinateX = data[1 + 2*i][15:16]
            coordinateY = data[1 + 2*i][17:18]
            inputDirection = data[1 + 2*i][19:20]

            roverName = name
            roverName = Rover(int(coordinateX), int(coordinateY), int(boundaryX), int(boundaryY), inputDirection)

            instructions = data[2 + 2*i].split(':')[1]
            
            #Loops through each char in instructions
            for char in instructions:
                if char != 'M' and char != 'L' and char != 'R':
                    print("Incorrect character, skipping over it")
                else:
                    if char == 'M':
                        roverName.moveForward()
                    if char == 'L':
                        roverName.turnLeft()
                    if char == 'R':
                        roverName.turnRight()
            
            print(name, ":", roverName.x, roverName.y, roverName.direction)
    else:
        print("Wrong command line input")








