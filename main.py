import keyboard
import sys, os
import random as rd


class CreateGame:

    def __init__(self, grid_size=4, start_tiles=2):

        self.grid_size = grid_size
        self.start_tiles = start_tiles
        self.grid = None
        self.score = 0

    def start_game(self):
        
        length = range(self.grid_size)
        new_grid = [[0 for i in length] for row in length]

        start_tiles = self.start_tiles

        while start_tiles:
            x = rd.randint(0, self.grid_size-1)
            y = rd.randint(0, self.grid_size-1)

            if new_grid[x][y] == 0:
                new_grid[x][y] = 2
                start_tiles -= 1

        self.grid = new_grid
    
    def move_tiles(self, direction):

        # Move up
        if direction == 'w':
            for idxr, row in enumerate(self.grid):
                for idxc, col in enumerate(row):
                    if col != 0:
                        check = idxr
                        while check != 0:
                            if self.grid[check-1][idxc] == 0:
                                self.grid[check-1][idxc] = col
                                self.grid[check][idxc] = 0
                            elif self.grid[check-1][idxc] == col:
                                self.grid[check-1][idxc] = col*2
                                self.grid[check][idxc] = 0
                            check -= 1
        
        # Move left
        if direction == 'a':
            for idxr, row in enumerate(self.grid):
                for idxc, col in enumerate(row):
                    if col != 0:
                        check = idxc
                        while check != 0:
                            if self.grid[idxr][check-1] == 0:
                                self.grid[idxr][check-1] = col
                                self.grid[idxr][check] = 0
                            elif self.grid[idxr][check-1] == col:
                                self.grid[idxr][check-1] = col*2
                                self.grid[idxr][check] = 0
                            check -= 1
    
    def new_tile(self):

        space = False

        if any(0 in x for x in self.grid):
            space = True

        while space:
            x = rd.randint(0, self.grid_size-1)
            y = rd.randint(0, self.grid_size-1)

            if self.grid[x][y] == 0:
                self.grid[x][y] = 2
                break
            

    def check_status(self):
        return True



if __name__ == "__main__":
    new_game = CreateGame()
    new_game.start_game()
    os.system('cls')

    while new_game.check_status:
        print('==================')

        for row in new_game.grid:
            print(row)

        print('==================')

        print("Keys: w=up, s=down, a=left, d=right")
        action = ''
        
        # Wait for user input
        while True:
            
            if keyboard.is_pressed('w'):
                action = 'w'
                break

            if keyboard.is_pressed('a'):
                action = 'a'
                break

            if keyboard.is_pressed('q'):
                new_game.check_status = False
                break
            

        new_game.move_tiles(action)
        new_game.new_tile()

        # If game still running clear old grid
        if new_game.check_status:
            os.system('cls')

        