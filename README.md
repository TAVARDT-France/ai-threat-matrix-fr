# Matrice Interactive des Menaces pour Systèmes d'Intelligence Artificielle

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-5b3cf5.svg)](https://tavardt-france.github.io/ai-threat-matrix-fr/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

***

Matrice interactive des menaces et évaluateur de posture défensive pour Grands Modèles de Langage et agents IA autonomes développé par **TAVARDT**. Ancré dans les standards OWASP Top 10 for LLM Applications et MITRE ATLAS, cet outil analyse les vulnérabilités, calcule un score global de robustesse et génère des plans de remédiation ciblés.

***

## Fonctionnalités Clés et Architecture Défensive

* **Modélisation Adaptée à l'Architecture** : Personnalise l'analyse des risques selon quatre modèles de déploiement incluant agent autonome, pipeline RAG, chat conversationnel et passerelle API.
* **Mesure Quantitative du Durcissement** : Calcule un score défensif étalonné de 0 à 100 points fondé sur des coefficients de sévérité et l'état effectif des contre-mesures.
* **Production de Plans de Renforcement** : Exporte des rapports structurés en Markdown précisant les expositions critiques, les axes d'amélioration prioritaires et les actions correctives.

***

## Vecteurs de Risque et Impact Opérationnel

Le déploiement de modèles linguistiques sans cartographie des cybermenaces expose l'infrastructure au détournement de contexte, à l'empoisonnement de données et à l'escalade d'accès. L'auditeur couvre dix vecteurs critiques tout au long du cycle opérationnel de l'IA :

* **Injections de Requêtes Directes et Indirectes (OWASP-LLM01)** : Neutralise les instructions hostiles conçues pour transgresser les règles du système ou exécuter des ordres non fiables (Pondération : 15 points).
* **Divulgation d'Informations Sensibles (OWASP-LLM02)** : Repère les fuites involontaires de données personnelles, de secrets industriels ou de contextes confidentiels dans les réponses (Pondération : 12 points).
* **Vulnérabilités de la Chaîne d'Approvisionnement (OWASP-LLM03)** : Audite les dépendances envers les modèles tiers non vérifiés, les extensions non auditées et les bases d'entraînement externes (Pondération : 10 points).
* **Empoisonnement des Données et Modèles (OWASP-LLM04)** : Détecte les risques d'altération intentionnelle des corpus d'entraînement ou des sources de récupération documentaire (Pondération : 10 points).
* **Traitement Inadéquat des Sorties (OWASP-LLM05)** : Examine les réponses brutes transmises sans assainissement préalable aux navigateurs, APIs ou interpréteurs système (Pondération : 12 points).
* **Autonomie et Permissions Excessives (OWASP-LLM06)** : Prévient les actions destructrices d'agents disposant de privilèges démesurés sur des bases de données de production (Pondération : 14 points).
* **Extraction du Prompt Système (OWASP-LLM07)** : Bloque les attaques d'ingénierie inversée visant la révélation des consignes maîtresses et règles de sécurité internes (Pondération : 8 points).
* **Faiblesses des Vecteurs et Plongements (OWASP-LLM08)** : Évalue les altérations sémantiques et les extractions non autorisées dans les bases de données vectorielles (Pondération : 7 points).
* **Hallucinations et Désinformation (OWASP-LLM09)** : Identifie les déclarations factuellement erronées ne reposant sur aucun point d'ancrage documentaire vérifié (Pondération : 6 points).
* **Consommation Incontrôlée de Ressources (OWASP-LLM10)** : Protège contre les dénis de service provoqués par des contextes démesurés ou des boucles d'agents infinies (Pondération : 6 points).

La posture globale est catégorisée en **HARDENED** (85 à 100), **DEVELOPING** (60 à 84) ou **VULNERABLE** (inférieur à 60). Les vecteurs protégés reçoivent leur pleine pondération, les défenses partielles obtiennent 50%, et les failles béantes comptent pour zéro.

***

## Installation et Utilisation CLI

Auditez les déploiements d'IA localement ou intégrez des contrôles automatisés dans vos chaînes logicielles via Python :

```bash
# Cloner le dépôt officiel
git clone https://github.com/TAVARDT-France/ai-threat-matrix-fr.git

# Accéder au dossier de travail
cd ai-threat-matrix-fr

# Évaluer la posture via le profil agent autonome
python threat_matrix_evaluator.py -a agent

# Exporter un plan de renforcement complet en Markdown
python threat_matrix_evaluator.py -a agent -e blueprint.md

# Exécuter une évaluation stricte avec rapport JSON structuré
python threat_matrix_evaluator.py -a agent -s -j
```

***

## FAQ Technique

### Quelle méthodologie la Matrice des Menaces IA utilise-t-elle pour évaluer la posture du modèle ?

Le moteur d'évaluation confronte les défenses actives aux dix catégories de l'OWASP Top 10 pour LLM à l'aide de coefficients pondérés totalisant 100 points. En fonction des contrôles validés, le système classe le niveau de protection en HARDENED dès 85 points, DEVELOPING entre 60 et 84 points, ou VULNERABLE sous 60 points.

### De quelle manière les profils architecturaux orientent-ils l'analyse de sécurité ?

L'utilitaire CLI ajuste son modèle d'évaluation selon quatre profils d'architecture regroupant agent autonome, pipeline RAG, interface de dialogue et passerelle API. Spécifier le profil adéquat via l'option -a permet d'adapter les recommandations aux flux de données réels du système inspecté.

### En quoi le générateur de plan de durcissement aide-t-il les équipes d'ingénierie ?

L'exécution de l'outil avec l'argument -e produit un plan de sécurité complet en syntaxe Markdown précisant les failles non couvertes et les mesures correctives indispensables. Ce document technique facilite la transition entre audit de gouvernance et renforcement pratique au sein des équipes de développement.

### Quels impacts opérationnels résultent d'une autonomie et d'autorisations excessives (LLM06) ?

Attribuer des privilèges étendus aux agents autonomes autorise des injections indirectes de prompt à déclencher des actions critiques sur les bases de données et services reliés. Mettre en place des listes blanches d'actions et des barrières de confirmation humaine restreint les capacités de l'agent au principe du moindre privilège.

### L'auditeur de matrice peut-il servir de barrière de validation dans les pipelines CI/CD ?

Le script CLI lit des profils de sécurité au format JSON via l'option -p et renvoie un code d'erreur 1 si le mode strict -s identifie des failles ouvertes. Associé à l'argument -j pour exporter un flux JSON structuré, il permet d'automatiser le blocage immédiat des déploiements vulnérables.

***

## Liens Utiles

* **Portail Institutionnel:** https://ag.tavardt.com/fr/
* **Suite de Diagnostic:** https://tools.tavardt.com/fr/
* **Contact Technique:** https://ag.tavardt.com/fr/contact/

***

### Licence
Distribué sous Licence MIT. Consultez [LICENSE](LICENSE) pour plus d'informations.

***

© 2026 TAVARDT. Tous droits réservés.
