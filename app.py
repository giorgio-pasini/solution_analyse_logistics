import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Audit Supply Chain Dyntech 2022",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .main-title {
        background: linear-gradient(90deg, #0f172a, #1e3a8a);
        color: white;
        padding: 16px 20px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.25);
        margin-bottom: 18px;
    }
    .sub-card {
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        background: #ffffff;
        margin-bottom: 10px;
    }
    .tag-quick-win {
        background: #22c55e;
        color: white;
        padding: 3px 8px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 600;
    }
    .tag-mid {
        background: #f59e0b;
        color: white;
        padding: 3px 8px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 600;
    }
    .tag-long {
        background: #ef4444;
        color: white;
        padding: 3px 8px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 600;
    }
    .footer {
        margin-top: 28px;
        text-align: center;
        color: #64748b;
        font-size: 13px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='main-title'><h2>Audit Supply Chain Dyntech 2022 - Pilotage performance Lean</h2><p>Cartographie complète des flux physiques et d'information — 8 processus analysés — 334 employés — Marne-la-Vallée + Orléans + 21 Agences + Export Marseille</p></div>",
    unsafe_allow_html=True,
)

kpi_cols = st.columns(7)
kpi_cols[0].metric("CA Total", "841,8 M€")
kpi_cols[1].metric("Stock immobilisé", "40,2 M€", "36 jours")
kpi_cols[2].metric("Coût commande", "240 €", "standard marché: 40 €")
kpi_cols[3].metric("Cash-to-Cash", "68 jours", "cible CEO: 30j")
kpi_cols[4].metric("EBITDA", "11%")
kpi_cols[5].metric("Efficience VALT", "2.4%")
kpi_cols[6].metric("OTIF", "92.55%")

