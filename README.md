# Automatisation des Ventes

A Python CLI tool for sales data entry, computation, CSV export, and chart generation.

---

## Features

- Interactive CLI for entering product sales data
- Automatic calculation of gross revenue, net revenue, and VAT
- Identification of the best-performing product
- Export of raw and computed data to CSV files
- Bar chart and pie chart generation with Matplotlib

---

## Requirements

- Python 3.7+
- Matplotlib

Install the dependency with:

```bash
pip install matplotlib
```

---

## Usage

Run the script from your terminal:

```bash
python ventes.py
```

You will be prompted to:
1. Enter the number of products to process
2. For each product, provide:
   - **ID** — unique integer identifier
   - **Prix** — unit price (€)
   - **Quantité** — quantity sold
   - **Remise** — discount percentage (0–100)

---

## Calculations

| Metric | Formula |
|---|---|
| CA Brut | `Prix × Quantité` |
| CA Net | `CA Brut × (1 - Remise / 100)` |
| TVA | `CA Net × 20%` |
| CA Total | Sum of all CA Net values |

The product with the highest CA Net is flagged as the most profitable.

---

## Output Files

| File | Description |
|---|---|
| `ventes.csv` | Raw input data (ID, Prix, Quantité, Remise) |
| `resultats_final.csv` | Full results including CA Brut, CA Net, and TVA |
| `graphiques_ventes.png` | Grouped bar chart + pie chart (150 dpi) |

---

## Charts

Two charts are generated side by side:

- **Grouped bar chart** — CA Brut, CA Net, and TVA for each product
- **Pie chart** — share of CA Net per product

Charts are saved as `graphiques_ventes.png` and displayed in a window.

---

## Example Session

```
==================================================
   Automatisation des Ventes - Saisie des données
==================================================

Combien de produits voulez-vous saisir ? 2

--- Produit 1 ---
  ID       : 101
  Prix     : 50.00
  Quantité : 20
  Remise % : 10

--- Produit 2 ---
  ID       : 102
  Prix     : 80.00
  Quantité : 15
  Remise % : 0

=======================================================
ID       CA Brut     CA Net        TVA
-------------------------------------------------------
101      1000.00      900.00     180.00
102      1200.00     1200.00     240.00
=======================================================

 CA Total de l'entreprise : 2100.00 €
 Produit le plus rentable  : ID 102 (CA Net = 1200.00 €)
```

- If Matplotlib is not installed, the script skips chart generation and prints a warning.
- All monetary values are rounded to 2 decimal places.
- VAT rate is fixed at 20% and defined as a constant (`TVA_RATE = 0.20`).
