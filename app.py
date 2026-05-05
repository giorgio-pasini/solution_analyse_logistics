import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Supply Chain Audit Dyntech 2022",
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
    "<div class='main-title'>"
    "<h2>Supply Chain Audit Dyntech 2022 — DMAIC · Lean · SCOR</h2>"
    "<p>Five‑axis diagnosis: Inventory · Logistics · Data · SAV · Invoicing — 7,110 active SKUs — 334 employees — "
    "Marne-la-Vallée HQ (4,000 m²) + Orléans production + 21 agencies + Export Marseille</p>"
    "</div>",
    unsafe_allow_html=True,
)

# ── Top KPI strip (all figures from PDF) ─────────────────────────────────────
kpi_cols = st.columns(7)
kpi_cols[0].metric("Turnover 2022", "€841.8 M")
kpi_cols[1].metric("Inventory", "€40.2 M", "36 days")
kpi_cols[2].metric("Stock-out Rate", "16.57%", "Benchmark: 6%")
kpi_cols[3].metric("Cash-to-Cash", "77 days", "CEO target: 30 d")
kpi_cols[4].metric("EBITDA", "11%", "OCF: 3%")
kpi_cols[5].metric("HQ NITO", "10.26", "Target: 14+")
kpi_cols[6].metric("COTD (normal)", "92.55%")

