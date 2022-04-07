#Rules of the game:
#Consider a single cell 
#   1. If cell is alive and number of neighbours alive is 2 or 3, cell continues to remain alive in the next iteration
#   2. If cell is dead and exactly 3 neighbours are alive, cell is revived in the next iteration
#   3. Remaining cells that are alive will die (and dead cells will remain dead) in the next iteration

#       Class that has all the information and methods required to implement the rules of the game:
#       - Number of rows
#       - Number of columns
#       - List of all the cell dicts
#       - Method to set the initial configuration of the cells 
#       - Method to update configuration after every iteration
#       - Method to locate the 8 neighbours surrounding a specific cell
#           ! Use cell's row and column to verify if neighbours exist within the grid
#       - Method to determine whether cell should be dead or alive in next iteration based on rules

# imports random module
import random
import time

class Game:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.cells = []

    # Create initial configuration of the game based on the number of rows and columns in the grid
    def initialize_config(self):
        # for every id number b/w 0 to l * h - 1, add a new dictionary to the list
        for n in range(0, self.rows):
            for m in range(0, self.columns):
                cell_data = {'id': (n * self.columns + m), 'row': n, 'column': m, 'status': 'alive'}
                # Figure out a way to initialize config, most likely random function
                chance = random.randint(1, 2)
                if (chance == 1):
                    cell_data['status'] = 'alive'
                else:
                    cell_data['status'] = 'dead'
                self.cells.append(cell_data)
        self.begin_game()

    # Evaluate status of cell by checking the neighbouring cells' status; conditions aren't enough. Edge case: neighbour is within range but isn't existent, i.e. id exists but neighbour doesn't
    def find_neighbours(self, id):
        # Firstly, create a list of all the neighbours
        neighbours = []
        # We need to check if the neghbouring cells at the location actually exists in the grid
        # Every neighbour is (±1 columns, ±1 rows) away from the cell.
        # So, range is from -1 to +1 rows/columns away from the cell
        # We can check if the row and column exist in the first place
        # If they do, we add it to the list of neighbours
        cell = self.cells[id]
        cell_row = cell['row']
        cell_col = cell['column']
        for n in range(-1, 2):
            for m in range(-1, 2):
                neighbour_row = cell_row + n
                neighbour_col = cell_col + m
                # check if neighbour's column and row is a part of the grid
                if ((neighbour_row >= 0 and neighbour_row <= self.rows - 1) and (neighbour_col >= 0 and neighbour_col <= self.columns - 1)):
                    neighbour_id = neighbour_row * columns + neighbour_col
                    # check that the neighbour_id we're evaluating isn't the cell's id, i.e. cell is not a neighbour of itself
                    if (neighbour_id != id):
                        neighbour_data = self.cells[neighbour_id]
                        neighbours.append(neighbour_data)
        return neighbours

    # evaluate the status of a cell for the next iteration
    def eval_status(self, id):
        neighbours = self.find_neighbours(id)
        num_dead = 0
        num_alive = 0
        cell_present_status = self.cells[id]["status"]
        # Find number of neighbours that are alive and dead
        for neighbour in neighbours:
            if (neighbour["status"] == "alive"):
                num_alive += 1
            elif (neighbour["status"] == "dead"):
                num_dead += 1
        if (cell_present_status == "alive" and (num_alive == 2 or num_alive == 3)) :
            # the cell shall stay alive
            return "alive"
        elif (cell_present_status == "dead" and num_alive == 3):
            # revive the cell
            return "alive"
        else:
            # the cell will be dead in the next iteration
            return "dead"

    # Perform the next iteration based on the rules
    # We are holding the new status values in a copy of the list because mutating the list after each element would alter the result
    def perform_iteration(self):
        cells_copy = []
        for cell in self.cells:
            id = cell["id"]
            cell_new_status = self.eval_status(id)
            new_cell = cell
            new_cell["status"] = cell_new_status
            cells_copy.append(new_cell)
        return cells_copy

    # Render the state of the game, i.e whether the cells are dead or alive
    def render_state(self):
        for n in range(0, rows):
            for m in range(0, columns):
                id = n * columns + m
                if (self.cells[id]["status"] == "alive"):
                    print("A ", end=" ")
                else:
                    print(". ", end=" ")
            print('')
        print('\n')

    def begin_game(self):
        cells = self.perform_iteration()
        self.render_state()
        time.sleep(5)
        self.begin_game()

rows = int(input("Enter the number of rows for the game: "))
columns = int(input("Enter the number of columns for the game: "))

game_of_life = Game(rows, columns)
game_of_life.initialize_config()