problems = [
    {
        "name": "1) Gestion de stock",
        "priority": "quick",
        "current_kpis": {
            "Stocks": "40 231 775 €",
            "NITO": "10,26",
            "Days of Inventory": "36 jours",
            "Holding cost": "23,4% (9,4 M€/an)",
            "Stockouts": "16,57%",
            "Ecarts inventaire": "442/an",
        },
        "ishikawa": {
            "Main d'oeuvre": "Pas de cycle counting, faible discipline ABC.",
            "Methodes": "Parametrage mini/maxi insuffisant, controles ponctuels.",
            "Machines": "ERP sans alertes intelligentes stock dormant.",
            "Milieu": "Saisonnalite + volatilite demande.",
            "Matieres": "SKU dormants (375), portefeuille trop large.",
        },
        "five_why": [
            "Pourquoi 442 ecarts inventaire ? -> Comptages non frequents.",
            "Pourquoi comptages non frequents ? -> Processus manualise et chronophage.",
            "Pourquoi processus chronophage ? -> Absence de priorisation ABC quotidienne.",
            "Pourquoi pas de priorisation ? -> Gouvernance stock peu formalisee.",
            "Pourquoi gouvernance faible ? -> Pas de pilotage visuel/Kanban integre ERP.",
        ],
        "muda": ["Inventory", "Defects", "Waiting"],
        "annual_current_cost": 9_400_000,
        "actions": [
            "Kanban sur 4 260 SKU classe A",
            "Cycle counting ABC quotidien",
            "Supermarche entrepot avec emplacements visuels",
            "Kanban electronique integre ERP",
            "Poka-Yoke: alertes stock dormant > 6 mois",
        ],
        "investment": 50_000,
        "future": {
            "NITO": "15,5",
            "Days of Inventory": "22 jours",
            "Stockouts": "5%",
            "Holding cost": "17%",
            "Gain annuel": "4,8 M€",
            "Payback": "< 1 mois",
        },
        "gain": 4_800_000,
        "payback": "< 1 mois",
        "vsm_before": """Fournisseur -> Reception -> Controle manuel -> Stock central (36j) -> Picking -> Livraison
             [Attente validation]     [Ecarts inventaire]         [Ruptures 16,57%]""",
        "vsm_after": """Fournisseur -> EDI/Kanban -> Reception scan -> Supermarche 5S (22j) -> Reappro auto -> Livraison
             [Flux tire]               [Cycle counting ABC]        [Ruptures 5%]""",
        "roi_hypothesis": "Reduction holding cost + reduction ecarts + recuperation ventes perdues.",
        "risks": "Adoption terrain lente; mitigation via coaching quotidien + management visuel.",
    },
    {
        "name": "2) Supply Chain (appro/production)",
        "priority": "quick",
        "current_kpis": {
            "Lignes PO/an": "52 350",
            "Fournisseurs": "303",
            "Cout traitement PO": "350 € (18,3 M€/an)",
            "Cycle time ligne PO": "10,05 min avec signature",
            "SOTD": "93%",
            "Reclamations fournisseurs": "2,20%",
        },
        "ishikawa": {
            "Main d'oeuvre": "Validation centralisee (M. Clarks).",
            "Methodes": "Pas de S&OP et audits fournisseurs insuffisants.",
            "Machines": "Pas d'EDI ni workflow digital complet.",
            "Milieu": "Multiplicite fournisseurs et variabilite.",
            "Matieres": "Donnees previsionnelles peu fiables.",
        },
        "five_why": [
            "Pourquoi cout PO eleve ? -> Trop d'etapes manuelles.",
            "Pourquoi manuel ? -> Pas d'EDI interconnecte.",
            "Pourquoi pas d'EDI ? -> Priorisation budget historiquement faible.",
            "Pourquoi goulot signature ? -> Delegation de pouvoir absente.",
            "Pourquoi delegation absente ? -> Regles de controle non formalisees.",
        ],
        "muda": ["Waiting", "Overprocessing", "Defects", "Motion"],
        "annual_current_cost": 18_300_000,
        "actions": [
            "EDI ASP top 50 fournisseurs",
            "Delegation signatures PO < 30kEUR",
            "S&OP mensuel multi-fonction",
            "SRM scorecard fournisseurs",
            "Activation module forecast ERP",
            "Poka-Yoke workflow auto-validation",
        ],
        "investment": 80_400,
        "future": {
            "Cout/PO": "180 €",
            "SOTD": "97,5%",
            "Reclamations": "0,8%",
            "Precision forecasts": "85%",
            "Gain annuel": "8,9 M€",
            "Payback": "4 jours",
        },
        "gain": 8_900_000,
        "payback": "4 jours",
        "vsm_before": """Besoin achat -> Saisie PO -> Signature manuelle -> Envoi fournisseur -> Relances -> Reception
               [2h30 attente]          [pas d'EDI]                [SOTD 93%]""",
        "vsm_after": """Besoin achat -> Workflow digital -> EDI fournisseur -> Confirmation auto -> Reception -> Scorecard SRM
               [5 min]                  [95% volume EDI]          [SOTD 97,5%]""",
        "roi_hypothesis": "Baisse cout administratif PO + reduction non-qualite fournisseurs.",
        "risks": "Resistance fournisseurs EDI; mitigation via onboarding progressif et support dedie.",
    },
    {
        "name": "3) SAV",
        "priority": "mid",
        "current_kpis": {
            "Lignes retour/an": "10 002 (2,598%)",
            "Reclamations agences": "16 815 (4,368%)",
            "Reclamations export": "498 (9,68%)",
            "Temps traitement retour": "13,17 min/ligne",
            "Produits detruits": "1 109/an",
            "Satisfaction client final": "NC AFNOR",
        },
        "ishikawa": {
            "Main d'oeuvre": "Equipe reduite (5 personnes).",
            "Methodes": "Process retours Access non exploitable.",
            "Machines": "Absence CRM analytique SAV.",
            "Milieu": "Variabilite qualite expedition agences.",
            "Matieres": "Packaging non poka-yoke (erreurs quantites).",
        },
        "five_why": [
            "Pourquoi taux retours 2,598% ? -> Erreurs preparation/quantite.",
            "Pourquoi erreurs preparation ? -> Regles controles non standard.",
            "Pourquoi pas de standard ? -> Pas de referentiel VoC/NPS.",
            "Pourquoi pas de VoC ? -> Processus centré interne, pas client final.",
            "Pourquoi pas client final ? -> Donnees satisfaction non captees.",
        ],
        "muda": ["Defects", "Waiting", "Motion"],
        "annual_current_cost": 2_000_000,
        "actions": [
            "VoC trimestriel clients B2B",
            "Lean Office retours (13,17 -> 6 min)",
            "CRM SAV avec analytics",
            "Poka-Yoke packaging",
            "NPS trimestriel + dashboard temps reel",
        ],
        "investment": 70_000,
        "future": {
            "Taux retours": "1,2%",
            "Temps traitement": "6 min/ligne",
            "Reclamations agences": "1,5%",
            "Reclamations export": "3%",
            "Gain annuel": "1,2 M€",
            "Payback": "< 2 mois",
        },
        "gain": 1_200_000,
        "payback": "< 2 mois",
        "vsm_before": """Retour agence -> Controle manuel -> Saisie Access -> Validation -> Remise stock/destruction
                 [13,17 min]            [data non exploitee]      [reclamations elevees]""",
        "vsm_after": """Retour agence -> Scan CRM -> Regles Lean Office -> Decision auto -> Remise stock rapide
                 [6 min]                 [dashboard temps reel]    [NPS pilote]""",
        "roi_hypothesis": "Reduction cout SAV direct + baisse destructions + reduction reclamations.",
        "risks": "Charge equipe durant transition; mitigation via pilote sur 2 agences puis extension.",
    },
    {
        "name": "4) Facturation",
        "priority": "quick",
        "current_kpis": {
            "Factures/an": "65 250",
            "Cout commande": "240 €",
            "DSO": "62 jours",
            "Cash-to-cash": "68 jours",
            "BFR (DSO-DPO)": "32 jours",
            "Mode facturation": "Papier + double controle",
        },
        "ishikawa": {
            "Main d'oeuvre": "Double controle facture non necessaire.",
            "Methodes": "Relances et litiges en fin d'annee.",
            "Machines": "Pas d'EDI facturation ni Factur-X.",
            "Milieu": "Dependance delais agences B2B.",
            "Matieres": "Donnees transport integrees tardivement.",
        },
        "five_why": [
            "Pourquoi DSO a 62 jours ? -> Envoi papier + workflow lent.",
            "Pourquoi workflow lent ? -> Double controle systematique.",
            "Pourquoi double controle ? -> Heritage ancien process risque.",
            "Pourquoi pas digitalisation ? -> EDI/facturation electronique non deployes.",
            "Pourquoi non deployes ? -> Gouvernance cash insuffisamment priorisee.",
        ],
        "muda": ["Overprocessing", "Waiting", "Motion"],
        "annual_current_cost": 15_660_000,
        "actions": [
            "Facturation electronique Factur-X",
            "Suppression double controle",
            "EDI facturation agences",
            "Escompte 1% paiement <15 jours",
            "Refacturation transport mensuelle automatisee",
            "Poka-Yoke validation donnees ERP",
        ],
        "investment": 60_000,
        "future": {
            "DSO": "35 jours",
            "Cash-to-cash": "30 jours",
            "Cout commande": "150 €",
            "Tresorerie one-shot": "+62 M€",
            "Gain annuel": "5,9 M€",
            "Payback": "4 jours",
        },
        "gain": 5_900_000,
        "payback": "4 jours",
        "vsm_before": """Commande -> Preparation facture -> Double controle -> Envoi postal -> Paiement client
              [attente validations]      [courrier]                [DSO 62j]""",
        "vsm_after": """Commande -> Factur-X auto -> EDI agences -> Relance digitale -> Paiement accelere
              [controle integre]         [temps reel]              [DSO 35j]""",
        "roi_hypothesis": "Baisse cout process + acceleration encaissement + reduction BFR.",
        "risks": "Compatibilite EDI partenaires; mitigation via phase dual-run 3 mois.",
    },
    {
        "name": "5) Data & integration",
        "priority": "long",
        "current_kpis": {
            "ERP": "In-house, MAJ 2020",
            "Integrations": "Pas d'EDI/WMS/CRM",
            "Transport": "Donnees non analysees",
            "Ecarts inventaire": "442/an non analyses",
            "Forecast": "Module peu utilise",
            "Satisfaction client": "NC AFNOR",
        },
        "ishikawa": {
            "Main d'oeuvre": "Culture data heterogene par departement.",
            "Methodes": "Pas de scorecard partagee.",
            "Machines": "Architecture applicative en silos.",
            "Milieu": "Pilotage decentralise multi-sites.",
            "Matieres": "Qualite donnees incompletes (poids/dimensions).",
        },
        "five_why": [
            "Pourquoi pilotage en silos ? -> Sources non connectees.",
            "Pourquoi non connectees ? -> Pas de data lake central.",
            "Pourquoi pas de data lake ? -> Investissement reporte.",
            "Pourquoi investissement reporte ? -> ROI transverse peu formalise.",
            "Pourquoi ROI peu formalise ? -> Manque gouvernance data dediee.",
        ],
        "muda": ["Inventory", "Waiting", "Defects", "Overprocessing", "Motion"],
        "annual_current_cost": 3_000_000,
        "actions": [
            "Data Lake / Data Warehouse central",
            "Dashboards BI par fonction",
            "Balanced Scorecard Kaplan",
            "API ERP-transporteurs",
            "CRM agences + portail B2B",
            "WMS integre + forecast collaboratif",
            "Poka-Yoke data quality",
        ],
        "investment": 230_000,
        "future": {
            "Cout transport/km": "0,95 €",
            "Precision forecast": "85%",
            "Visibilite": "Temps reel",
            "Conformite ISO": "Conforme",
            "Gain annuel": "5-8 M€",
            "Payback": "6 mois",
        },
        "gain": 5_000_000,
        "payback": "6 mois",
        "vsm_before": """ERP silo -> Exports manuels -> Fichiers departement -> Decision tardive
              [pas de CRM/WMS]          [pas d'API]                [actions reactives]""",
        "vsm_after": """ERP + CRM + WMS -> Data Lake -> Dashboard BI -> Alertes qualite data -> Decision data-driven
              [flux integre]            [temps reel]               [pilotage proactif]""",
        "roi_hypothesis": "Optimisation transport + reduction stocks securite + productivite globale.",
        "risks": "Complexite integration SI; mitigation via feuille de route modulaire par trimestre.",
    },
]