# ── Problem data (5 axes: Inventory, Logistics, Data, SAV, Facturation) ──────
problems = [
    {
        "name": "1) Inventory — Uniform Policies on 7,110 SKUs",
        "priority": "quick",
        "current_kpis": {
            "Stock Value": "€40,200,000",
            "HQ NITO": "10.26 (target 14+)",
            "Days of Inventory": "36 days",
            "Holding Cost": "23.4% (≈ €9.4 M/yr)",
            "Stock-out Rate": "16.57% (benchmark 6%)",
            "Obsolete SKUs": "375 (€178 K frozen)",
            "Inventory Variance 2022": "€12,147",
        },
        "ishikawa": {
            "Manpower": "Cycle counting documented (LOGW2612/05) but not executed; no ABC discipline.",
            "Methods": "Uniform replenishment rules on all 7,110 SKUs; B & C items reviewed only quarterly.",
            "Machines": "ERP forecast module exists but ignored by all 21 sales agencies.",
            "Environment": "Summer demand peaks (+40% volume) not anticipated in stock policies.",
            "Materials": "375 obsolete CZ SKUs immobilise €178 K; portfolio too broad.",
        },
        "five_why": [
            "Why 16.57% stock-out rate? → Uniform min/max rules applied to every SKU regardless of value or volatility.",
            "Why uniform rules? → No ABC × XYZ segmentation; governance not differentiated.",
            "Why no segmentation? → ERP capability underused; no S&OP cycle activated.",
            "Why ERP underused? → Agencies never trained; no shared KPI dashboard.",
            "Why no dashboard? → Data silos between ERP, forwarder DB and agencies — no integration.",
        ],
        "muda": ["Inventory (€178 K frozen)", "Defects (€12,147 variance)", "Waiting (quarterly B/C review)"],
        "annual_current_cost": 9_400_000,
        "actions": [
            "ABC × XYZ matrix: 9-cell governance backbone for all PO and safety-stock decisions",
            "Discard 375 CZ obsolete SKUs → recover €178 K write-off immediately",
            "Restart ERP cycle counting (reactivate LOGW2612/05 procedure)",
            "Activate ERP forecast module + train all 21 agencies",
            "AX cells: continuous EDI replenishment, low SS, daily monitoring",
            "AZ cells: make-to-order, zero stock, dedicated workshop lane",
            "CZ cells: order on demand or discard (no forecast, no holding cost)",
            "Monthly B/C parameter review under ABC/XYZ rules",
        ],
        "investment": 25_000,
        "future": {
            "HQ NITO": "14+",
            "Days of Inventory": "24 days",
            "Stock-out Rate": "< 6%",
            "Inventory Value": "€32 M (−€8 M)",
            "Holding Cost Saved": "€1,872,000 / yr",
            "Payback": "Self-funded by €178 K write-off",
        },
        "gain": 1_872_000,
        "payback": "Self-funded by CZ write-off",
        "vsm_before": (
            "Supplier → Receiving → Manual check → Central stock (36 d) → Picking → Delivery\n"
            "          [Uniform min/max]     [No cycle count]    [Stock-out 16.57%]"
        ),
        "vsm_after": (
            "Supplier → EDI (AX) / Kanban (BX/CX) → Scan receiving → ABC/XYZ slots (24 d) → Auto replenishment → Delivery\n"
            "          [Pull flow by cell]              [Daily cycle count]    [Stock-out < 6%]"
        ),
        "roi_hypothesis": (
            "€40 M × 20 % reduction × 23.4 % holding cost = €1,872,000/yr. "
            "Plus €178 K recovered from CZ write-off in month 0."
        ),
        "risks": "Agency adoption of ERP forecast module; mitigated by dedicated training and monthly S&OP review.",
    },
    {
        "name": "2) Logistics — Frozen 2014 Procedures & Summer Peak",
        "priority": "mid",
        "current_kpis": {
            "COTD Normal": "92.55%",
            "COTD Summer Peak": "88.99% (target 96%)",
            "Delayed Lines": "8.55%",
            "Domestic Claim Rate": "4.37% (target < 1.5%)",
            "Export Claim Rate": "9.68% (target < 3%)",
            "Export Orders Blocked": "2.8%",
            "Transport Cost/km": "€1.20 (CNR benchmark: €0.89)",
            "Goods-in Time/Line": "4.46 min (factory: 1.16 min)",
            "Export Doc Waiting": "14 days (phantom stock)",
        },
        "ishikawa": {
            "Manpower": "No agreed inbound delivery windows; warehouse roles not adapted to summer peak.",
            "Methods": "ISO procedures frozen since 2014; no parallel export documentation workflow.",
            "Machines": "ERP and forwarder database not interfaced; weight/dimension fields empty in ERP.",
            "Environment": "Summer volumes +40%; export complexity (Côte d'Ivoire, Algeria, Dubai, Greece, Israel).",
            "Materials": "14-day export document wait creates phantom stock; random storage allocation.",
        },
        "five_why": [
            "Why 88.99% COTD in summer? → Volumes surge 40% with no anticipation in warehouse layout or staffing.",
            "Why no anticipation? → ISO procedures not updated since 2014; no seasonal slotting.",
            "Why no slotting? → Random storage allocation; ABC zones not defined in WMS.",
            "Why export claim rate at 9.68%? → 14-day document waiting creates phantom stock and blocks 2.8% of orders.",
            "Why 14-day wait? → No ERP↔forwarder API; export documentation handled manually and sequentially.",
        ],
        "muda": ["Waiting (14-day export docs)", "Motion (random storage)", "Defects (4.37%/9.68% claims)", "Overprocessing (4.46 min/line vs 1.16)"],
        "annual_current_cost": 2_320_000,
        "actions": [
            "ABC/XYZ slotting in WMS: Class A items in golden zone, seasonal items pre-positioned",
            "Inbound delivery appointment booking (dock scheduling system)",
            "Parallel export documentation workflow to eliminate 14-day wait",
            "Correct ERP status of all pending export orders (eliminate phantom stock to 0%)",
            "ERP ↔ forwarder API integration (customer ASN)",
            "Renegotiate transport contracts at CNR benchmark rate (€0.89/km)",
            "Update ISO 9001 procedures (2014 → current); reinstate annual supplier audits",
            "Monthly S&OP with seasonality factor for Y-pattern items",
        ],
        "investment": 95_000,
        "future": {
            "COTD Summer Peak": "96%",
            "Domestic Claim Rate": "< 1.5%",
            "Export Claim Rate": "< 3%",
            "Phantom Stock": "0%",
            "Transport Cost/km": "€0.89 (CNR)",
            "Transport Savings": "€800,000 / yr",
        },
        "gain": 800_000,
        "payback": "Within year 1 via transport savings",
        "vsm_before": (
            "Order → WMS random pick → Export manual docs (14 d wait) → Carrier (€1.20/km) → Delivery\n"
            "        [No inbound slots]     [Phantom stock]                 [Claims 4.37%/9.68%]"
        ),
        "vsm_after": (
            "Order → ABC/XYZ slots → Parallel export docs (0 d wait) → ERP↔forwarder API → Carrier (€0.89/km) → Delivery\n"
            "        [Dock booking]       [Phantom stock 0%]              [Claims < 1.5% / < 3%]"
        ),
        "roi_hypothesis": (
            "Transport: (€1.20 − €0.89) × ~2.9 M km = €800,000/yr. "
            "Claims reduction and phantom-stock elimination add further upside not quantified conservatively."
        ),
        "risks": "Carrier renegotiation resistance; mitigated by CNR benchmarked data and competitive tendering.",
    },
    {
        "name": "3) Data & Integration — No EDI, ERP Unused, Silo KPIs",
        "priority": "long",
        "current_kpis": {
            "PO Lines / Year": "52,350 (24 PO/day + 3 manual signature)",
            "PO Processing Time": "10.05 min/line (75% NVA)",
            "PO Processing Cost": "€350/PO (→ €18.3 M/yr)",
            "Supplier OTD (SOTD)": "93% (target > 97%)",
            "Supplier Calls / Day": "3 hours = 750 hrs/yr lost",
            "Last Supplier Audit": "2017",
            "EDI Coverage": "0% (no EDI with any supplier)",
            "B2B Satisfaction Survey": "None (ISO 9001 non-conformity)",
        },
        "ishikawa": {
            "Manpower": "3 h/day on manual supplier calls; buyer time consumed by rework not value.",
            "Methods": "No EDI; no supplier portal; no shared KPI dashboard; no B2B satisfaction survey.",
            "Machines": "ERP and forwarder database not interfaced; weight/dimension fields empty.",
            "Environment": "303 suppliers, 21 agencies, 5 export markets — all operating in silos.",
            "Materials": "Unreliable forecast data; Access non-conformity DB not integrated into ERP.",
        },
        "five_why": [
            "Why 75% NVA in PO process? → Manual steps: physical carry to M. Clarks's office + 360-sec wait for signature.",
            "Why manual signature? → PO threshold not delegated; approval rules not formalised.",
            "Why €350/PO cost? → No EDI; every PO is keyed, printed, signed, scanned, emailed, archived.",
            "Why SOTD only 93%? → No supplier scorecard, no annual audits since 2017, no real-time OTD visibility.",
            "Why no visibility? → Zero data integration: ERP/forwarder/agencies each maintain separate, unconnected files.",
        ],
        "muda": ["Waiting (360 sec signature)", "Motion (carry PO to 1st floor)", "Overprocessing (scan/email/archive)", "Defects (unreliable data)"],
        "annual_current_cost": 18_300_000,
        "actions": [
            "EDI with 5 strategic preferred suppliers (AX cells first)",
            "Raise PO signature threshold €30 K → €75 K (digital workflow above)",
            "ERP ↔ forwarder API: eliminate weight/dimension gaps, enable customer ASN",
            "Power BI shared KPI dashboard (reviewed monthly by executive board)",
            "Reinstate annual supplier audits + deploy supplier scorecard (SOTD, quality, lead time)",
            "Migrate Access non-conformity database into ERP module",
            "Launch B2B satisfaction survey (resolve active ISO 9001 non-conformity)",
            "Create Supply Chain Director role reporting to CEO (CODIR-level sponsor)",
            "Full ERP forecast roll-out across all 21 agencies",
        ],
        "investment": 220_000,
        "future": {
            "PO Processing Time": "3 min/line (−70%)",
            "PO Processing Cost": "< €200 (−€150/PO)",
            "SOTD": "> 97%",
            "PO Process Savings": "€280,000 / yr",
            "ISO 9001 Status": "Compliant (2015 migration)",
            "Satisfaction Score": "> 4/5",
        },
        "gain": 280_000,
        "payback": "Covered by PO savings in year 1",
        "vsm_before": (
            "Purchase need → ERP entry (110 s) → Walk to M. Clarks (40 s) → Wait signature (360 s) → Scan/email/archive (93 s) → Supplier\n"
            "                                     [NVA 75%]                  [Critical bottleneck]"
        ),
        "vsm_after": (
            "Purchase need → Digital workflow (< €75 K auto) → EDI supplier → Auto OA confirmation → ERP update → SRM scorecard\n"
            "                [3 min total]                        [95% EDI]        [SOTD > 97%]"
        ),
        "roi_hypothesis": (
            "(€350 − €200) × 12,300 PO/yr = €1,845,000 gross saving; conservative net figure after implementation: €280,000/yr. "
            "750 hrs/yr of supplier calls recovered for value-added buyer tasks."
        ),
        "risks": "IS integration complexity and supplier EDI onboarding; mitigated by modular phased rollout (AX cells first).",
    },
    {
        "name": "4) After-Sales Service (SAV) — Returns, Claims & Customer Satisfaction",
        "priority": "mid",
        "current_kpis": {
            "Return Lines / yr": "10,002 (2.598% of order lines)",
            "Agency Claims / yr": "16,815 (4.368%)",
            "Export Claims": "498 (9.68%)",
            "Return Processing Time": "13.17 min/line",
            "Products Destroyed / yr": "1,109",
            "End-Customer Satisfaction": "Not measured (AFNOR N/A)",
        },
        "ishikawa": {
            "Manpower": "Small team of 5 people; insufficient for volume and analytical depth.",
            "Methods": "Returns process managed on Access database — not exploitable for root-cause analysis.",
            "Machines": "No analytical CRM for after-sales; no real-time claim tracking dashboard.",
            "Environment": "Variable shipping quality across 21 agencies; no harmonised packing standard.",
            "Materials": "Non-poka-yoke packaging allows quantity errors; no automated quantity check at dispatch.",
        },
        "five_why": [
            "Why 2.598% return rate? → Preparation and quantity errors at agency level.",
            "Why preparation errors? → No standardised control rules at pick & pack stage.",
            "Why no standard? → No Voice of Customer (VoC) / NPS framework to identify recurring failure modes.",
            "Why no VoC? → Process is internally focused; customer feedback not systematically captured.",
            "Why not captured? → No CRM with analytics; satisfaction data never fed back into operations.",
        ],
        "muda": ["Defects (4.368% claim rate)", "Waiting (13.17 min/line processing)", "Motion (manual Access entries)"],
        "annual_current_cost": 2_000_000,
        "actions": [
            "Quarterly B2B customer VoC survey + NPS framework across all 21 agencies",
            "Lean Office on returns process: 13.17 min → 6 min/line via standardised rules",
            "Deploy SAV CRM with analytics (claim type, agency, SKU — real-time dashboard)",
            "Poka-Yoke packaging: automated quantity check at dispatch to prevent preparation errors",
            "Quarterly NPS review + real-time claim dashboard fed back to agency managers",
            "Pilot on 2 agencies before full rollout to manage team workload transition",
        ],
        "investment": 70_000,
        "future": {
            "Return Rate": "1.2% (from 2.598%)",
            "Processing Time": "6 min/line (from 13.17 min)",
            "Agency Claim Rate": "1.5% (from 4.368%)",
            "Export Claim Rate": "3% (from 9.68%)",
            "Annual Gain": "€1,200,000",
            "Payback": "< 2 months",
        },
        "gain": 1_200_000,
        "payback": "< 2 months",
        "vsm_before": (
            "Agency return → Manual check → Access entry → Validation → Restock / Destroy (1,109/yr)\n"
            "               [13.17 min/line]   [data not exploitable]   [claim rate 4.368%]"
        ),
        "vsm_after": (
            "Agency return → CRM scan → Lean Office rules → Auto decision → Fast restock\n"
            "               [6 min/line]   [real-time dashboard]   [NPS tracked — claim < 1.5%]"
        ),
        "roi_hypothesis": (
            "Reduction in direct SAV cost (processing time −54%) + fewer destructions (1,109/yr → target < 400) "
            "+ lower domestic and export claim rates. Conservative annual gain: €1.2 M."
        ),
        "risks": "Team workload during transition; mitigated via pilot on 2 agencies before full rollout.",
    },
    {
        "name": "5) Invoicing (Facturation) — DSO, Cash-to-Cash & Electronic Billing",
        "priority": "quick",
        "current_kpis": {
            "Invoices / yr": "65,250",
            "Order (Invoice) Cost": "€240",
            "DSO": "62 days",
            "Cash-to-Cash": "68 days",
            "NWC (DSO − DPO)": "32 days",
            "Invoicing Mode": "Paper + systematic double check",
        },
        "ishikawa": {
            "Manpower": "Unnecessary systematic double invoice check adds lead time with no quality gain.",
            "Methods": "Late-year collection chasing and disputes; no early-payment incentive scheme.",
            "Machines": "No EDI billing and no Factur-X e-invoicing; fully paper-based workflow.",
            "Environment": "Dependency on B2B agency lead times; transport data integrated too late in cycle.",
            "Materials": "Transport data not available at invoice creation; manual rebilling causes errors and delays.",
        },
        "five_why": [
            "Why DSO at 62 days? → Paper invoices sent by post + slow internal validation workflow.",
            "Why slow workflow? → Systematic double check inherited from legacy risk process.",
            "Why double check maintained? → No ERP data-quality controls — manual verification seen as necessary.",
            "Why no EDI / e-invoicing? → Electronic billing (Factur-X) not deployed; treated as low priority.",
            "Why not prioritised? → Cash governance and NWC impact not formalised at executive level.",
        ],
        "muda": ["Overprocessing (double check)", "Waiting (postal send + DSO 62 d)", "Motion (manual transport rebilling)"],
        "annual_current_cost": 15_660_000,
        "actions": [
            "Deploy Factur-X electronic invoicing (eliminate paper + postal delay)",
            "Remove systematic double check — replaced by ERP Poka-Yoke data validation at source",
            "Agency invoicing EDI: direct digital flow from all 21 agencies",
            "Introduce 1% early-payment discount for settlement < 15 days",
            "Automated monthly transport rebilling (ERP rule-based, no manual entry)",
            "Poka-Yoke: ERP data quality gates prevent invoice errors before emission",
        ],
        "investment": 60_000,
        "future": {
            "DSO": "35 days (from 62 days)",
            "Cash-to-Cash": "30 days (CEO target met)",
            "Invoice Cost": "€150 (from €240)",
            "One-shot Cash Recovery": "+€62 M (NWC release)",
            "Annual Gain": "€5,900,000",
            "Payback": "4 days",
        },
        "gain": 5_900_000,
        "payback": "4 days",
        "vsm_before": (
            "Order → Invoice prep → Double check → Postal send → Client payment\n"
            "        [validation delays]   [paper mail]   [DSO 62 d — Cash-to-Cash 68 d]"
        ),
        "vsm_after": (
            "Order → Auto Factur-X → Agency EDI → Digital chase (−1% discount) → Accelerated payment\n"
            "        [ERP Poka-Yoke]   [real-time]   [DSO 35 d — Cash-to-Cash 30 d]"
        ),
        "roi_hypothesis": (
            "Lower process cost (€240 → €150 × 65,250 invoices) + faster collection (DSO −27 days) "
            "+ one-shot NWC release of €62 M. Annual recurring gain: €5.9 M."
        ),
        "risks": "EDI partner compatibility across agencies; mitigated via 3-month dual-run (paper + electronic) transition phase.",
    },
]

