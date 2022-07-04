from PIL import Image
from utils import *

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# Yannis RACHID, Junior Data Scientist
##### *Curriculum Vitae* 
''')

image = Image.open('img/photo.png')
st.image(image, width=150)

st.markdown('## Profil', unsafe_allow_html=True)
st.info('''
Junior Data Scientist âgé de 25 ans en recherche d'un poste en CDI suite à l'obtention du Master MIASHS. Force de propositions, j'ai de fortes capacités d'adaptation et d'intégration.
''')

#####################
# Navigation
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #256D8E;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/yannis-rachid-230/" target="_blank">Yannis RACHID</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Accueil <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#formations">Formations</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experiences">Expériences</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#competences">Compétences</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#liens">Liens</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
# corriger le lien expériences

st.markdown('''
## Formations
''')

txt('**Master 2 MIASHS** (Data Science), *Université Montpellier 3*, France',
    '2021-2022')
st.markdown('''
- Résultat : `En cours d'obtention`
- Programmation et calcul parallèle
- Régression logistique et modèles log-linéaires
- Données massives et Big Data
- Open Data et Web des données
- Optimisation et régularisation des modèles d'apprentissage
- Data visualisation
- Deep Learning (+ challenge de classification d'images)
- Recherche opérationnelle
- Analyse d'images
- Anglais
- Alternance
''')

txt('**Master 1 MIASHS** (Data Science), *Université Montpellier 3*, France',
    '2020-2021')
st.markdown('''
- Résultat : `Mention Assez Bien`
- Bases de données (SQL et noSQL)
- Intégration de données connectées
- Apprentissage supervisé et non-supervisé
- Sémiologie graphique
- Modèles de régression linéaire
- Analyse de données multidimensionnelles (Analyse en Composantes Principales)
- Anglais
- Travail d'étude et de recherche : Annotation de données médicales (customisation algorithme + interface)
- Analyse de réseaux sociaux (+ projet avec l'API Twitter)
- Analyse de données textuelles (+ projet avec classification de texte à l'aide du sentiment)
- Analyse de données spatiales (QGIS)
- Analyse de données de panels
- Gestion de projets (méthodes, outils)
- Marathon du web (vainqueur, association ABDIA)
- Alternance
''')

txt('**Licence MIASHS** (Data Science), *Université Montpellier 3*, France',
    '2017-2020')
st.markdown('''
- Résultat : `Mention Assez Bien`
''')

#####################
st.markdown('''
## Experiences
''')

txt('**Data Scientist (alternant)**, MeetDeal, Rivesaltes, France',
    '2021-2022')
st.markdown('''
- Contribution à la mise en œuvre d'outils de prétraitement et de structuration des données textuelles en amont des tâches de traitement du langage naturel (NLP) telles que la reconnaissance des entités nommées, l'analyse sémantique, l'extraction de terminologie, l'extraction de connaissances. - pour l'entraînement des modèles statistiques (y compris les modèles de langage tels que BERT, les classifieurs).
- Mise en œuvre d'un outil d'analyse thématique des conversations de chat en direct anonymisées afin de dégager les grandes tendances.
- Contribution à la conception d'outils de visualisation de données issues de conversations et de réseaux sociaux.
- Contribution à la caractérisation de profils de clients en vue de leur généralisation et de leur classification.
- Développement d'une application automatisant la génération de reporting au format PDF (KPI, visualisations sur une période sélectionnée)
- Enrichissement de la base de connaissances métier pour l'apprentissage incrémental des classifieurs.
- Documentation des outils développés et des contributions.
''')

txt('**Créateur de contenu**, [Football Analytics, @lookatfoot](https://www.instagram.com/lookatfoot/?hl=fr)',
    '2022-Présent')
st.markdown('''
- Analyse de données liées au football (performances, matchs, scouting de joueurs)
- Création d'un outil d'analyse d'après-match en Python à l'aide des données WhoScored
''')

txt('**Data Scientist (stagiaire)**, MeetDeal, Rivesaltes, France',
    '2020-2021')
st.markdown('''
- Étude des outils et environnements existants des principaux acteurs du marché (Facebook API, Google API).
- Développement d'une brique logicielle pour l'automatisation et le suivi des campagnes marketing.
- Développement d'une brique de structuration des données de campagne (statistiques de campagne) et de documentation.
- Data scraping et utilisation d'un réseau lexico-sémantique pour la construction d'une base de connaissances métier en vue de la conception d'un chatbot.
- Développement d'un outil d'analyse de sentiment avec la suite Elastic.
''')

txt('**Footballeur (contrat aspirant professionnel)**, [Yannis RACHID Highlights](https://www.dailymotion.com/yannis-rachid6/videos)',
    '2013-2016')
st.markdown('''
En quittant le domicile familial à l'âge de 16 ans, je suis vite devenu autonome et mature. Au-delà du contexte sportif, j’ai appris ce qu’était la rigueur et le goût de l’effort au quotidien.
''')

#####################
st.markdown('''
## Competences
''')
txt3('Langages de programmation', '`Python`, `R`, `SQL`')
txt3('Data processing', '`pandas`, `numpy`, `pyspark`')
txt3('Data visualisation', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`, `Kibana`')
txt3('Apprentissage Automatique', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`, `PyTorch`')
txt3('Bases de données', '`MySQL`, `PostgreSQL`, `Neo4j`, `Elastic Search`')
txt3('Natural Langage Processing', '`nltk`, `spacy`')
txt3('Théorie des graphes', '`igraph`, `networkx`')
txt3('Développement Web', '`Flask`, `HTML5`, `CSS3`, `PHP`')
txt3('Déploiement de modèle', '`streamlit`, `R Shiny`, `Heroku`, `AWS EC2`')
txt3('Cloud', '`Amazon Web Services`')
txt3("Systèmes d'exploitation", '`Windows`, `MacOS`, `Linux`')
txt3("Bureautique", '`Microsoft Office`, `LateX`, `OpenOffice`')
txt3('Langues', '`Français (maternel)`, `Anglais (professionnel)`, `Espagnol (intermédiaire)`')
txt3('Gestion de projet', '`Git`, `Jira`, `Méthode Agile`')

#####################
st.markdown('''
## Liens
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/yannis-rachid-230/')
txt2('GitHub', 'https://github.com/yannisrachid')