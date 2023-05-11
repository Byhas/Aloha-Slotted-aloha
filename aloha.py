import matplotlib.pyplot as plt
import numpy as np

# Ask the user for the number of users in the network
N = int(input("Enter the number of users in the network: "))

# Create an array of values for p
p_values = np.linspace(0, 1, 101)

# Calculate the efficiency of Aloha for each value of p
efficiency_values = [N * p * (1 - p)**(2 * (N - 1)) for p in p_values]

# Plot the efficiency values
plt.plot(p_values, efficiency_values)
plt.title(f"Aloha Efficiency (N={N})")
plt.xlabel("p")
plt.ylabel("Efficiency")
plt.show()
