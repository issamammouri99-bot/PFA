import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. Charger dataset réel
# =========================
# Exemple : dataset CSV (tu peux le télécharger en ligne)
# ici on simule un chargement
data = pd.read_csv(r"C:\Users\SAMSUNG\Downloads\Housing.csv")

# afficher les premières lignes
print(data.head())

# =========================
# 2. Séparer X et y
# =========================
# y = prix
y = data["price"].values

# X = autres variables
X = data.drop("price", axis=1).values

# =========================
# 3. Normalisation
# =========================
def normaliser(X):
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    
    sigma[sigma == 0] = 1
    X_norm = (X - mu) / sigma
    
    return X_norm, mu, sigma

X_norm, mu, sigma = normaliser(X)

# ajout biais
m = X_norm.shape[0]
X_norm = np.c_[np.ones(m), X_norm]

# =========================
# 4. Matrices normales
# =========================
A = X_norm.T @ X_norm
b = X_norm.T @ y

# =========================
# 5. Gauss-Seidel
# =========================
def gauss_seidel(A, b, tol=1e-6, max_iter=1000):
    n = len(b)
    beta = np.zeros(n)

    for k in range(max_iter):
        beta_old = beta.copy()

        for i in range(n):
            s1 = sum(A[i][j] * beta[j] for j in range(i))
            s2 = sum(A[i][j] * beta_old[j] for j in range(i+1, n))

            beta[i] = (b[i] - s1 - s2) / A[i][i]

        if np.linalg.norm(beta - beta_old) < tol:
            print(f"Convergence en {k} itérations")
            break

    return beta

beta = gauss_seidel(A, b)

# =========================
# 6. Prédiction
# =========================
y_pred = X_norm @ beta

# =========================
# 7. Évaluation
# =========================
mse = np.mean((y - y_pred) ** 2)
print("MSE:", mse)

# =========================
# 8. Visualisation
# =========================
plt.scatter(y, y_pred)
plt.xlabel("Valeurs réelles")
plt.ylabel("Valeurs prédites")
plt.title("Régression avec Gauss-Seidel (Dataset réel)")
plt.show()