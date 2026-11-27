import csv

def charger_donnees(chemin):
    """Lit le CSV et renvoie une liste de dictionnaires."""
    with open(chemin, newline="") as f:
        return list(csv.DictReader(f))

def prix_moyen(maisons):
    """Calcule le prix moyen des maisons."""
    prix = [float(m["prix"]) for m in maisons]
    return sum(prix) / len(prix)

def prix_par_m2(maisons):
    """le prix moyen au m2 (pour chaque maison, prix / surface_m2 , puis
la moyenne)"""
    prix_m2 = [float(m["prix"]) / float(m["surface_m2"]) for m in maisons]
    return sum(prix_m2) / len(prix_m2)

def prix_min(maisons):
    """le prix minimum"""
    prix = [float(m["prix"]) for m in maisons] 
    return min(prix)

def prix_max(maisons):
    """le prix maximum"""
    prix = [float(m["prix"]) for m in maisons] 
    return max(prix)

if __name__ == "__main__":
    maisons = charger_donnees("data/maisons.csv")
    print(f"Nombre de maisons : {len(maisons)}")
    print(f"Prix moyen : {prix_moyen(maisons):.0f}")
    print(f"Prix au m2 moyen : {prix_par_m2(maisons):.0f}")
    print(f"Prix minimum : {prix_min(maisons):.0f}")
    print(f"Prix maximum : {prix_max(maisons):.0f}")