import numpy as np
import matplotlib.pyplot as plt

# function to calculate the efficiency of slotted Aloha
def slotted_aloha_efficiency(N, p):
    return N * p * ((1 - p) ** (N - 1))

# get the number of users in the network from user input
N = int(input("Enter the number of users in the network: "))

# generate a list of probabilities between 0 and 1
p_list = np.linspace(0, 1, 100)

# calculate the efficiency of slotted Aloha for each probability
efficiency_list = [slotted_aloha_efficiency(N, p) for p in p_list]

# plot the efficiency as a function of probability
plt.plot(p_list, efficiency_list)
plt.xlabel('Probability of transmission (p)')
plt.ylabel('Efficiency of slotted Aloha')
plt.title(f'Efficiency of slotted Aloha with N={N}')
plt.show()
