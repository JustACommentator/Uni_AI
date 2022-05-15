import pygame.display

import genetics as gen
import settings
import board


population = gen.populate()
fitnesses = []
for chromosome in population:
    fitnesses.append(gen.fitnessScore(chromosome))
avg1 = round(sum(fitnesses)/len(fitnesses), 2)
maxFitness = 0

for i in range(settings.ITERATION_COUNT):
    print(f"Generation {i + 1}:")
    population = gen.geneticAlgorithm(population)
    fitnesses = []
    for chromosome in population:
        fitnesses.append(gen.fitnessScore(chromosome))
    maxFitness = max(fitnesses)
    avg2 = round(sum(fitnesses)/settings.POPULATION_SIZE, 2)
    print(f"Best specimen: {population[fitnesses.index(maxFitness)]}. Fitness score: {maxFitness}. Average: {avg2}")
    pygame.display.set_caption(f"Population: {settings.POPULATION_SIZE}; Generation: {i + 1}; Score: {maxFitness}; Average: {avg2}")
    board.update(population[fitnesses.index(maxFitness)])
    if maxFitness == 28:
        break

print("-----------------------------------------------------------------------------------------")

print(f"Best specimen in final generation with {settings.POPULATION_SIZE} specimen per generation:")
print(population[fitnesses.index(maxFitness)])
print(f"Fitness score: {maxFitness}")

increase = avg2 / avg1
print(f"Initial average score: {avg1}. Final average score: {avg2}. Change: {round(abs((avg2/avg1)-1)*100, 2)}%")

input()
