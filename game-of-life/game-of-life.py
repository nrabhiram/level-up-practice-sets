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
#           * Once located, we have to determine whether the cell should be dead or alive in the next iteration
#           ? How do we configure the initial state, when the game first starts. 
#           ? Do we assume that all of the cells are dead/alive? 
#           ? Or do we use use a random function to determine the initial state of each cell? 
#           ? Does this even matter in the first place?