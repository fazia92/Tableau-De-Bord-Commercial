import pandas as pd
import random
from faker import Faker

fake = Faker("fr_FR")
Faker.seed(42)
random.seed(42)

# ----------------------
# 1. TABLE PRODUIT
# ----------------------
produits = []
prix_map = {"25": 800, "50": 1200, "100": 2200}
noms_produits = ["DiabetoCheck", "GlucoTest", "GlucoStrip"]

id_counter = 1
for nom in noms_produits:
    for boite in ["25", "50", "100"]:
        produits.append({
            "id_produit": f"P{id_counter:03d}",
            "nom_produit": nom,
            "type_boite": f"Bandelette {boite}",
            "prix_unitaire": prix_map[boite]
        })
        id_counter += 1

df_produit = pd.DataFrame(produits)

# ----------------------
# 2. TABLE CLIENT
# ----------------------
clients = []
categories = ["Pharmacie", "Hôpital", "Grossiste"]

for i in range(1, 201):  # 200 clients
    clients.append({
        "id_client": f"C{i:03d}",
        "nom_client": fake.company(),
        "categorie": random.choice(categories)
    })

df_client = pd.DataFrame(clients)

# ----------------------
# 3. TABLE WILAYA (58)
# ----------------------
wilayas_list = [
    "Adrar","Chlef","Laghouat","Oum El Bouaghi","Batna","Béjaïa","Biskra","Béchar","Blida","Bouira",
    "Tamanrasset","Tébessa","Tlemcen","Tiaret","Tizi Ouzou","Alger","Djelfa","Jijel","Sétif","Saïda",
    "Skikda","Sidi Bel Abbès","Annaba","Guelma","Constantine","Médéa","Mostaganem","MSila","Mascara",
    "Ouargla","Oran","El Bayadh","Illizi","Bordj Bou Arreridj","Boumerdès","El Tarf","Tindouf","Tissemsilt",
    "El Oued","Khenchela","Souk Ahras","Tipaza","Mila","Aïn Defla","Naâma","Aïn Témouchent","Ghardaïa",
    "Relizane","El M'ghair","El Meniaa","Ouled Djellal","Bordj Baji Mokhtar","Béni Abbès","Timimoun",
    "Touggourt","Djanet","In Salah","In Guezzam"
]

wilayas = []
for i, nom in enumerate(wilayas_list, start=1):
    wilayas.append({
        "id_wilaya": f"W{i:03d}",
        "num_wilaya": i,
        "nom_wilaya": nom
    })

df_wilaya = pd.DataFrame(wilayas)

# ----------------------
# 4. TABLE VENTE
# ----------------------
ventes = []
canaux = ["Direct", "Distributeur"]

for i in range(1, 5001):  # 5000 transactions
    produit = random.choice(produits)
    client = random.choice(clients)
    wilaya = random.choice(wilayas)
    quantite = random.randint(1, 50)

    ventes.append({
        "id_transaction": f"T{i:05d}",
        "date_vente": fake.date_between(start_date="-2y", end_date="today"),
        "id_produit": produit["id_produit"],
        "quantite": quantite,
        "prix_unitaire": produit["prix_unitaire"],
        "id_client": client["id_client"],
        "id_wilaya": wilaya["id_wilaya"],
        "canal": random.choice(canaux)
    })

df_vente = pd.DataFrame(ventes)

# ----------------------
# Sauvegarde CSV
# ----------------------
df_produit.to_csv("table_produit.csv", index=False, encoding="utf-8")
df_client.to_csv("table_client.csv", index=False, encoding="utf-8")
df_wilaya.to_csv("table_wilaya.csv", index=False, encoding="utf-8")
df_vente.to_csv("table_vente.csv", index=False, encoding="utf-8")

print("✅ Fichiers générés : table_produit.csv, table_client.csv, table_wilaya.csv, table_vente.csv")
