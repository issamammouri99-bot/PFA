import csv
import matplotlib.pyplot as plt 

# ─────────────────────────────────────────
# 1. Saisie des données par l'utilisateur
# ─────────────────────────────────────────

print("=" * 50)
print("   Automatisation des Ventes - Saisie des données")
print("=" * 50)

ventes_data = []

while True:
    try:
        n = int(input("\nCombien de produits voulez-vous saisir ? "))
        if n <= 0:
            print("  Veuillez entrer un nombre positif.")
        else:
            break
    except ValueError:
        print("  Veuillez entrer un nombre entier valide.")

print()
for i in range(n):
    print(f"--- Produit {i + 1} ---")
    while True:
        try:
            id_produit = int(input("  ID       : "))
            break
        except ValueError:
            print("  ID invalide, entrez un entier.")

    while True:
        try:
            prix = float(input("  Prix     : "))
            if prix < 0:
                print("Le prix ne peut pas être négatif.")
            else:
                break
        except ValueError:
            print("Prix invalide, entrez un nombre.")

    while True:
        try:
            quantite = int(input("  Quantité : "))
            if quantite < 0:
                print("    La quantité ne peut pas être négative.")
            else:
                break
        except ValueError:
            print("    Quantité invalide, entrez un entier.")

    while True:
        try:
            remise = float(input("  Remise % : "))
            if not (0 <= remise <= 100):
                print("    La remise doit être entre 0 et 100.")
            else:
                break
        except ValueError:
            print("    Remise invalide, entrez un nombre.")

    ventes_data.append({
        "ID": id_produit,
        "Prix": prix,
        "Quantite": quantite,
        "Remise": remise
    })

# ─────────────────────────────────────────
# Écriture du fichier ventes.csv
# ─────────────────────────────────────────

ventes_file = "ventes.csv"
with open(ventes_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["ID", "Prix", "Quantite", "Remise"])
    writer.writeheader()
    writer.writerows(ventes_data)

print(f"\n Fichier '{ventes_file}' généré avec succès.\n")

# ─────────────────────────────────────────
# 2-6. Calculs
# ─────────────────────────────────────────

TVA_RATE = 0.20
resultats = []
ca_total = 0.0
meilleur_id = None
meilleur_ca_net = 0.0

with open(ventes_file, mode="r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        id_produit = int(row["ID"])
        prix       = float(row["Prix"])
        quantite   = int(row["Quantite"])
        remise     = float(row["Remise"])

        # 2. CA Brut
        ca_brut = prix * quantite

        # 3. CA Net
        ca_net = ca_brut * (1 - remise / 100)

        # 4. TVA
        tva = ca_net * TVA_RATE

        # 5. CA Total
        ca_total += ca_net

        # 6. Meilleur produit
        if ca_net > meilleur_ca_net:
            meilleur_ca_net = ca_net
            meilleur_id = id_produit

        resultats.append({
            "ID":       id_produit,
            "Prix":     prix,
            "Quantite": quantite,
            "Remise":   remise,
            "CA_Brut":  round(ca_brut, 2),
            "CA_Net":   round(ca_net,  2),
            "TVA":      round(tva,     2),
        })

# ─── Affichage ────────────────────────────
print("=" * 55)
print(f"{'ID':<8} {'CA Brut':>10} {'CA Net':>10} {'TVA':>10}")
print("-" * 55)
for r in resultats:
    print(f"{r['ID']:<8} {r['CA_Brut']:>10.2f} {r['CA_Net']:>10.2f} {r['TVA']:>10.2f}")
print("=" * 55)

print(f"\n CA Total de l'entreprise : {ca_total:.2f} €")
print(f" Produit le plus rentable  : ID {meilleur_id} (CA Net = {meilleur_ca_net:.2f} €)\n")

# ─────────────────────────────────────────
# 7. Export resultats_final.csv
# ─────────────────────────────────────────

resultats_file = "resultats_final.csv"
fieldnames = ["ID", "Prix", "Quantite", "Remise", "CA_Brut", "CA_Net", "TVA"]

with open(resultats_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(resultats)

print(f" Fichier '{resultats_file}' exporté avec succès.\n")

# ─────────────────────────────────────────
# Graphiques Matplotlib
# ─────────────────────────────────────────

try:
    import matplotlib.pyplot as plt

    ids   = [str(r["ID"])  for r in resultats]
    bruts = [r["CA_Brut"]  for r in resultats]
    nets  = [r["CA_Net"]   for r in resultats]
    tvas  = [r["TVA"]      for r in resultats]

    x     = range(len(ids))
    width = 0.25

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("Analyse des Ventes par Produit", fontsize=14, fontweight="bold")

    # Barres groupées
    ax1 = axes[0]
    ax1.bar([i - width for i in x], bruts, width, label="CA Brut",   color="#4C72B0")
    ax1.bar([i         for i in x], nets,  width, label="CA Net",    color="#55A868")
    ax1.bar([i + width for i in x], tvas,  width, label="TVA (20%)", color="#C44E52")
    ax1.set_xticks(list(x))
    ax1.set_xticklabels([f"ID {i}" for i in ids])
    ax1.set_ylabel("Montant (€)")
    ax1.set_title("CA Brut / CA Net / TVA par produit")
    ax1.legend()
    ax1.grid(axis="y", linestyle="--", alpha=0.5)

    # Camembert
    ax2 = axes[1]
    ax2.pie(nets, labels=[f"ID {i}" for i in ids], autopct="%1.1f%%",
            startangle=140, colors=plt.cm.Paired.colors)
    ax2.set_title("Répartition du CA Net par produit")

    plt.tight_layout()
    plt.savefig("graphiques_ventes.png", dpi=150)
    plt.show()
    print(" Graphiques sauvegardés dans 'graphiques_ventes.png'.")

except ImportError:
    print("  Matplotlib non installé — graphiques ignorés.")
    print("   Installez-le avec : pip install matplotlib")