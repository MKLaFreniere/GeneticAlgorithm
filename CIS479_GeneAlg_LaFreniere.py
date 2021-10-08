# Mark LaFreniere
# Creation: 6/4/2021
# Modified: 6/5/2021
# Problem solved with a genetic algorithm

import random

items = [['Sleeping Bag', 15, 15], ['Rope', 3, 7], ['Pocket Knife', 2, 10], ['Flashlight', 5, 5], 
         ['Bottle', 9, 8], ['Sugar Candy', 20, 17], ['Lighter', 1, 10], ['GPS', 5, 13], 
         ['Tent', 15, 20], ['Whistle', 4, 2]]

population = ['1001001010', '0001000110', '0001101100', '0001111011', '1100111110', '1011110001', '0110100001', '1011011010', '1100110111', 
'1010100100', '0111010110', '1100000000', '0001011001', '0101000110', '1010101001', '0010001001', '0110100011', 
'1101100001', '1000010001', '0111010011']

generation = 1

# Each Generation
for i in range(30):
    # Reset needed lists in each generation
    best20 = []
    children = []
    acceptedPop = []
    newPop = []
    points = []
    sortedPop = []
    finalPop = []

    # Find acceptable members of the population for first generation
    if i == 0:
        for solution in population:
            weight = 0
            count = 0
            for i in solution:
                if i == '1':
                    weight += items[count][1]
                count = count + 1
            if weight <= 30:
                acceptedPop.append(solution)
    else:
        acceptedPop = population

    # Crossover rate of 70%, else no mating
    if random.randint(0,100) <= 70:
        for j in range(7):
            # Pick random parents to mate
            parent1se = random.randint(0,len(acceptedPop) - 1)
            parent2se = parent1se
            while parent2se == parent1se:
                parent2se = random.randint(0,len(acceptedPop) - 1)
            parent1 = acceptedPop[parent1se]
            parent2 = acceptedPop[parent2se]
            # Find a random crossover point and parse strings
            crossover = random.randint(1,9)
            child1 = parent1[0:crossover] + parent2[crossover:10]
            child2 = parent2[0:crossover] + parent1[crossover:10]
            children.append(child1)
            children.append(child2)
        # Add children to the population
        newPop = acceptedPop + children
    else:
        newPop = acceptedPop
    
    # Mutate the new population, 1% chance for each bit
    for solution in newPop:
        for i in solution:
            if random.randint(0,100) == 1:
                if i == '0':
                    i = '1'
                else:
                    i = '0'

    # Find Fitnesses
    for solution in newPop:
        point = 0
        count = 0
        for i in solution:
            if i == '1':
                point += items[count][2]
            count = count + 1
        points.append(point)

    # Sort List by descending points
    sortedPop = [newPop for _, newPop in sorted(zip(points,newPop))]
    sortedPop.reverse()

    # Get rid of bad weights early to make sorting easier later
    for solution in sortedPop:
        weight = 0
        count = 0
        for i in solution:
            if i == '1':
                weight += items[count][1]
            count = count + 1
        if weight <= 30:
            finalPop.append(solution)

    # Find best top 20
    while len(finalPop) > 20:
        finalPop.pop()

    # Make the sorted best 20 the new population
    population = finalPop

    # Find and Display generational info
    sum = 0
    for k in points:
        sum += k
    average = sum/len(points)
    print("Top answer for generation %(M)d: %(S)s \n Average fitness: %(A)d \n"%{'M':generation, 'S':population[0], 'A':average})

    # Find out if generations should stop or continue, decided if the average fitness equals the greatest fitness
    count = 0
    point = 0
    for i in population[0]:
        if i == '1':
            point += items[count][2]
        count = count + 1
    if point == average:
        print("*Early end due to lack of progress*\n")
        break
    else:
        generation += 1

# Find and Display final results
finalPoints = []
answerPop = [population[0], population[1], population[2], population[3]]
iter = 1
for answer in answerPop:
        item = []
        point = 0
        weight = 0
        count = 0
        for i in answer:
            if i == '1':
                point += items[count][2]
                weight += items[count][1]
                item.append(items[count][0])
            count = count + 1
        print("Answer #%(A)d: %(B)s, Weight: %(D)d, Fitness: %(C)d "%{'A':iter, 'B':population[iter - 1], 'C':point, 'D':weight})
        for i in item:
            print("  ", i)
        iter += 1