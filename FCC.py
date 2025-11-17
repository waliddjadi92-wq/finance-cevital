import streamlit as st
import pandas as pd

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Calculateur de ratios financiers SCF", layout="wide")
st.title("Calculateur de Ratios Financiers (SCF – Algérie)")
st.markdown("""
Application simplifiée pour calculer automatiquement les **ratios financiers essentiels** selon les postes du **SCF** :
- **EBITDA**
- **ROE (Rentabilité des capitaux propres)**
- **Leverage (Effet de levier)**
- **CAF – Capacité d'autofinancement**

> *Version entièrement en français.*
""")

# --- SAISIE DES DONNÉES SELON SCF ---
st.header("Données financières (SCF)")
col1, col2 = st.columns(2)

with col1:
    chiffre_affaires = st.number_input("Chiffre d'affaires (Ventes)", min_value=0.0, step=100.0)
    achats = st.number_input("Achats consommés", min_value=0.0, step=100.0)
    charges_personnel = st.number_input("Charges de personnel", min_value=0.0, step=100.0)
    impots_taxes = st.number_input("Impôts et taxes", min_value=0.0, step=100.0)
    dotations = st.number_input("Dotations aux amortissements et provisions", min_value=0.0, step=100.0)

with col2:
    resultat_net = st.number_input("Résultat net", min_value=0.0, step=100.0)
    capitaux_propres = st.number_input("Capitaux propres", min_value=0.0, step=100.0)
    total_passif = st.number_input("Total du passif", min_value=0.0, step=100.0)
    reprises = st.number_input("Reprises sur amortissements / provisions", min_value=0.0, step=100.0)
    autres_charges = st.number_input("Autres charges d'exploitation", min_value=0.0, step=100.0)

# --- CALCUL DES RATIOS ---
def safe_div(a, b):
    return a / b if b != 0 else None

# EBITDA = Résultat d'exploitation + Dotations – Reprises
resultat_exploitation = chiffre_affaires - achats - charges_personnel - impots_taxes - autres_charges
EBITDA = resultat_exploitation + dotations - reprises

ROE = safe_div(resultat_net, capitaux_propres)
Leverage = safe_div(total_passif, capitaux_propres)
CAF = resultat_net + dotations - reprises

# --- AFFICHAGE ---
st.header("Résultats des Ratios")
ratios = {
    "EBITDA": f"{EBITDA:,.2f} DA" if EBITDA is not None else "—",
    "ROE (Rentabilité des CP)": f"{ROE*100:.2f}%" if ROE else "—",
    "Leverage (Effet de levier)": f"{Leverage:.2f}" if Leverage else "—",
    "CAF (Capacité d'autofinancement)": f"{CAF:,.2f} DA" if CAF is not None else "—",
}

st.table(pd.DataFrame.from_dict(ratios, orient='index', columns=["Valeur"]))