# ── Tabs ──────────────────────────────────────────────────────────────────────
tabs = st.tabs(["AS IS — Current State", "TO BE — Target State", "ROI & CEO Objectives"])

# ── Tab 0: AS IS ──────────────────────────────────────────────────────────────
with tabs[0]:
    st.header("AS IS — Five Structural Deficiencies")
    st.caption(
        "SIPOC · VSM · SCOR analysis — every column of the supply chain shows deficiency. "
        "The five axes are self-reinforcing: uniform inventory → delayed orders → data gaps → poor after‑sales → slow invoicing."
    )

    for p in problems:
        with st.expander(p["name"], expanded=False):
            c1, c2 = st.columns([1, 1])
            with c1:
                st.subheader("Current KPI Sheet")
                st.dataframe(pd.DataFrame([p["current_kpis"]]).T.rename(columns={0: "Value"}), use_container_width=True)
                st.markdown("**MUDA Wastes Identified:** " + " · ".join(p["muda"]))
                st.markdown(
                    f"**Estimated Annual Loss:** :red[{p['annual_current_cost'] / 1_000_000:.2f} M€/yr]"
                )
            with c2:
                st.subheader("Ishikawa 5M — Root Causes")
                for key, value in p["ishikawa"].items():
                    st.markdown(f"- **{key}**: {value}")

            st.subheader("5 Whys")
            for why in p["five_why"]:
                st.markdown(f"- {why}")

            st.subheader("Micro VSM — AS IS")
            st.code(p["vsm_before"], language="text")

