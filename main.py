def fitness(chromosome):
    b1, b2, b3, b4, b5 = map(int, list(chromosome))
    and_result = 1 if b1 == b2 == b3 == b4 == b5 == 1 else 0
    return b1 + b2 + b3 + b4 + b5 + and_result

chromosomes = ["00101", "11101", "00000", "10010", "11111"]
population_fitness = sum([fitness(chromosome) for chromosome in chromosomes])

for chromosome in chromosomes:
    fitness_value = fitness(chromosome)
    fitness_ratio = fitness_value / population_fitness
    print(f"{chromosome}: fitness = {fitness_value}, fitness ratio% = {fitness_ratio:.2f}")
def crossover(chromosome1, chromosome2, point):
    offspring1 = chromosome1[:point] + chromosome2[point:]
    offspring2 = chromosome2[:point] + chromosome1[point:]
    return offspring1, offspring2

chromosome1 = "10010"
chromosome2 = "11111"
crossover_point = 2
offspring1, offspring2 = crossover(chromosome1, chromosome2, crossover_point)
print(f"Offspring1: {offspring1}")
print(f"Offspring2: {offspring2}")
def mutation(chromosome, point1, point2):
    chromosome_list = list(chromosome)
    chromosome_list[point1], chromosome_list[point2] = chromosome_list[point2], chromosome_list[point1]
    return "".join(chromosome_list)

chromosomes = ["00101", "11101", "10010"]
mutation_points = [(2,3), (2,3), (2,3)]
for i in range(len(chromosomes)):
    mutated_chromosome = mutation(chromosomes[i], mutation_points[i][0], mutation_points[i][1])
    print(f"{chromosomes[i]}: Mutation = {mutated_chromosome}")
