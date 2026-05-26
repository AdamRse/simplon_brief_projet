import pandas as pd
import plotly.express as px

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Ventes par région
figure = px.pie(données, values='qte', names='region', title='Quantité vendue par région')
figure.write_html('ventes-par-region.html')
print('ventes-par-region.html généré avec succès !')

# Page 2 : Ventes par produit
ventes_produit = données.groupby('produit', as_index=False)['qte'].sum()
figure2 = px.pie(ventes_produit, values='qte', names='produit', title='Quantité vendue par produit')
figure2.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré avec succès !')

# Page 3 : Chiffre d'affaires par produit
données['ca'] = données['prix'] * données['qte']
ca_produit = données.groupby('produit', as_index=False)['ca'].sum()
figure3 = px.pie(ca_produit, values='ca', names='produit', title="Chiffre d'affaires par produit")
figure3.write_html('ca-par-produit.html')
print("ca-par-produit.html généré avec succès !")
