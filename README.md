# GeneticAlgorithm

<img src="https://media.cheggcdn.com/media/751/751e31ac-0f93-447d-8ed0-8ecf37991bf8/php31FkEp">
Transcribed image text: <KBD>QUESTION 2</KBd>
 Consider a Genetic Algorithm in which chromosomes are represented using
 a 5-bit string of the form b1b2b3b4b5. An example of a chromosome is 
00101 for which b1=0, b2=0, b3=1, b4=0, 65=1. The fitness function is 
defined over these chromosomes as follows: f(b1b2b3b4b5) = bi + b2 + b3 +
 b4 + b5 + AND (b1,b2,13,14,65), where: AND (b1,b2,63, b4,b5) 1 if 
b1=b2=b3=b4=b5=1; and AND (b1,b2, 53,54,55) = 0 otherwise. Answer the 
following questions. a) Fill in the table below by calculating the 
fitness and the fitness ratio of each individual chromosome. Show each 
step of your work. Chromosome Fitness Fitness Ratio, % Chromosome 00101 
11101 00000 10010 11111 (15 marks) b) Apply crossover on the fourth and 
the fifth chromosomes using single crossover point i.e., between the 
second and the third gene. (2 marks) c) Apply mutation for the first, 
second, and fourth chromosomes by swapping the third and the fourth 
gene. (3 marks)
</br>
consider a genetic algorithm in which individuals are represented  using a 5bit string of the form b1 b2 b3 b4 b5.
an example of chromosome is 00101 for which b1=0 b2=0 b3=1 b4=0 b5=1 
the fitness function is defined over these chromosome as follows:
f(b1b2b3b4b5) = b1+b2+b3+b4+b5+ And(b1,b2,b3,b4,b5)
where:
AND(b1,b2,b3,b4,b5)=1 if b1=b2=b3=b4=b5=1; and 
AND(b1,b2,b3,b4,b5) =0 otherwise
Answer the following questions
a)find the chromosome fitness & fitness ratio% 
for 
00101
11101
00000
10010
11111
b) apply crossover on the fourth and the fifth chromosome using single crossover point between the second and the third gene 
c)apply mutation for the first ,second and fourth chromosome by swapping the third and the fourth gene 
explain your answer 
<p>
a) The fitness and fitness ratio% for the given chromosomes are as follows:

00101: fitness = b1 + b2 + b3 + b4 + b5 + AND(b1,b2,b3,b4,b5) = 0 + 0 + 1 + 0 + 1 + 0 = 2, fitness ratio% = 2/15
11101: fitness = b1 + b2 + b3 + b4 + b5 + AND(b1,b2,b3,b4,b5) = 1 + 1 + 1 + 0 + 1 + 1 = 5, fitness ratio% = 5/15
00000: fitness = b1 + b2 + b3 + b4 + b5 + AND(b1,b2,b3,b4,b5) = 0 + 0 + 0 + 0 + 0 + 0 = 0, fitness ratio% = 0/15
10010: fitness = b1 + b2 + b3 + b4 + b5 + AND(b1,b2,b3,b4,b5) = 1 + 0 + 0 + 1 + 0 + 0 = 2, fitness ratio% = 2/15
11111: fitness = b1 + b2 + b3 + b4 + b5 + AND(b1,b2,b3,b4,b5) = 1 + 1 + 1 + 1 + 1 + 1 = 6, fitness ratio% = 6/15
b) Applying crossover on the fourth and the fifth chromosome using a single crossover point between the second and the third gene:

Fourth chromosome: 10010
Fifth chromosome: 11111
Single crossover point between the second and the third gene:
Offspring1: 10011
Offspring2: 11110
c) Applying mutation for the first, second, and fourth chromosome by swapping the third and fourth gene:

First chromosome: 00101
Mutation: 00110
Second chromosome: 11101
Mutation: 11011
Fourth chromosome: 10010
Mutation: 10100

</p>
