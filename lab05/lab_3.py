'''
@author: djk45 
3-6-2020
lab05
'''
import sys
sys.path.append('/home/djk45/cs344/cs344-code/tools/aima/')

from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
])

#P(Raise | sunny)
print(enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())
#P(Raise | happy ∧ sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())

# I'm not sure how you get even 1% chance of a raise when it's sunny. Maybe because your boss is happy?
# Getting a raise is correlated to being happy and sunny, but the chance of a raise is so low and it's possible to be happy even if P(raise) = 0

# By hand:
#P(R | S) = P(RS) / P(S)
# = 0.007 / 0.7
# = 0.01

#P(R | H ∧ S) = @ * P(R) * P(H | R) * P(S | R)
# = @ < 0.01 * ? * 0.7 , 0.99 * -? * 0.3 >
# = < , >
#hm, having trouble getting P(H | R) 
#P(H|R) = P(HR) / P(R) = ... i think P(H) = .55 (multiply all the probabilities, get the avg) 
#P(S|R) = P(SR) / P(R) = .007 / .01 = 0.7


#P(Raise | happy)
print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())
#P(Raise | happy ∧ ¬sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())

#These results are similar to the last one; your happiness doesn't really play into getting you a raise (again the chance of a raise is so small- maybe your boss likes it when you smile though?)
#It makes sense that the second is slightly more likely when it's not sunny because you are still happy despite that; maybe that's because of a raise.