# ── Tab 1: TO BE ──────────────────────────────────────────────────────────────
with tabs[1]:
    st.header("TO BE — Five Converging Transformations")
    st.caption(
        "ABC × XYZ inventory governance · Standardised & digitised logistics · "
        "End-to-end EDI / ERP / Power BI integration · Lean SAV · Electronic invoicing — 24 actions over 24 months."
    )

    for p in problems:
        with st.expander(p["name"], expanded=False):
            if p["priority"] == "quick":
                st.markdown("<span class='tag-quick-win'>Quick Win — 0–3 months</span>", unsafe_allow_html=True)
            elif p["priority"] == "mid":
                st.markdown("<span class='tag-mid'>Mid-term — 3–12 months</span>", unsafe_allow_html=True)
            else:
                st.markdown("<span class='tag-long'>Long-term — 12–24 months</span>", unsafe_allow_html=True)

            st.subheader("SCOR Actions")
            for action in p["actions"]:
                st.markdown(f"- {action}")

            st.subheader("Target KPIs — Before / After")
            before = pd.Series(p["current_kpis"], name="AS IS")
            after = pd.Series(p["future"], name="TO BE")
            comp = pd.concat([before, after], axis=1).fillna("—")
            st.dataframe(comp, use_container_width=True)

            st.subheader("Micro VSM — TO BE")
            st.code(p["vsm_after"], language="text")

            roi = p["gain"] / p["investment"]
            st.success(
                f"Annual Gain: {p['gain'] / 1_000_000:.2f} M€ | "
                f"Investment: {p['investment'] / 1000:.0f} k€ | "
                f"ROI: {roi:.1f}x | Payback: {p['payback']}"
            )

            with st.expander("ROI Calculation (assumptions + formula)"):
                st.markdown(f"- **Main assumption**: {p['roi_hypothesis']}")
                st.markdown(
                    f"- **ROI formula**: (Annual Gain − Investment) / Investment = "
                    f"({p['gain']:,} − {p['investment']:,}) / {p['investment']:,}"
                )
                st.markdown(f"- **Calculated ROI**: {(p['gain'] - p['investment']) / p['investment']:.1f}x")
                st.markdown(f"- **Payback**: {p['payback']}")
                st.markdown(f"- **Main risk & mitigation**: {p['risks']}")

    # Gantt — updated with SAV and invoicing actions
    gantt_df = pd.DataFrame(
        [
            # Quick wins 0–3 m
            ("Discard 375 CZ SKUs + cycle counting restart", "2023-01-01", "2023-03-31", "Quick Win"),
            ("Activate ERP forecast module + agency training", "2023-01-15", "2023-03-31", "Quick Win"),
            ("Raise PO threshold €30K → €75K", "2023-01-01", "2023-02-28", "Quick Win"),
            ("Inbound delivery appointment booking", "2023-02-01", "2023-03-31", "Quick Win"),
            ("Correct export ERP status (phantom stock = 0)", "2023-01-01", "2023-02-15", "Quick Win"),
            ("Deploy Factur-X e-invoicing + remove double check", "2023-01-15", "2023-03-31", "Quick Win"),
            # Mid-term 3–12 m
            ("EDI on AX cells — 5 preferred suppliers", "2023-04-01", "2023-09-30", "Mid-term"),
            ("ABC/XYZ slotting in WMS", "2023-04-01", "2023-07-31", "Mid-term"),
            ("Power BI KPI dashboard", "2023-04-01", "2023-08-31", "Mid-term"),
            ("ERP ↔ forwarder API + transport renegotiation", "2023-05-01", "2023-10-31", "Mid-term"),
            ("Digital signature workflow + supplier scorecard", "2023-04-01", "2023-09-30", "Mid-term"),
            ("Monthly S&OP launch", "2023-04-01", "2023-06-30", "Mid-term"),
            ("SAV CRM deployment + Lean Office returns", "2023-05-01", "2023-11-30", "Mid-term"),
            ("Agency invoicing EDI + 1% discount", "2023-04-01", "2023-09-30", "Mid-term"),
            # Long-term 12–24 m
            ("Supply Chain Director appointment", "2024-01-01", "2024-03-31", "Long-term"),
            ("Full ERP forecast roll-out 21 agencies", "2024-01-01", "2024-06-30", "Long-term"),
            ("VMI on AY cells + supplier portal", "2024-03-01", "2024-09-30", "Long-term"),
            ("ISO 9001:2008 → 2015 migration", "2024-01-01", "2024-12-31", "Long-term"),
            ("NPS & real‑time claim dashboard (SAV)", "2024-01-01", "2024-06-30", "Long-term"),
            ("Change-management / data-driven culture programme", "2024-01-01", "2024-12-31", "Long-term"),
        ],
        columns=["Step", "Start", "End", "Horizon"],
    )
    fig_gantt = px.timeline(
        gantt_df,
        x_start="Start",
        x_end="End",
        y="Step",
        color="Horizon",
        color_discrete_map={"Quick Win": "#22c55e", "Mid-term": "#f59e0b", "Long-term": "#ef4444"},
        title="22‑Action Deployment Gantt — 24 months (Including SAV & Invoicing)",
    )
    fig_gantt.update_yaxes(autorange="reversed")
    st.plotly_chart(fig_gantt, use_container_width=True)

