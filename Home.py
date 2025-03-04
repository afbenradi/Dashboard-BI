# Home.py
import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Accueil - Dashboard de Turnover", layout="wide")

# Styles CSS personnalisés
st.markdown(
    """
    <style>
    .header {
        background-color: #4CAF50;
        padding: 10px;
        border-radius: 5px;
        color: white;
        text-align: center;
    }
    .section {
        background-color: #f2f2f2;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titre principal avec style
st.markdown("""
    <div class="header">
        <h1>Bienvenue sur le Dashboard: Turnover des Employés ! </h1>
    </div>
    """, unsafe_allow_html=True)

import streamlit as st
import qrcode
from PIL import Image

# URL de ton application Streamlit
url = "https://nom-du-projet.streamlit.app/"

# Générer et sauvegarder le QR Code
qr = qrcode.make(url)
qr.save("qr_code.png")

# Afficher le QR Code sur Streamlit
st.image("qr_code.png", caption="Scannez ce QR Code pour accéder au tableau de bord", use_container_width=True)# Description du projet dans une section stylisée
st.markdown("""
    <div class="section">
        <h2>À propos de ce projet</h2>
        <p>
            Ce <strong>dashboard interactif</strong> a été spécialement conçu pour les <strong>ressources humaines (RH)</strong> afin de 
            <strong>prédire la probabilité qu'un employé quitte l'entreprise</strong>. En utilisant un modèle de régression logistique, ce tableau de bord fournit 
            des <strong>analyses approfondies</strong> et des <strong>visualisations intuitives</strong> pour aider les professionnels RH à 
            <strong>identifier les facteurs clés</strong> influençant le turnover et à <strong>prendre des décisions éclairées</strong> pour réduire 
            le taux de départ des employés.
        </p>
        <h3>Fonctionnalités principales</h3>
        <ul>
            <li><strong>Dashboard KPI</strong> : Accède aux indicateurs clés de performance et visualisations interactives, incluant des métriques telles que le taux de turnover global, la satisfaction moyenne des employés, les heures mensuelles moyennes, ainsi que des visualisations détaillées comme des histogrammes, graphiques en barres, graphiques en secteurs, et des scatter plots dynamiques pour une analyse approfondie du turnover.</li>
            <li><strong>Prédiction de Turnover</strong> : Affiche la probabilité qu'un employé quitte l'entreprise.</li>
            <li><strong>Visualisation des Détails</strong> : Permet de visualiser les caractéristiques spécifiques de l'employé sélectionné.</li>
            <li><strong>Explications SHAP</strong> : Fournit des explications détaillées sur l'impact des différentes caractéristiques (features) sur la prédiction.</li>
            <li><strong>Recommandations</strong> : Affiche des recommandations pour améliorer la rétention des employés.</li>
        </ul>
        <h3>Objectifs du Dashboard</h3>
        <p>
            Ce dashboard vise à fournir une interface utilisateur claire et accessible pour les responsables RH et les analystes de données, 
            facilitant ainsi la prise de décisions informées pour réduire le taux de turnover au sein de l'entreprise. 
            Vous pouvez naviguer vers le Dashboard KPI en utilisant la barre latérale de Streamlit, où vous trouverez des visualisations détaillées et des indicateurs essentiels.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Section des Critères d'Accessibilité d'un Bon Dashboard
st.markdown("""
    <div class="section">
        <h2>Critères d'un Bon Dashboard</h2>
        <p>
            Pour garantir une expérience utilisateur optimale et une accessibilité conforme, ce dashboard respecte les <strong>critères de succès</strong> suivants issus des 
            <a href="https://www.w3.org/Translations/WCAG21-fr/" target="_blank">Web Content Accessibility Guidelines (WCAG) 2.1</a> du W3C :
        </p>
        <ol>
            <li><strong>Critère de succès 1.1.1 Contenu non textuel</strong><br>
                Assurer que tout contenu non textuel dispose d'une alternative textuelle afin que les utilisateurs ayant des déficiences visuelles puissent comprendre l'information.</li>
            <li><strong>Critère de succès 1.4.1 Utilisation de la couleur</strong><br>
                Ne pas utiliser la couleur comme seul moyen de transmettre l'information, permettant ainsi aux utilisateurs daltoniens de naviguer efficacement dans le dashboard.</li>
            <li><strong>Critère de succès 1.4.3 Contraste (minimum)</strong><br>
                Maintenir un contraste suffisant entre le texte et le fond pour garantir une lisibilité optimale, notamment pour les utilisateurs ayant une vision réduite.</li>
            <li><strong>Critère de succès 1.4.4 Redimensionnement du texte</strong><br>
                Permettre aux utilisateurs de redimensionner le texte jusqu'à 200% sans perte de contenu ou de fonctionnalité, facilitant la lecture pour ceux ayant des difficultés visuelles.</li>
            <li><strong>Critère de succès 2.4.2 Titre de page</strong><br>
                Fournir un titre de page unique et descriptif pour chaque page du dashboard, aidant les utilisateurs à comprendre rapidement le contenu et la fonction de chaque section.</li>
        </ol>
        <h3>Importance de ces Critères</h3>
        <p>
            Ces critères sont essentiels pour assurer que le tableau de bord soit accessible à tous les utilisateurs, y compris ceux ayant des handicaps visuels ou cognitifs. 
            En respectant ces directives, nous garantissons une utilisation inclusive et une meilleure expérience utilisateur pour tous.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Bouton pour afficher les Recommandations et Résultats avec style
if st.button("📊 Afficher les Recommandations et Résultats"):
    st.markdown("---")
    st.subheader("📈 Recommandations et Résultats")

    st.markdown("""
    ### 👤 Profil des Collaborateurs qui Quitte l'Entreprise :
    
    - **Satisfaction Faible** :
      Les employés ayant un niveau de satisfaction faible sont plus susceptibles de quitter l'entreprise.
    
    - **Charge de Travail Déséquilibrée** :
      - **Surcharge** : Heures travaillées > 220.
      - **Sous-utilisation** : Heures travaillées < 150.
    
    - **Salaire Bas** :
      Les employés dans les catégories de salaire bas sont majoritairement touchés par le turnover.
    
    - **Postes à Risque** :
      Les départements **Ressources Humaines (HR)** et **Accounting** présentent un taux de turnover plus élevé.
    
    - **Facteurs Spécifiques** :
      Les employés insatisfaits sont plus aptes à quitter l'entreprise.
    
    ### ❓ Pourquoi les Collaborateurs Quittent-ils ?
    
    - **Insatisfaction au Travail** :
      - Faible reconnaissance.
      - Mauvaises conditions de travail.
    
    - **Charge de Travail** :
      - **Surmenage (Burnout)** : Trop d'heures de travail.
      - **Sous-engagement (Désintérêt)** : Trop peu d'heures de travail.
    
    - **Rémunération Insuffisante** :
      - Salaire bas perçu comme non compétitif par rapport au marché.
    
    ### 💡 Comment Améliorer le Turnover
    
    - **Améliorer la Satisfaction** :
      - Équilibrer les charges de travail.
      - Mieux reconnaître et récompenser les efforts des employés.
    
    - **Offrir des Promotions Régulières** :
      - Clarifier les plans de carrière.
      - Fournir des opportunités de développement professionnel.
    
    - **Augmenter la Rémunération** :
      - Aligner les salaires sur le marché.
      - Introduire des primes de performance.
    
    - **Cibler les Postes Critiques** :
      - Offrir des formations spécifiques.
      - Fournir un soutien supplémentaire pour les départements Accounting et RH.
    """)
else:
    st.markdown("""
    ### 📈 Recommandations et Résultats

    Cliquez sur le bouton ci-dessus pour afficher les recommandations et les résultats basés sur l'analyse des données de turnover des employés.
    """)

# Source des Critères d'Accessibilité
st.markdown("""
    ---
    <div style="text-align: center; color: gray;">
        **Source :**  
        Ces critères de succès sont issus des <a href="https://www.w3.org/Translations/WCAG21-fr/" target="_blank">Web Content Accessibility Guidelines (WCAG) 2.1</a> élaborées par le W3C (World Wide Web Consortium).
    </div>
    """, unsafe_allow_html=True)
