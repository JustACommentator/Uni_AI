import queens_problem as q
import settings
import numpy
import random


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


def doubleCheck(child, parent1, parent2):
    if fitnessScore(child) > fitnessScore(parent1) and fitnessScore(child) > fitnessScore(parent2):
        return child
    elif fitnessScore(parent1) > fitnessScore(child) and fitnessScore(parent1) > fitnessScore(parent2):
        return parent1
    else:
        return parent2


def geneticAlgorithm(population):
    totalFitness = 0
    for chromosome in population:
        totalFitness += fitnessScore(chromosome)
    probabilities = [fitnessScore(chromosome) / totalFitness for chromosome in population]

    newPopulation = []
    for i in range(settings.POPULATION_SIZE):
        parents = selectParents(population, probabilities)
        child = reproduce(*parents)
        if settings.DOUBLE_CHECK:
            child = doubleCheck(child, parents[0], parents[1])
        newPopulation.append(child)
    return newPopulation


def selectParents(population, probabilities):
    return numpy.random.choice(population, 2, p=probabilities)


def reproduce(x, y):
    n = len(x)
    c = random.randint(settings.GUARANTEED_CROSSOVER, n-settings.GUARANTEED_CROSSOVER)
    child = ""
    child += x[0:c]
    child += y[c:n + 1]
    if random.randint(1, settings.MUTATION_CHANCE) == 1:
        child = mutate(child)
    return child


def mutate(child):
    for i in range(settings.MUTATION_COUNT):
        n = random.randint(0, 7)
        child = child[:n] + str(random.randint(1, 8)) + child[n + 1:]
    return child


def populate():
    Q = q.QueensProblem()
    population = []
    for i in range(settings.POPULATION_SIZE):
        Q.randomize()
        population.append(Q.queenString)

    return population