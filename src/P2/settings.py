# BACKTRACKING:

# maximum number of queens on the board. Will also affect board size
QUEEN_COUNT = 8

# if true, will visualize the backtracking process
# WARNING: This will drastically slow down the execution
SHOW_PROCESS = False

# GENETICS:

# one in X cases will mutate
MUTATION_CHANCE = 100

# iterations til end
ITERATION_COUNT = 100

# size of Population
POPULATION_SIZE = 500

# size of guaranteed crossover per parent (0-4)
GUARANTEED_CROSSOVER = 1

# maximum mutations of a single child
MUTATION_COUNT = 1

# if true, after reproduction, child and parents will be compared. The best individual will be added to new population
# WARNING: This will drastically increase the chance to end in a local maximum
DOUBLE_CHECK = True