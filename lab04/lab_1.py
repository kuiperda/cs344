'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013

Edited: Daniel Kuiper, Feb 28 2020 for Lab04
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC.show_approx())

# Exercise 4.1
# P(Cavity|Catch) by hand:
# P(A|B) = P(AB) / P(B) so P(Cavity|Catch) = P(Cavity AND Catch) / P(Catch)
#
#   P(Cavity AND Catch):
#   P(T,T,T) = .108 and P(F,T,T) = .72
#   so P(*, T, T) = .108 + .072 = 0.18
#
#   P(Catch):
#   Add up all the results where 'Catch' is true (or P(*, *, T))
#   .108 + .072 + .016 + .144 = 0.34
#
#   P(Cavity|Catch): 0.18 / 0.34 = .53

# Compute P(Cavity|Catch) with code
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())
# Prints 0.529 for True, which matches my answer above.

# Joint Probability Distribution for two coins
P = JointProbDist(['Coin1', 'Coin2'])
H, T = 'heads', 'tails'

P[H, H] = 0.25
P[H, T] = 0.25
P[T, H] = 0.25
P[T, T] = 0.25

PC = enumerate_joint_ask('Coin2', {'Coin1': H}, P)
print(PC.show_approx())
# Shows 0.5 for heads and for tails which is how it should be.