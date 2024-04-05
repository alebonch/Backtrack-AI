# Backtrack-MAC
Project for Artificial Intelligence Exam @ Unifi - Backtracking Algorithm implementation and application to the Job Scheduling Problem.
##  What it does
In this repository you will find a backtracking algorithm implementation and its application to solve the job scheduling problem found in §6.1.2 R&N 2021. The solver works recursively to find variables that satisfy the constraints that are given. To accellerate the process, after finding a suitable variable, the program reduces the domain of the other variables using the constraints to reduce the number of values that it needs to check using the Maintaining Arc Consistency approach. After finding the solutions, the program prints out the best solutions, which are the ones that minimize the maximum value of each solution.
## Files
- **Backtrackjobscheduling.py** Main file, which contains both the class that works as the solver and the **main()** function.
- **prob1.py** First instance of the problem, exaclty the one found at §6.1.2 R&N 2021
- **prob2.py** and **prob3.py** are both randomly generated problems
## How to run
The program, given an input beetween: '1','2' and '3' to choose which of the given problems we want to resolve. The program also needs an input to decide how many solutions we need to calculate. To make the program calculate all the solutions, this number just needs to be either 0 or any negative number. 

It is also possible to create a new problem, by creating correctly the variables and constraints: 
- A single hash table to represent variables and their domains, using the variables as keys which lead to their domains.
- A double hash table to represent the constraints. Each variable has to be represented in the first key set. For each constraint we want to add, we will need to insert a coinstraint in the form:

> hashtable[var1][var2]=(value, typeofconstraint)

You can check the types of constraint in the  **check_constraint()** method of the **Backtrackjobscheduling.py** file. You can also add other constraints, but you will also have to adjust the **removeDomains()** method to be sure that inferences are correct.

No special libraries are required to run the program.