# ── Tab 2: ROI & CEO objectives ───────────────────────────────────────────────
with tabs[2]:
    st.header("ROI & CEO Strategic Objectives")
    st.caption("Financial justification (PDF § 5 ROI Matrix) and strategic alignment (PDF § 6).")

    # ROI matrix updated with SAV and Facturation gains
    summary_df = pd.DataFrame(
        [
            ["Inventory reduction (−20%)", "€25 K", "€1,872,000", "~75×", "Month 0 (write-off)"],
            ["Transport renegotiation", "€95 K", "€800,000", "~8×", "Year 1"],
            ["Stock-out reduction (−10 pts)", "Cross-axis", "€450,000", "—", "Year 1"],
            ["PO process automation (EDI)", "€220 K", "€280,000", "~1.3×", "Year 1"],
            ["After‑Sales Service (SAV)", "€70 K", "€1,200,000", "~17×", "< 2 months"],
            ["Electronic Invoicing (Facturation)", "€60 K", "€5,900,000 + €62M one‑shot", "~98× + cash", "4 days"],
            ["TOTAL — 22 actions", "€470 K (0.056% OPEX)", "€10,502,000 / yr + €62M", "~22×", "< 3 months"],
        ],
        columns=["Source of Gain", "Investment Envelope", "Annual Gain", "ROI", "Payback"],
    )
    st.subheader("ROI Matrix — 6 Sources of Gain (Updated with SAV & Invoicing)")
    st.dataframe(summary_df, use_container_width=True)

    # Action-level detail (now includes all 5 axes)
    st.subheader("Action Detail by Axis")
    selected = st.selectbox("Select an axis", [p["name"] for p in problems])
    p_sel = next(p for p in problems if p["name"] == selected)
    impacts = []
    for idx, action in enumerate(p_sel["actions"], start=1):
        future_keys = list(p_sel["future"].keys())
        future_vals = list(p_sel["future"].values())
        kpi_key = future_keys[min(idx - 1, len(future_keys) - 1)]
        kpi_val = future_vals[min(idx - 1, len(future_vals) - 1)]
        impacts.append(
            {
                "Action": action,
                "Target KPI": kpi_key,
                "TO BE Value": kpi_val,
                "Attributed Gain (est.)": f"{p_sel['gain'] / max(len(p_sel['actions']), 1) / 1_000:.0f} k€/yr",
            }
        )
    st.dataframe(pd.DataFrame(impacts), use_container_width=True)

    # CEO strategic alignment (unchanged, covers all gains)
    st.subheader("Strategic Alignment — CEO Targets (PDF § 6)")
    st.success(
        "The €470,000 envelope over 24 months represents 0.056% of OPEX and unlocks €10.5 M of recurring annual gains "
        "plus a one‑time €62 M NWC release — an average 22× ROI with payback under 3 months. "
        "Every euro maps to one of the four CEO targets with no external financing required."
    )

    objectives_df = pd.DataFrame(
        [
            ("+5% Net Revenue", "Service level → 96%; stock-out < 6%", "€841.8 M → ~€844 M (+€2 M recovered sales)", 105),
            ("+12% Export Share", "Phantom stock 0%; parallel docs; claims 9.68% → < 3%", "Export cycle time −50%; Marseille claims −70%", 112),
            ("−20% Inventory", "ABC×XYZ policies; CZ discard; monthly B/C review", "€40 M → €32 M; €1.87 M/yr holding cost saved", 120),
            ("−9% Transport Cost", "ERP↔forwarder API; CNR-benchmarked renegotiation", "€1.20/km → €0.89/km; €800 K/yr saved", 109),
            ("30-day Cash-to-Cash", "Inventory reduction + e‑invoicing + faster export cycle", "Cash-to-cash 77 d → 30 d; OCF 3% → 9%", 130),
        ],
        columns=["CEO Target", "How Addressed", "Quantified Outcome", "Achievement (%)"],
    )
    st.dataframe(objectives_df[["CEO Target", "How Addressed", "Quantified Outcome"]], use_container_width=True)

    fig_obj = px.bar(
        objectives_df,
        x="CEO Target",
        y="Achievement (%)",
        color="Achievement (%)",
        color_continuous_scale=["#f59e0b", "#22c55e"],
        title="CEO Objective Achievement — Indicative Progress (PDF § 6)",
        range_y=[0, 140],
        text="Achievement (%)",
    )
    fig_obj.update_traces(textposition="outside")
    st.plotly_chart(fig_obj, use_container_width=True)

    # Governance conditions (unchanged)
    st.subheader("Three Conditions for Success (PDF § 6)")
    col1, col2, col3 = st.columns(3)
    col1.info(
        "**1 — Executive Sponsorship**\n\n"
        "Appoint a Supply Chain Director reporting directly to CEO. "
        "Monthly review tied to 22 actions and 4 CEO targets. Without CODIR-level sponsor, "
        "the project erodes after Q1."
    )
    col2.info(
        "**2 — Sequenced Away from Summer Peak**\n\n"
        "Structural changes (WMS slotting, EDI roll-out, ERP activation) must NOT deploy "
        "June–August when volumes are 40% above normal. Gantt schedules them in months 3–6 and 9–12."
    )
    col3.info(
        "**3 — Data Integration as Strategic Asset**\n\n"
        "EDI, ERP↔forwarder API and shared KPI dashboard are the operating system of the new supply chain. "
        "Funding ring-fenced; KPIs reviewed monthly by executive board, not left to IT alone."
    )

    # Compliance
    st.subheader("Framework Compliance")
    st.markdown("**Badges:** ✅ DMAIC   |   ✅ Lean / VSM   |   ✅ SCOR (Plan · Source · Make · Deliver · Return · Enable)   |   ✅ ISO 9001:2015 (target)")
    check_df = pd.DataFrame(
        [
            ("DMAIC", "Define/Measure/Analyse/Improve/Control structure respected throughout", "Applied"),
            ("Lean / VSM", "AS IS and TO BE VSM per process axis; MUDA identified and quantified", "Applied"),
            ("SCOR", "6 levers: Plan, Source, Make, Deliver, Return, Enable — with KPI targets", "Applied"),
            ("ISO 9001:2015", "B2B survey launched; NC DB migrated to ERP; audit cycle reinstated", "In progress"),
        ],
        columns=["Framework", "Points Verified", "Status"],
    )
    st.table(check_df)

st.markdown(
    "<div class='footer'>"
    "ISTELI Paris — N. Yacine NDIAYE · Chaewon JUNG · Jonathan RINCON — Dyntech Supply Chain Continuous Improvement 2022"
    "</div>",
    unsafe_allow_html=True,
)
