"""


@author: djk45
@version 14feb2020
copied (mostly from abs.py)
"""
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class SinVariant(Problem):
    """
    State: x value for the sine function variant f(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """
    
    def __init__(self, initial, maximum=30.0, delta=.0001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta
        
    def actions(self, state):
        return [state + self.delta, state - self.delta]
    
    def result(self, stateIgnored, x):
        return x
    
    def value(self, x):
        return math.fabs(x*math.sin(x))

if __name__ == '__main__':

    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    initial = randrange(0, maximum)
    p = SinVariant(initial, maximum, delta=1.0)
    print('Initial                      x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )

    # Solve the problem using hill-climbing.
    #added random restart
    solutionList = []
    for x in range(100):
        hill_solution = hill_climbing(p)
        solutionList.append(hill_solution)

    print('Hill-climbing solution       x: ' + str(max(solutionList))
          + '\tvalue: ' + str(p.value(max(solutionList)))
          )
    print(sum(solutionList) / len(solutionList))

    # Solve the problem using simulated annealing.
    #added random restart
    solutionList = []
    for x in range(100):
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        solutionList.append(annealing_solution)

    print('Simulated annealing solution x: ' + str(max(solutionList))
          + '\tvalue: ' + str(p.value(max(solutionList)))
          )
    print(sum(solutionList) / len(solutionList))