tabs = st.tabs(["Etat actuel", "Etat futur", "ROI & Resultats"])

with tabs[0]:
    st.header("Etat actuel - Diagnostic des 5 problematiques")
    st.caption("Analyse Lean Six Sigma: fiche KPI, Ishikawa 5M, 5 Pourquoi, MUDA et cout annuel.")

    for p in problems:
        with st.expander(p["name"], expanded=False):
            c1, c2 = st.columns([1, 1])
            with c1:
                st.subheader("Fiche diagnostic")
                st.dataframe(pd.DataFrame([p["current_kpis"]]), use_container_width=True)
                st.markdown("**Gaspillages MUDA identifies:** " + ", ".join(p["muda"]))
                st.markdown(
                    f"**Cout actuel estime (pertes annuelles):** :red[{p['annual_current_cost'] / 1_000_000:.2f} MEUR/an]"
                )
            with c2:
                st.subheader("Ishikawa 5M (racine)")
                for key, value in p["ishikawa"].items():
                    st.markdown(f"- **{key}** : {value}")

            st.subheader("5 Pourquoi")
            for why in p["five_why"]:
                st.markdown(f"- {why}")

            st.subheader("VSM ASCII - Etat actuel")
            st.code(p["vsm_before"], language="text")

with tabs[1]:
    st.header("Etat futur - Solutions Lean simulees")
    st.caption("Actions Kaizen, Poka-Yoke, KPI cibles, VSM futur, ROI et plan de deploiement.")

    for p in problems:
        with st.expander(p["name"], expanded=False):
            if p["priority"] == "quick":
                st.markdown("<span class='tag-quick-win'>Quick Win</span>", unsafe_allow_html=True)
            elif p["priority"] == "mid":
                st.markdown("<span class='tag-mid'>Mid-term</span>", unsafe_allow_html=True)
            else:
                st.markdown("<span class='tag-long'>Long-term</span>", unsafe_allow_html=True)

            st.subheader("Actions Kaizen")
            for action in p["actions"]:
                st.markdown(f"- {action}")

            st.subheader("Indicateurs cibles (Avant/Apres)")
            before = pd.Series(p["current_kpis"], name="Avant")
            after = pd.Series(p["future"], name="Apres")
            comp = pd.concat([before, after], axis=1).fillna("-")
            st.dataframe(comp, use_container_width=True)

            st.subheader("VSM ASCII - Etat futur")
            st.code(p["vsm_after"], language="text")

            roi = p["gain"] / p["investment"]
            st.success(
                f"Gain annuel: {p['gain'] / 1_000_000:.1f} MEUR | Investissement: {p['investment'] / 1000:.1f} kEUR | ROI: {roi:.1f}x | Payback: {p['payback']}"
            )

            with st.expander("Calcul detaille du ROI (hypotheses + formule)"):
                st.markdown(f"- **Hypothese principale** : {p['roi_hypothesis']}")
                st.markdown(
                    f"- **Formule ROI** : (Gain annuel - Investissement) / Investissement = ({p['gain']:,} - {p['investment']:,}) / {p['investment']:,}"
                )
                st.markdown(f"- **ROI calcule** : {(p['gain'] - p['investment']) / p['investment']:.2f}x")
                st.markdown(f"- **Payback annonce** : {p['payback']}")
                st.markdown(f"- **Risque principal et mitigation** : {p['risks']}")

    gantt_df = pd.DataFrame(
        [
            ("Kanban + Cycle Counting", "2023-01-01", "2023-06-30", "Stock"),
            ("EDI fournisseurs", "2023-01-15", "2023-07-15", "Supply"),
            ("VoC + CRM SAV", "2023-04-01", "2023-09-30", "SAV"),
            ("Facturation electronique", "2023-02-01", "2023-08-31", "Facturation"),
            ("Data Lake + WMS + CRM", "2023-01-01", "2023-12-31", "Data"),
            ("Stabilisation & standard", "2023-10-01", "2023-12-31", "Transverse"),
        ],
        columns=["Etape", "Debut", "Fin", "Axe"],
    )
    fig_gantt = px.timeline(
        gantt_df,
        x_start="Debut",
        x_end="Fin",
        y="Etape",
        color="Axe",
        title="Plan de deploiement Gantt simule - 2023",
    )
    fig_gantt.update_yaxes(autorange="reversed")
    st.plotly_chart(fig_gantt, use_container_width=True)

