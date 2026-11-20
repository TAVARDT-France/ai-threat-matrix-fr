#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TAVARDT France
Matrice Interactive des Menaces pour Systemes d Intelligence Artificielle
Matrice interactive des menaces et guide de mitigation pour applications avec modeles de langage et IA. Fonde sur OWASP LLM et MITRE ATLAS.

Standard: Referentiels de Securite de l IA, ANSSI, OWASP LLM et MITRE ATLAS
Repository: https://github.com/TAVARDT-France/ai-threat-matrix-fr
Online Web App: https://tavardt-france.github.io/ai-threat-matrix-fr/
"""

import os
import sys
import json
import argparse
from datetime import datetime

THREAT_DEFINITIONS = [
    {"id": "LLM01", "code": "OWASP-LLM01", "title": "Injection de Prompt (Directe et Indirecte)", "weight": 15, "default": "exposed"},
    {"id": "LLM02", "code": "OWASP-LLM02", "title": "Fuite de Donnees Sensibles", "weight": 12, "default": "partial"},
    {"id": "LLM03", "code": "OWASP-LLM03", "title": "Vulnerabilites de la Chaine d Approvisionnement", "weight": 10, "default": "exposed"},
    {"id": "LLM04", "code": "OWASP-LLM04", "title": "Empoisonnement des Donnees et Modeles", "weight": 10, "default": "exposed"},
    {"id": "LLM05", "code": "OWASP-LLM05", "title": "Traitement Inapproprie des Sorties", "weight": 12, "default": "exposed"},
    {"id": "LLM06", "code": "OWASP-LLM06", "title": "Octroi Excessif d Autonomie", "weight": 14, "default": "exposed"},
    {"id": "LLM07", "code": "OWASP-LLM07", "title": "Fuite du Prompt Systeme", "weight": 8,  "default": "defended"},
    {"id": "LLM08", "code": "OWASP-LLM08", "title": "Faiblesses Vectorielles et Embeddings", "weight": 7,  "default": "partial"},
    {"id": "LLM09", "code": "OWASP-LLM09", "title": "Hallucinations et Desinformation Critique", "weight": 6,  "default": "defended"},
    {"id": "LLM10", "code": "OWASP-LLM10", "title": "Consommation Illimitee de Ressources", "weight": 6,  "default": "exposed"}
]

def evaluate_posture(arch, profile_states):
    total_score = 0
    defended_count = 0
    exposed_count = 0
    eval_items = []

    for item in THREAT_DEFINITIONS:
        tid = item["id"]
        state = profile_states.get(tid, item["default"]).lower()
        if state == "defended":
            total_score += item["weight"]
            defended_count += 1
        elif state == "partial":
            total_score += (item["weight"] * 0.5)
        else:
            state = "exposed"
            exposed_count += 1

        eval_items.append({
            "id": tid,
            "code": item["code"],
            "title": item["title"],
            "weight": item["weight"],
            "status": state
        })

    score = round(total_score)
    if score >= 85:
        posture = "SECURISE"
    elif score >= 60:
        posture = "EN COURS"
    else:
        posture = "VULNERABLE"

    return {
        "architecture": arch,
        "score": score,
        "posture": posture,
        "defended_count": defended_count,
        "exposed_count": exposed_count,
        "items": eval_items
    }

def generate_blueprint_md(evaluation):
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    md = []
    md.append("# AI Security Hardening Blueprint")
    md.append(f"- **Organization**: TAVARDT France")
    md.append(f"- **Evaluation Date**: {ts} UTC")
    md.append(f"- **Architecture Profile**: {evaluation['architecture'].upper()}")
    md.append(f"- **Compliance Standard**: Referentiels de Securite de l IA, ANSSI, OWASP LLM et MITRE ATLAS")
    md.append(f"- **Hardening Score**: {evaluation['score']} / 100")
    md.append(f"- **Defensive Posture**: {evaluation['posture']}")
    md.append("")
    md.append("## Threat Vector Status and Gaps")
    md.append("")
    for it in evaluation["items"]:
        md.append(f"### [{it['code']}] {it['title']} - Status: {it['status'].upper()}")
        if it["status"] == "exposed":
            md.append("- **Deficiency**: Unmitigated exposure. Direct security risk.")
            md.append("- **Remediation**: Implement mandatory heuristic guardrails, context sandboxing, and execution whitelists.")
        elif it["status"] == "partial":
            md.append("- **Deficiency**: Partial controls active.")
            md.append("- **Remediation**: Introduce secondary confirmation gates and automated red-teaming checks.")
        else:
            md.append("- **Status**: Verified defensive controls documented.")
        md.append("")
    return "\n".join(md)

def main():
    parser = argparse.ArgumentParser(description="Evaluateur de Posture de Securite en Intelligence Artificielle et Generateur de Blueprint.")
    parser.add_argument("--arch", choices=["agent", "rag", "chat", "api"], default="agent", help="Profil architectural de la solution (agent, rag, chat, api)")
    parser.add_argument("--profile", help="Chemin vers le fichier JSON de statut des controles defensifs")
    parser.add_argument("--export-blueprint", help="Exporter le blueprint de securisation en fichier Markdown")
    parser.add_argument("--strict", action="store_true", help="Quitter avec code 1 en presence d un vecteur vulnerable")
    parser.add_argument("--json", action="store_true", help="Afficher la sortie au format JSON structure")

    args = parser.parse_args()

    states = {}
    if args.profile:
        if not os.path.exists(args.profile):
            print(f"Error: Profile file not found: {args.profile}", file=sys.stderr)
            sys.exit(2)
        try:
            with open(args.profile, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    states = data.get("threat_states", data)
        except Exception as e:
            print(f"Error reading JSON from {args.profile}: {e}", file=sys.stderr)
            sys.exit(2)

    eval_res = evaluate_posture(args.arch, states)

    if args.export_blueprint:
        bp_content = generate_blueprint_md(eval_res)
        with open(args.export_blueprint, "w", encoding="utf-8") as bf:
            bf.write(bp_content)
        print(f"Blueprint de securisation enregistre avec succes dans: {args.export_blueprint}")

    if args.json:
        print(json.dumps(eval_res, indent=2, ensure_ascii=False))
    else:
        print("=" * 64)
        print(f"MATRICE DES MENACES IA: TAVARDT France")
        print(f"Standard: Referentiels de Securite de l IA, ANSSI, OWASP LLM et MITRE ATLAS")
        print(f"Architecture: {eval_res['architecture'].upper()}")
        print(f"Hardening Score: {eval_res['score']} / 100")
        print(f"Defensive Posture: {eval_res['posture']}")
        print(f"Active Defended Controls: {eval_res['defended_count']} / 10")
        print(f"Exposed Vectors: {eval_res['exposed_count']} / 10")
        print("=" * 64)

        for it in eval_res["items"]:
            status_label = it["status"].upper()
            print(f"[{it['code']}] {it['title']}: {status_label}")

    if args.strict and eval_res["exposed_count"] > 0:
        sys.exit(1)
    if eval_res["score"] < 60:
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
