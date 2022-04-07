#Rules of the game:
#Consider a single cell 
#   1. If cell is alive and number of neighbours alive is 2 or 3, cell continues to remain alive in the next iteration
#   2. If cell is dead and exactly 3 neighbours are alive, cell is revived in the next iteration
#   3. Remaining cells that are alive will die (and dead cells will remain dead) in the next iteration

# Steps:
#   1. Create a class that has all the information and methods required to implement the rules of the game:
#       - Number of rows
#       - Number of columns
#       - Method to set the initial configuration of the cells and the configuration after every iteration
#           * In this method, we have to locate the 8 neighbours surrounding a specific cell
#           ! Formula to locate a cell's 8 neighbours (assuming there are l columns and h rows, and id of cell is n):
#               - T: n - l
#               - B: n + l
#               - L: n - 1
#               - R: n + 1
#               - TR: n - (l - 1)
#               - TL: n - (l + 1)
#               - BR: n + (l + 1)
#               - BL: n + (l - 1)
#               - Edge cases: check if the id of the neighbour is >= 0 and <= l * h - 1 (in order to see if it actually exists; corner cells might miss some neighbours)
#               - View formula-1.jpg and formula-2.jpg to see how I arrived at the formula
#           * Once located, we have to determine whether the cell should be dead or alive in the next iteration
#           ? How do we configure the initial state, when the game first starts. 
#           ? Do we assume that all of the cells are dead/alive? 
#           ? Or do we use use a random function to determine the initial state of each cell? 
#           ? Does this even matter in the first place?

# Get number of rows required for the game from user
rows = int(input("Enter the number of rows for the game: "))
# Get number of columns required for the game from user
columns = int(input("Enter the number of columns for the game: "))
# Create a list of dictionaries that looks like this:
# [{'row': 0, 'column': 0, 'status': 'dead'}, ...]
cells = []

# Figuring out function syntax
def generate_cells_data():
    # for every id number b/w 0 to l * h - 1, add a new dictionary to the list
    for n in range(0, rows * columns):
        # This is giving me an error, need to figure out syntax
        cells.append({"id": n, "status": "alive"})

# Evaluate status of cell by checking the neighbouring cells' status; conditions aren't enough. Edge case: neighbour is within range but isn't existent, i.e. id exists but neighbour doesn't
def find_neighbours(id):
    # Firstly, create a list of all the neighbours
    neighbours = []
    # We need to check if the neghbouring cells at the location actually exists in the grid
    # Every neighbour is (±1 columns, ±1 rows) away from the cell.
    # So, range is from -1 to +1 rows/columns away from the cell
    # We can check if the row and column exist in the first place
    # If they do, we add it to the list of neighbours

    # Top neighbour
    # if ((id - columns) >= 0 and (id - columns) <= (rows * columns - 1)):
    #     neighbours.append(id - columns)
    #     print("top")
    # # Bottom neighbour
    # if ((id + columns) >= 0 and (id + columns) <= (rows * columns - 1)):
    #     neighbours.append(id + columns)
    #     print("bottom")
    # # Left neighbour
    # if ((id - 1) >= 0 and (id - 1) <= (rows * columns - 1)):
    #     neighbours.append(id - 1)
    #     print("left")
    # # Right neighbour
    # if ((id + 1) >= 0 and (id + 1) <= (rows * columns - 1)):
    #     neighbours.append(id + 1)
    #     print("right")
    # # Top-right neighbour
    # if ((id - (columns - 1)) >= 0 and (id - (columns - 1)) <= (rows * columns - 1)):
    #     neighbours.append(id - (columns - 1))
    #     print("tr")
    # # Top-left neighbour
    # if ((id - (columns + 1)) >= 0 and (id - (columns + 1)) <= (rows * columns - 1)):
    #     neighbours.append(id - (columns + 1))
    #     print("tl")
    # # Bottom-right neighbour
    # if ((id + (columns + 1)) >= 0 and (id + (columns + 1)) <= (rows * columns - 1)):
    #     neighbours.append(id + (columns + 1))
    #     print("br")
    # # Bottom-left neighbour
    # if ((id + (columns - 1)) >= 0 and (id + (columns - 1)) <= (rows * columns - 1)):
    #     neighbours.append(id + (columns - 1))
    #     print("bl")
    # return neighbours

def eval_status(id):
    neighbours = find_neighbours(id)
    num_dead = 0
    num_alive = 0
    cell_present_status = cells[id]["status"]
    # Find number of neighbours that are alive and dead
    for neighbour in neighbours:
        if (cells[neighbour]["status"] == "alive"):
            num_alive += 1
        elif (cells[neighbour]["status"] == "dead"):
            num_dead += 1
    if (cell_present_status == "alive" and (num_alive == 2 or num_alive == 3)) :
        print("remain alive")
    elif (cell_present_status == "dead" and num_alive == 3):
        print("revive")
    else:
        print(neighbours)




generate_cells_data()
find_neighbours(2)
eval_status(2)