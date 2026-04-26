"""
Pivot de Gauss 
Système :  2x + y - z = 8
          -3x - y + 2z = -11
          -2x + y + 2z = -3
"""

# ── Le tableau (matrice augmentée) ──────────
M = [
    [ 2.0,  1.0, -1.0,  8.0],
    [-3.0, -1.0,  2.0, -11.0],
    [-2.0,  1.0,  2.0, -3.0],
]

def afficher(M, titre):
    print(f"\n{titre}")
    for row in M:
        print("  ", [round(v, 4) for v in row])

afficher(M, "Tableau initial :")

# ── Étape 1 : éliminer x des lignes 2 et 3 ──
f2 = M[1][0] / M[0][0]   # -3 / 2 = -1.5
f3 = M[2][0] / M[0][0]   # -2 / 2 = -1.0

for j in range(4):
    M[1][j] -= f2 * M[0][j]
    M[2][j] -= f3 * M[0][j]

afficher(M, "Après étape 1 (x éliminé) :")

# ── Étape 2 : éliminer y de la ligne 3 ──────
f3b = M[2][1] / M[1][1]  # 2 / 0.5 = 4

for j in range(4):
    M[2][j] -= f3b * M[1][j]

afficher(M, "Après étape 2 (y éliminé) :")

# ── Étape 3 : remontée ───────────────────────
z = M[2][3] / M[2][2]
y = (M[1][3] - M[1][2] * z) / M[1][1]
x = (M[0][3] - M[0][1] * y - M[0][2] * z) / M[0][0]

print(f"\nSolution :")
print(f"  x = {x}")
print(f"  y = {y}")
print(f"  z = {z}")

# ── Vérification ─────────────────────────────
print("\nVérification :")
print(f"  2x + y - z   = {2*x + y - z}   (attendu : 8)")
print(f"  -3x - y + 2z = {-3*x - y + 2*z}  (attendu : -11)")
print(f"  -2x + y + 2z = {-2*x + y + 2*z}   (attendu : -3)")