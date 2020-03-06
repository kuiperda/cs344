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

cancer = BayesNet([
    ('Cancer', '', .01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}), 
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
])

#P(Cancer | positive results on both tests)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
#P(Cancer | a positive result on test 1, but a negative result on test 2)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())


#The results seem a bit odd to me; if both tests are positive, apparently that's still only 17% chance of having cancer? 
#   seems like it's because the chance of cancer is very low (1% of the time) but there is still a decent chance that the test is positive anyway (20% of the time!)
#The effect of having one failed test out of two is quite large, dropping the probability to 0.5% of having cancer.

#By hand: (answer is < +C, -C >)

#P(C | t1 /\ t2) = @ * P(C) * P(t1 | C) * P(t2 | C)
# = @ * < (0.01 * 0.9 * 0.9), (0.99 * 0.2 * 0.2) >
# = @ * < 0.0081, 0.0396 >
# @ = 0.0477
# = < 0.17 , 0.83>

#P(C | t1 /\ -t2) = @ * P(C) * P(t1 | C) * P(-t2 | C)
# = @ * < (0.01 * 0.9 * 0.1), (0.99 * 0.2 * 0.9) >
# = @ * < 0.0009, 0.1782 >
# @ = 0.1791
# = < 0.005, 0.995>
