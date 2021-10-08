# GeneticAlgorithm
An example of the genetic algorithm I had to make for a project in my AI class

This algorithm solves the knapsack problem, which involves picking a set of 
camping items that best help one survive. Each item has the attributes of weight
and survivability. In order to camp comfortably, the total weight of the items 
brought cannot exceed 30. Because of this little caveat, there are a multitude 
of solutions that can be found by bringing different items. Finding these can be
difficult by hand, but using a genetic algorithm, it can be solved quite quickly 
and reliably. 

For this genetic algorithm used, it was programmed in python due to the ease of 
parsing strings. This is extremely useful when creating children. What’s done first
is the creation of a list that contains the names and attributes for all ten items 
that can be brought. This list contains the following items for this knapsack problem:

Item (Weight, Survival Points)

Sleeping Bag (15, 15)

Rope (3, 7)

Pocket Knife (2, 10)

Flashlight (5, 5)

Bottle (9, 8)

Sugar Candy (20, 17)

Lighter	(1, 10)

GPS (5, 13)

Tent (15, 20)

Whistle	(4, 2)


Next, a population of binary numbers with 10 digits were randomly generated. Each number
in the sequence represents one of the 10 items. 1 means that the item is taken on the 
camping trip, 0 means that it was not taken. With this information cataloged, the start
of the first generation can begin. There can be a maximum of 30 generations in the 
algorithm. How it is decided if the generations should stop will be discussed later.
 
At the beginning of each generation, many lists used are reset to a null statis. If this 
was not done, unnecessary information would leak into a different generation than its own,
which would skew results. After, the randomly generated population is sifted to get rid of 
any solution that has a weight higher than 30. This is done through simple iterations through
the list. 

After a population of only acceptable answers is present, the program decides whether there 
will be a crossover. This has a 70% chance of happening. If it happens, the algorithm choses 
a random pair of parents from the accepted population, then parses their strings on the randomly
generated crossover point. The parsings are combined in 2 ways, creating 2 new strings that are
the children of the 2 parents. This process is done 7 times and all the new children are added 
to the population. 
	
With this new population, the algorithm goes through every bit of every solution and throws a 
dice to see if it that bit should mutate. A mutation consists of changing the value 0 or 1 to 
the opposite value. This has a 1% chance of happening, but as each solution is 10 bits and there
can be as much as 20+ solutions, some mutations are guaranteed to occur. 
	
Next, the algorithm finds the total survival points for each solution, then sorts them in descending
order. Since the order is different, the weights must be calculated again. After this is done the 
algorithm removes and weights above 30 and this section of the generation will be where weights are 
removed in the future, instead of the beginning of each generation. This is just to make it easier 
to find the final answers when the algorithm ends. 
	
Once all the harder work is over, the algorithm finds and displays the top answer of the generation 
and the average fitness of that generation. Lastly, it decides if a new generation should start. This
is decided by seeing if the average fitness is near the same as the greatest fitness. When this is the
case, it usually means that most of the answers that have been generated are the same and will not have
good variation when creating new children. It is also an indication that the algorithm had found a good
answer to the problem, but this is not always the case. 
