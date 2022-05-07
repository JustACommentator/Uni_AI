import random
import numpy
import board

# one in X cases will mutate
MUTATION_CHANCE = 100

# iterations til end
ITERATION_COUNT = 100

# size of Population
POPULATION_SIZE = 100

# size of guaranteed crossover per parent (0-4)
GUARANTEED_CROSSOVER = 0


class QueensProblem:

    def __init__(self):
        self.queenString = ""

    def set(self, queenString):
        self.queenString = queenString

    def randomize(self):
        self.queenString = ""
        for i in range(8):
            self.queenString += str(random.randint(1, 8))

    def print(self):
        for i in range(8):
            for k in range(8):
                if int(self.queenString[k]) == i + 1:
                    print("Q  ", end="")
                else:
                    print(".  ", end="")
            print("")


def fitnessScore(chromosome):  # using number of non-attacking pairs of queens as fitness score. Optimal: 28
    score = 0

    for x1 in range(8):
        y = int(chromosome[x1])

        for x2 in range(8):

            if x2 == x1:
                continue
            if int(chromosome[x2]) == y:
                continue
            if x2 + int(chromosome[x2]) == x1 + y:
                continue
            if x2 - int(chromosome[x2]) == x1 - y:
                continue
            score += 1

    return int(score / 2)  # each queen is counted twice per pair


def geneticAlgorithm(population):
    totalFitness = 0
    for chromosome in population:
        totalFitness += fitnessScore(chromosome)
    probabilities = [fitnessScore(chromosome) / totalFitness for chromosome in population]

    newPopulation = []
    for i in range(POPULATION_SIZE):
        parents = selectParents(population, probabilities)
        child = reproduce(*parents)
        newPopulation.append(child)
    return newPopulation


def selectParents(population, probabilities):
    return numpy.random.choice(population, 2, p=probabilities)


def reproduce(x, y):
    n = len(x)
    c = random.randint(GUARANTEED_CROSSOVER, n-GUARANTEED_CROSSOVER)
    child = ""
    child += x[0:c]
    child += y[c:n + 1]
    if random.randint(1, MUTATION_CHANCE) == 1:
        child = mutate(child)
    return child


def mutate(child):
    n = random.randint(0, 7)
    child = child[:n] + str(random.randint(1, 8)) + child[n + 1:]
    return child


def populate():
    Q = QueensProblem()
    population = []
    for i in range(POPULATION_SIZE):
        Q.randomize()
        population.append(Q.queenString)

    return population


population= populate()
fitnesses = []
for chromosome in population:
    fitnesses.append(fitnessScore(chromosome))
avg1 = sum(fitnesses)/len(fitnesses)
maxFitness = 0

for i in range(ITERATION_COUNT):
    print(f"Generation {i + 1}:")
    population = geneticAlgorithm(population)
    fitnesses = []
    for chromosome in population:
        fitnesses.append(fitnessScore(chromosome))
    maxFitness = max(fitnesses)
    print(f"Best specimen: {population[fitnesses.index(maxFitness)]}. Fitness score: {maxFitness}. Average: {sum(fitnesses)/POPULATION_SIZE}")
    board.update(population[fitnesses.index(maxFitness)])
    if maxFitness == 28:
        break

print("-----------------------------------------------------------------------------------------")

print(f"Best specimen in final generation with {POPULATION_SIZE} specimen per generation:")
print(population[fitnesses.index(maxFitness)])
print(f"Fitness score: {maxFitness}")

avg2 = sum(fitnesses)/POPULATION_SIZE
increase = avg2 / avg1
print(f"Initial average score: {avg1}. Final average score: {avg2}. Change: {round(abs((avg2/avg1)-1)*100, 2)}%")

while True:
    True