with tabs[2]:
    st.header("ROI & Resultats")
    st.caption("Synthese financiere, details d'impacts, atteinte objectifs CEO et conformite.")

    summary_df = pd.DataFrame(
        [
            ["Gestion de stock", "50 k€", "4,8 M€", "96x", "< 1 mois"],
            ["Supply Chain", "80,4 k€", "8,9 M€", "110x", "4 jours"],
            ["SAV", "70 k€", "1,2 M€", "17x", "< 2 mois"],
            ["Facturation", "60 k€", "5,9 M€ + 62 M€ (one-shot)", "98x + tresorerie", "4 jours"],
            ["Data & integration", "230 k€ + 80 k€/an", "5-8 M€", "~25x", "6 mois"],
            ["TOTAL", "490,4 k€", "25,8 M€/an + 62 M€", "moyenne 70x", "< 3 mois"],
        ],
        columns=["Problematique", "Investissement", "Gain annuel", "ROI", "Payback"],
    )
    st.subheader("Tableau synthetique des 5 problematiques")
    st.dataframe(summary_df, use_container_width=True)

    st.subheader("Detail de l'impact de chaque action")
    selected = st.selectbox("Choisir une problematique", [p["name"] for p in problems])
    p_sel = next(p for p in problems if p["name"] == selected)
    impacts = []
    for idx, action in enumerate(p_sel["actions"], start=1):
        impacts.append(
            {
                "Action": action,
                "Indicateur cible": list(p_sel["future"].keys())[min(idx - 1, len(p_sel["future"]) - 1)],
                "Avant/Apres": f"{list(p_sel['current_kpis'].values())[0]} -> {list(p_sel['future'].values())[min(idx - 1, len(p_sel['future']) - 1)]}",
                "Gain attribue": f"{p_sel['gain'] / max(len(p_sel['actions']),1) / 1_000_000:.2f} M€/an",
            }
        )
    st.dataframe(pd.DataFrame(impacts), use_container_width=True)

    st.subheader("Synthese CEO")
    st.success(
        "Les 5 actions proposees generent plus de 25 M€ de gains annuels pour un investissement total inferieur a 500 k€, "
        "avec un retour sur investissement moyen inferieur a 3 mois. La tresorerie est renforcee de 62 M€ des la premiere annee. "
        "Tous les objectifs strategiques du CEO 2022 sont atteints voire depasses."
    )

    objectives_df = pd.DataFrame(
        [
            ("+5% CA net", 108),
            ("-20% stocks", 195),
            ("-9% cout transport", 233),
            ("Cash-to-cash 30j", 100),
            ("+9% fidelisation", 112),
        ],
        columns=["Objectif CEO", "Realisation (%)"],
    )
    fig_obj = px.bar(
        objectives_df,
        x="Objectif CEO",
        y="Realisation (%)",
        color="Realisation (%)",
        color_continuous_scale=["#f59e0b", "#22c55e"],
        title="Jauge d'atteinte des objectifs CEO",
        range_y=[0, 240],
    )
    st.plotly_chart(fig_obj, use_container_width=True)

    st.subheader("Conformite")
    st.markdown("**Badges:** ✅ ASLOG   |   ✅ ISO 9001   |   ✅ SCOR v12")
    check_df = pd.DataFrame(
        [
            ("ASLOG", "Pilotage flux, standardisation processus", "OK"),
            ("ISO 9001", "Boucle d'amelioration continue, satisfaction client", "OK"),
            ("SCOR v12", "KPIs plan-source-make-deliver-return", "OK"),
        ],
        columns=["Referentiel", "Points verifies", "Statut"],
    )
    st.table(check_df)

st.markdown("<div class='footer'>Projet Lean Six Sigma - Dyntech 2022</div>", unsafe_allow_html=True)
