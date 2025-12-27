import numpy as np
import matplotlib.pyplot as plt

def simulated_annealing(func, start, temp, alpha, iterations):
    x = start
    best_x = x

    for i in range(iterations):
        # Générer une nouvelle solution dans le voisinage
        new_x = x + np.random.uniform(-1, 1)

        # Calcul de la variation de la fonction objectif
        delta_e = func(new_x) - func(x)

        # Critère d’acceptation (Metropolis)
        if delta_e < 0 or np.random.rand() < np.exp(-delta_e / temp):
            x = new_x

            # Mise à jour de la meilleure solution trouvée
            if func(x) < func(best_x):
                best_x = x

        # Refroidissement
        temp *= alpha

    return best_x

# Fonction objectif
def func(x):
    return np.cos(x) + 0.05 * x**2

# Paramètres
start = 6              # Point de départ
temp = 100.0           # Température initiale
alpha = 0.99           # Facteur de refroidissement
iterations = 1000      # Nombre d’itérations

# Exécution du recuit simulé
best_x = simulated_annealing(func, start, temp, alpha, iterations)

print("Global minimum found at x =", best_x)
print("Function value at global minimum =", func(best_x))

# Tracé de la fonction
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = func(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='cos(x) + 0.05 * x^2')
plt.scatter(best_x, func(best_x), color='red', label='Global Minimum', zorder=5)
plt.title("Simulated Annealing on cos(x) + 0.05 * x^2")
plt.xlabel("x")
plt.ylabel("cos(x) + 0.05 * x^2")
plt.legend()
plt.grid()
plt.show()
