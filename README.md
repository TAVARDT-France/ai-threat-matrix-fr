# Matrice Interactive des Menaces pour Systemes d Intelligence Artificielle

[![Live Demo](https://img.shields.io/badge/GitHub%20Pages-Live%20Demo-38bdf8?style=for-the-badge)](https://tavardt-france.github.io/ai-threat-matrix-fr/)
[![Standard](https://img.shields.io/badge/Standard-OWASP%20LLM%20%26%20MITRE-3b82f6?style=for-the-badge)](https://tavardt-france.github.io/ai-threat-matrix-fr/)
[![Privacy](https://img.shields.io/badge/Privacy-100%25%20Client--Side-10b981?style=for-the-badge)](https://tavardt-france.github.io/ai-threat-matrix-fr/)
[![License](https://img.shields.io/badge/License-MIT-slate?style=for-the-badge)](LICENSE)

Matrice interactive des menaces et guide de mitigation pour applications avec modeles de langage et IA. Fonde sur OWASP LLM et MITRE ATLAS.

Concu pour les organisations et equipes techniques en **France**, ce depot fournit un outil autonome pour cartographier les menaces et generer des directives de durcissement pour les modeles de langage et agents d Intelligence Artificielle.

---

## Modes d Utilisation

### 1. Application Web Client (GitHub Pages)
Accessible directement depuis un navigateur web :
- **Lien Officiel** : [https://tavardt-france.github.io/ai-threat-matrix-fr/](https://tavardt-france.github.io/ai-threat-matrix-fr/)
- **Confidentialite Native** : Execution 100% cote client dans le moteur JavaScript de votre navigateur. Aucune donnee n est transmise vers des serveurs tiers.

### 2. Outil en Ligne de Commande (CLI)
Pour les flux d integration continue (CI/CD) ou les audits locaux :

```bash
# Evaluation de base pour profil d agent autonome
python threat_matrix_evaluator.py --arch agent

# Generation de Blueprint de Securisation au format Markdown
python threat_matrix_evaluator.py --arch rag --export-blueprint hardening-blueprint.md

# Mode strict pour pipeline CI/CD (echec avec code 1 en cas de vecteur vulnerable)
python threat_matrix_evaluator.py --profile profile.json --strict

# Export structure en JSON
python threat_matrix_evaluator.py --arch agent --json
```

---

## 10 Vecteurs de Menaces Evalues (OWASP Top 10 for LLMs)

1. **Injection de Prompt (Directe et Indirecte)** : Contournement des consignes du modele via des entrees malveillantes ou du contexte externe.
2. **Fuite de Donnees Sensibles** : Divulgation involontaire d informations confidentielles ou de secrets dans les reponses.
3. **Vulnerabilites de la Chaine d Approvisionnement** : Paquets tiers non verifies, plugins defectueux ou modeles sans tracabilite.
4. **Empoisonnement des Donnees et Modeles** : Corruption des jeux de donnees d entrainement ou bases documentaires.
5. **Traitement Inapproprie des Sorties** : Execution directe sans assainissement des reponses du LLM par des interpretateurs de code.
6. **Octroi Excessif d Autonomie** : Outils d agent dotes de droits etendus sans validation humaine prealable.
7. **Fuite du Prompt Systeme** : Extraction de consignes internes ou de secrets integres au prompt de reference.
8. **Faiblesses Vectorielles et Embeddings** : Injection de contenus falsifies dans la base vectorielle du RAG pour tromper le modele.
9. **Hallucinations et Desinformation Critique** : Formulation d affirmations erronees dans des processus decisionnels sensibles.
10. **Consommation Illimitee de Ressources** : Surcharge de calcul, attaques par deni de service ou couts de tokens disproportionnes.

---

## Exemple d Integration GitHub Actions

```yaml
name: AI Threat Matrix Gate
on: [push, pull_request]

jobs:
  evaluate-ai-security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configurer Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Executer Evaluation de la Matrice des Menaces
        run: |
          python threat_matrix_evaluator.py --arch agent --strict
```

---

## Cadre de Conformite

- **Juridiction** : France
- **Referentiel Technique** : Referentiels de Securite de l IA, ANSSI, OWASP LLM et MITRE ATLAS
- **Organisation Responsable** : [TAVARDT-France](https://github.com/TAVARDT-France)

## Portails TAVARDT

- **Portail Principal** : [https://ag.tavardt.com/fr/](https://ag.tavardt.com/fr/)
- **Outils de Cybersecurite** : [https://tools.tavardt.com/fr/](https://tools.tavardt.com/fr/)
- **Contact Technique** : [https://ag.tavardt.com/fr/contact/](https://ag.tavardt.com/fr/contact/)

---

### Licence
Distribue sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d informations.
