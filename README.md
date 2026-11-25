# Matrice Interactive des Menaces pour Systèmes d'Intelligence Artificielle

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-5b3cf5.svg)](https://tavardt-france.github.io/ai-threat-matrix-fr/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)](LICENSE)

Matrice interactive des menaces et guide de mitigation pour applications avec modèles de langage et IA. Fondé sur OWASP LLM et MITRE ATLAS.

Conçu pour les organisations, chercheurs et équipes d'ingénierie en **France**, ce référentiel propose une matrice structurée pour évaluer la posture défensive et générer des plans de sécurisation pour les modèles de langage et les agents d'Intelligence Artificielle autonomes.

***

## Modes d'Utilisation

### 1. Application Web dans le Navigateur (GitHub Pages)
Accédez à la version interactive directement dans votre navigateur :
- **Adresse Officielle** : [https://tavardt-france.github.io/ai-threat-matrix-fr/](https://tavardt-france.github.io/ai-threat-matrix-fr/)
- **Confidentialité par Conception** : Traitement exécuté à 100% dans le moteur JavaScript de votre navigateur. Aucune donnée architecturale ni résultat n'est transmis à des serveurs tiers.

### 2. Utilitaire en Ligne de Commande (CLI)
Pour les audits automatisés dans les pipelines CI/CD ou l'évaluation locale :

```bash
# Évaluation standard avec profil d'agent autonome
python threat_matrix_evaluator.py -arch agent

# Exportation du plan de sécurisation en Markdown
python threat_matrix_evaluator.py -arch rag -export-blueprint hardening-blueprint.md

# Validation avec fichier de profil de contrôles défensifs
python threat_matrix_evaluator.py -profile profile.json -strict

# Sortie structurée en JSON pour automatisations
python threat_matrix_evaluator.py -arch agent -json
```

***

## 10 Vecteurs Critiques de Risque (OWASP Top 10 for LLMs)

1. **Injection de Prompt (Directe et Indirecte)** : Contournement des consignes du modèle via des entrées malveillantes ou du contexte externe.
2. **Fuite de Données Sensibles** : Divulgation involontaire d'informations confidentielles ou de secrets dans les réponses.
3. **Vulnérabilités de la Chaîne d'Approvisionnement** : Paquets tiers non vérifiés, plugins défectueux ou modèles sans traçabilité.
4. **Empoisonnement des Données et Modèles** : Corruption des jeux de données d'entraînement ou bases documentaires.
5. **Traitement Inapproprié des Sorties** : Exécution directe sans assainissement des réponses du LLM par des interpréteurs de code.
6. **Octroi Excessif d'Autonomie** : Outils d'agent dotés de droits étendus sans validation humaine préalable.
7. **Fuite du Prompt Système** : Extraction de consignes internes ou de secrets intégrés au prompt de référence.
8. **Faiblesses Vectorielles et Embeddings** : Injection de contenus falsifiés dans la base vectorielle du RAG pour tromper le modèle.
9. **Hallucinations et Désinformation Critique** : Formulation d'affirmations erronées dans des processus décisionnels sensibles.
10. **Consommation Illimitée de Ressources** : Surcharge de calcul, attaques par déni de service ou coûts de tokens disproportionnés.

***

## Intégration CI/CD (GitHub Actions)

Exemple de pipeline pour la vérification continue de la posture défensive :

```yaml
name: AI Threat Matrix Gate
on: [push, pull_request]

jobs:
  evaluate-ai-security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Run AI Threat Matrix Assessment
        run: |
          python threat_matrix_evaluator.py -arch agent -strict
```

***

## Conformité et Normes Techniques

- **Norme de Référence** : OWASP Top 10 pour Applications LLM et MITRE ATLAS

***

## Liens Utiles

* **Portail Entreprise:** https://ag.tavardt.com/fr/
* **Suite de Diagnostic:** https://tools.tavardt.com/fr/
* **Contact Technique:** https://ag.tavardt.com/fr/contact/

***

### Licence
Distribué sous Licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.

***

© 2026 TAVARDT. Tous droits réservés.
