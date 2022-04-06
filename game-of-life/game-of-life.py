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
#           ? How to locate? This is a 2D grid, so there'll be an X coordinate, and a Y coordinate. We could assume that the first cell is located at (0, 0).
#           ! There must be a formula to find the 8 neighbours that applies for every integer ranging from 1...n; where n = rows * columns, i.e. the final cell
#           ! View formula-1.jpg. I think it checks out for all square grids. Will check if it replicates for other values of n by induction. Next, have to figure out edge cases, i.e. how to check if a neighbour exists in that location in the first place?
#           ? What if the number of grids and columns aren't equal?
#           * Once located, we have to determine whether the cell should be dead or alive in the next iteration
#           ? How do we configure the initial state, when the game first starts. 
#           ? Do we assume that all of the cells are dead/alive? 
#           ? Or do we use use a random function to determine the initial state of each cell? 
#           ? Does this even matter in the first place?