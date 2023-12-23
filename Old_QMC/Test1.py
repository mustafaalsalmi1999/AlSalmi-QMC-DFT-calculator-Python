import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla
# Construct the Hamiltonian matrix for a simple quantum system (e.g., a spin chain)
H = sp.csr_matrix([[-1, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 1]])
beta = 10  # Inverse temperature
n_walkers = 100  # Number of walkers
n_steps = 1000  # Number of Monte Carlo steps
walkers = np.random.randint(0, 3, size=(n_walkers, 1))  # Random initial positions
for step in range(n_steps):
    for i in range(n_walkers):
        # Propose a new position for the walker
        new_pos = np.random.randint(0, 3)

        # Calculate the energy difference
        delta_E = H[new_pos, new_pos] - H[walkers[i, 0], walkers[i, 0]]

        # Accept or reject the move based on the Metropolis criterion
        if np.random.rand() < np.exp(-beta * delta_E):
            walkers[i, 0] = new_pos

# Compute the energy expectation value
energy = np.mean(H[walkers[:, 0], walkers[:, 0]])

# Compute other observables as needed (e.g., magnetization)


