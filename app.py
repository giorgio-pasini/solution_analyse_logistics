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
    "<div class='main-title'><h2>Supply Chain Audit Dyntech 2022 - Lean Performance Management</h2><p>Complete mapping of physical and information flows — 8 processes analysed — 334 employees — Marne-la-Vallée + Orléans + 21 Agencies + Export Marseille</p></div>",
    unsafe_allow_html=True,
)

kpi_cols = st.columns(7)
kpi_cols[0].metric("Total Revenue", "€841.8M")
kpi_cols[1].metric("Tied-up Stock", "€40.2M", "36 days")
kpi_cols[2].metric("Order Cost", "€240", "Market standard: €40")
kpi_cols[3].metric("Cash-to-Cash", "68 days", "CEO target: 30d")
kpi_cols[4].metric("EBITDA", "11%")
kpi_cols[5].metric("VALT Efficiency", "2.4%")
kpi_cols[6].metric("OTIF", "92.55%")

problems = [
    {
        "name": "1) Inventory Management",
        "priority": "quick",
        "current_kpis": {
            "Stock Value": "€40,231,775",
            "NITO": "10.26",
            "Days of Inventory": "36 days",
            "Holding Cost": "23.4% (€9.4M/yr)",
            "Stockouts": "16.57%",
            "Inventory Discrepancies": "442/yr",
        },
        "ishikawa": {
            "Manpower": "No cycle counting, weak ABC discipline.",
            "Methods": "Insufficient min/max parameters, ad-hoc controls.",
            "Machines": "ERP without intelligent dormant stock alerts.",
            "Environment": "Seasonality + demand volatility.",
            "Materials": "Dormant SKUs (375), overly broad portfolio.",
        },
        "five_why": [
            "Why 442 inventory discrepancies? -> Infrequent counts.",
            "Why infrequent counts? -> Manual and time-consuming process.",
            "Why time-consuming? -> No daily ABC prioritisation.",
            "Why no prioritisation? -> Poorly formalised stock governance.",
            "Why weak governance? -> No visual/Kanban management integrated with ERP.",
        ],
        "muda": ["Inventory", "Defects", "Waiting"],
        "annual_current_cost": 9_400_000,
        "actions": [
            "Kanban on 4,260 Class A SKUs",
            "Daily ABC cycle counting",
            "Warehouse supermarket with visual locations",
            "Electronic Kanban integrated with ERP",
            "Poka-Yoke: alerts for dormant stock > 6 months",
        ],
        "investment": 50_000,
        "future": {
            "NITO": "15.5",
            "Days of Inventory": "22 days",
            "Stockouts": "5%",
            "Holding Cost": "17%",
            "Annual Gain": "€4.8M",
            "Payback": "< 1 month",
        },
        "gain": 4_800_000,
        "payback": "< 1 month",
        "vsm_before": """Supplier -> Receiving -> Manual Check -> Central Stock (36d) -> Picking -> Delivery
          [Validation Wait]     [Inventory Gaps]         [Stockouts 16.57%]""",
        "vsm_after": """Supplier -> EDI/Kanban -> Scan Receiving -> 5S Supermarket (22d) -> Auto Replenishment -> Delivery
          [Pull Flow]               [ABC Cycle Count]        [Stockouts 5%]""",
        "roi_hypothesis": "Reduction in holding costs + fewer discrepancies + recovery of lost sales.",
        "risks": "Slow field adoption; mitigated via daily coaching + visual management.",
    },
    {
        "name": "2) Supply Chain (Procurement/Production)",
        "priority": "quick",
        "current_kpis": {
            "PO Lines/yr": "52,350",
            "Suppliers": "303",
            "PO Processing Cost": "€350 (€18.3M/yr)",
            "PO Line Cycle Time": "10.05 min with signature",
            "SOTD": "93%",
            "Supplier Claims": "2.20%",
        },
        "ishikawa": {
            "Manpower": "Centralised approval (Mr. Clarks).",
            "Methods": "No S&OP and insufficient supplier audits.",
            "Machines": "No EDI or complete digital workflow.",
            "Environment": "Multiple suppliers and high variability.",
            "Materials": "Unreliable forecast data.",
        },
        "five_why": [
            "Why high PO cost? -> Too many manual steps.",
            "Why manual? -> No interconnected EDI.",
            "Why no EDI? -> Historically low budget priority.",
            "Why signature bottleneck? -> No delegation of authority.",
            "Why no delegation? -> Approval rules not formalised.",
        ],
        "muda": ["Waiting", "Overprocessing", "Defects", "Motion"],
        "annual_current_cost": 18_300_000,
        "actions": [
            "EDI ASP for top 50 suppliers",
            "PO signature delegation < €30K",
            "Monthly multi-function S&OP",
            "SRM supplier scorecard",
            "ERP forecast module activation",
            "Poka-Yoke auto-validation workflow",
        ],
        "investment": 80_400,
        "future": {
            "Cost/PO": "€180",
            "SOTD": "97.5%",
            "Claims": "0.8%",
            "Forecast Accuracy": "85%",
            "Annual Gain": "€8.9M",
            "Payback": "4 days",
        },
        "gain": 8_900_000,
        "payback": "4 days",
        "vsm_before": """Purchase Need -> PO Entry -> Manual Signature -> Supplier Send -> Follow-ups -> Receiving
             [2h30 wait]          [no EDI]                [SOTD 93%]""",
        "vsm_after": """Purchase Need -> Digital Workflow -> EDI Supplier -> Auto Confirmation -> Receiving -> SRM Scorecard
             [5 min]                  [95% EDI volume]          [SOTD 97.5%]""",
        "roi_hypothesis": "Lower PO admin cost + reduction in supplier non-quality.",
        "risks": "Supplier resistance to EDI; mitigated via gradual onboarding and dedicated support.",
    },
    {
        "name": "3) After-Sales Service (SAV)",
        "priority": "mid",
        "current_kpis": {
            "Return Lines/yr": "10,002 (2.598%)",
            "Agency Claims": "16,815 (4.368%)",
            "Export Claims": "498 (9.68%)",
            "Return Processing Time": "13.17 min/line",
            "Products Destroyed": "1,109/yr",
            "End-Customer Satisfaction": "AFNOR N/A",
        },
        "ishikawa": {
            "Manpower": "Small team (5 people).",
            "Methods": "Access-based returns process, not exploitable.",
            "Machines": "No analytical CRM for after-sales.",
            "Environment": "Variable shipping quality from agencies.",
            "Materials": "Non-poka-yoke packaging (quantity errors).",
        },
        "five_why": [
            "Why 2.598% return rate? -> Preparation/quantity errors.",
            "Why preparation errors? -> Non-standard control rules.",
            "Why no standard? -> No VoC/NPS framework.",
            "Why no VoC? -> Process internally focused, not customer-centric.",
            "Why not customer-centric? -> Satisfaction data not captured.",
        ],
        "muda": ["Defects", "Waiting", "Motion"],
        "annual_current_cost": 2_000_000,
        "actions": [
            "Quarterly B2B customer VoC",
            "Lean Office for returns (13.17 -> 6 min)",
            "SAV CRM with analytics",
            "Poka-Yoke packaging",
            "Quarterly NPS + real-time dashboard",
        ],
        "investment": 70_000,
        "future": {
            "Return Rate": "1.2%",
            "Processing Time": "6 min/line",
            "Agency Claims": "1.5%",
            "Export Claims": "3%",
            "Annual Gain": "€1.2M",
            "Payback": "< 2 months",
        },
        "gain": 1_200_000,
        "payback": "< 2 months",
        "vsm_before": """Agency Return -> Manual Check -> Access Entry -> Validation -> Restock/Destroy
              [13.17 min]            [data not used]      [high claims]""",
        "vsm_after": """Agency Return -> CRM Scan -> Lean Office Rules -> Auto Decision -> Fast Restock
              [6 min]                 [real-time dashboard]    [NPS tracked]""",
        "roi_hypothesis": "Reduction in direct SAV cost + fewer destructions + lower claims.",
        "risks": "Team workload during transition; mitigated via pilot on 2 agencies then rollout.",
    },
    {
        "name": "4) Invoicing",
        "priority": "quick",
        "current_kpis": {
            "Invoices/yr": "65,250",
            "Order Cost": "€240",
            "DSO": "62 days",
            "Cash-to-Cash": "68 days",
            "NWC (DSO-DPO)": "32 days",
            "Invoicing Mode": "Paper + double check",
        },
        "ishikawa": {
            "Manpower": "Unnecessary double invoice check.",
            "Methods": "Late-year chasing and disputes.",
            "Machines": "No EDI billing or Factur-X.",
            "Environment": "Dependency on B2B agency lead times.",
            "Materials": "Transport data integrated too late.",
        },
        "five_why": [
            "Why DSO at 62 days? -> Paper sending + slow workflow.",
            "Why slow workflow? -> Systematic double check.",
            "Why double check? -> Legacy risk process.",
            "Why no digitalisation? -> EDI/e-invoicing not deployed.",
            "Why not deployed? -> Cash governance insufficiently prioritised.",
        ],
        "muda": ["Overprocessing", "Waiting", "Motion"],
        "annual_current_cost": 15_660_000,
        "actions": [
            "Factur-X electronic invoicing",
            "Remove double check",
            "Agency invoicing EDI",
            "1% discount for payment < 15 days",
            "Automated monthly transport rebilling",
            "Poka-Yoke ERP data validation",
        ],
        "investment": 60_000,
        "future": {
            "DSO": "35 days",
            "Cash-to-Cash": "30 days",
            "Order Cost": "€150",
            "One-shot Cash": "+€62M",
            "Annual Gain": "€5.9M",
            "Payback": "4 days",
        },
        "gain": 5_900_000,
        "payback": "4 days",
        "vsm_before": """Order -> Invoice Preparation -> Double Check -> Postal Send -> Client Payment
           [validation delays]      [mail]                [DSO 62d]""",
        "vsm_after": """Order -> Auto Factur-X -> Agency EDI -> Digital Chase -> Accelerated Payment
           [integrated control]         [real time]              [DSO 35d]""",
        "roi_hypothesis": "Lower process cost + faster collection + NWC reduction.",
        "risks": "EDI partner compatibility; mitigated via 3-month dual-run phase.",
    },
    {
        "name": "5) Data & Integration",
        "priority": "long",
        "current_kpis": {
            "ERP": "In-house, last updated 2020",
            "Integrations": "No EDI/WMS/CRM",
            "Transport": "Data not analysed",
            "Inventory Discrepancies": "442/yr not analysed",
            "Forecast": "Module barely used",
            "Customer Satisfaction": "AFNOR N/A",
        },
        "ishikawa": {
            "Manpower": "Heterogeneous data culture by department.",
            "Methods": "No shared scorecard.",
            "Machines": "Siloed application architecture.",
            "Environment": "Decentralised multi-site management.",
            "Materials": "Incomplete data quality (weight/dimensions).",
        },
        "five_why": [
            "Why siloed management? -> Disconnected sources.",
            "Why disconnected? -> No central data lake.",
            "Why no data lake? -> Investment deferred.",
            "Why deferred? -> Cross-functional ROI poorly formalised.",
            "Why poorly formalised? -> Lack of dedicated data governance.",
        ],
        "muda": ["Inventory", "Waiting", "Defects", "Overprocessing", "Motion"],
        "annual_current_cost": 3_000_000,
        "actions": [
            "Central Data Lake / Data Warehouse",
            "Function-level BI dashboards",
            "Kaplan Balanced Scorecard",
            "ERP-carrier API",
            "Agency CRM + B2B portal",
            "Integrated WMS + collaborative forecast",
            "Poka-Yoke data quality",
        ],
        "investment": 230_000,
        "future": {
            "Transport Cost/km": "€0.95",
            "Forecast Accuracy": "85%",
            "Visibility": "Real-time",
            "ISO Compliance": "Compliant",
            "Annual Gain": "€5-8M",
            "Payback": "6 months",
        },
        "gain": 5_000_000,
        "payback": "6 months",
        "vsm_before": """ERP silo -> Manual Exports -> Dept Files -> Late Decision
           [no CRM/WMS]          [no API]                [reactive actions]""",
        "vsm_after": """ERP + CRM + WMS -> Data Lake -> BI Dashboard -> Data Quality Alerts -> Data-driven Decision
           [integrated flow]            [real time]               [proactive management]""",
        "roi_hypothesis": "Transport optimisation + reduced safety stock + overall productivity.",
        "risks": "IS integration complexity; mitigated via modular quarterly roadmap.",
    },
]

tabs = st.tabs(["Current State", "Future State", "ROI & Results"])

with tabs[0]:
    st.header("Current State - Diagnosis of 5 Key Issues")
    st.caption("Lean Six Sigma analysis: KPI sheet, Ishikawa 5M, 5 Whys, MUDA and annual cost.")

    for p in problems:
        with st.expander(p["name"], expanded=False):
            c1, c2 = st.columns([1, 1])
            with c1:
                st.subheader("Diagnostic Sheet")
                st.dataframe(pd.DataFrame([p["current_kpis"]]), use_container_width=True)
                st.markdown("**MUDA Wastes Identified:** " + ", ".join(p["muda"]))
                st.markdown(
                    f"**Estimated Annual Cost (losses):** :red[{p['annual_current_cost'] / 1_000_000:.2f} MEUR/yr]"
                )
            with c2:
                st.subheader("Ishikawa 5M (Root Cause)")
                for key, value in p["ishikawa"].items():
                    st.markdown(f"- **{key}** : {value}")

            st.subheader("5 Whys")
            for why in p["five_why"]:
                st.markdown(f"- {why}")

            st.subheader("VSM ASCII - Current State")
            st.code(p["vsm_before"], language="text")

with tabs[1]:
    st.header("Future State - Simulated Lean Solutions")
    st.caption("Kaizen actions, Poka-Yoke, target KPIs, future VSM, ROI and deployment plan.")

    for p in problems:
        with st.expander(p["name"], expanded=False):
            if p["priority"] == "quick":
                st.markdown("<span class='tag-quick-win'>Quick Win</span>", unsafe_allow_html=True)
            elif p["priority"] == "mid":
                st.markdown("<span class='tag-mid'>Mid-term</span>", unsafe_allow_html=True)
            else:
                st.markdown("<span class='tag-long'>Long-term</span>", unsafe_allow_html=True)

            st.subheader("Kaizen Actions")
            for action in p["actions"]:
                st.markdown(f"- {action}")

            st.subheader("Target Indicators (Before/After)")
            before = pd.Series(p["current_kpis"], name="Before")
            after = pd.Series(p["future"], name="After")
            comp = pd.concat([before, after], axis=1).fillna("-")
            st.dataframe(comp, use_container_width=True)

            st.subheader("VSM ASCII - Future State")
            st.code(p["vsm_after"], language="text")

            roi = p["gain"] / p["investment"]
            st.success(
                f"Annual Gain: {p['gain'] / 1_000_000:.1f} MEUR | Investment: {p['investment'] / 1000:.1f} k€ | ROI: {roi:.1f}x | Payback: {p['payback']}"
            )

            with st.expander("Detailed ROI Calculation (assumptions + formula)"):
                st.markdown(f"- **Main Assumption**: {p['roi_hypothesis']}")
                st.markdown(
                    f"- **ROI Formula**: (Annual Gain - Investment) / Investment = ({p['gain']:,} - {p['investment']:,}) / {p['investment']:,}"
                )
                st.markdown(f"- **Calculated ROI**: {(p['gain'] - p['investment']) / p['investment']:.2f}x")
                st.markdown(f"- **Announced Payback**: {p['payback']}")
                st.markdown(f"- **Main Risk & Mitigation**: {p['risks']}")

    gantt_df = pd.DataFrame(
        [
            ("Kanban + Cycle Counting", "2023-01-01", "2023-06-30", "Stock"),
            ("Supplier EDI", "2023-01-15", "2023-07-15", "Supply"),
            ("VoC + SAV CRM", "2023-04-01", "2023-09-30", "SAV"),
            ("Electronic Invoicing", "2023-02-01", "2023-08-31", "Invoicing"),
            ("Data Lake + WMS + CRM", "2023-01-01", "2023-12-31", "Data"),
            ("Stabilisation & Standardisation", "2023-10-01", "2023-12-31", "Cross-functional"),
        ],
        columns=["Step", "Start", "End", "Stream"],
    )
    fig_gantt = px.timeline(
        gantt_df,
        x_start="Start",
        x_end="End",
        y="Step",
        color="Stream",
        title="Simulated Gantt Deployment Plan - 2023",
    )
    fig_gantt.update_yaxes(autorange="reversed")
    st.plotly_chart(fig_gantt, use_container_width=True)

with tabs[2]:
    st.header("ROI & Results")
    st.caption("Financial summary, impact details, CEO objective attainment and compliance.")

    summary_df = pd.DataFrame(
        [
            ["Inventory Management", "€50k", "€4.8M", "96x", "< 1 month"],
            ["Supply Chain", "€80.4k", "€8.9M", "110x", "4 days"],
            ["After-Sales Service", "€70k", "€1.2M", "17x", "< 2 months"],
            ["Invoicing", "€60k", "€5.9M + €62M (one-shot)", "98x + cash", "4 days"],
            ["Data & Integration", "€230k + €80k/yr", "€5-8M", "~25x", "6 months"],
            ["TOTAL", "€490.4k", "€25.8M/yr + €62M", "avg 70x", "< 3 months"],
        ],
        columns=["Issue", "Investment", "Annual Gain", "ROI", "Payback"],
    )
    st.subheader("Summary Table — 5 Key Issues")
    st.dataframe(summary_df, use_container_width=True)

    st.subheader("Impact Detail by Action")
    selected = st.selectbox("Select an issue", [p["name"] for p in problems])
    p_sel = next(p for p in problems if p["name"] == selected)
    impacts = []
    for idx, action in enumerate(p_sel["actions"], start=1):
        impacts.append(
            {
                "Action": action,
                "Target Indicator": list(p_sel["future"].keys())[min(idx - 1, len(p_sel["future"]) - 1)],
                "Before/After": f"{list(p_sel['current_kpis'].values())[0]} -> {list(p_sel['future'].values())[min(idx - 1, len(p_sel['future']) - 1)]}",
                "Attributed Gain": f"{p_sel['gain'] / max(len(p_sel['actions']),1) / 1_000_000:.2f} M€/yr",
            }
        )
    st.dataframe(pd.DataFrame(impacts), use_container_width=True)

    st.subheader("CEO Summary")
    st.success(
        "The 5 proposed initiatives generate over €25M in annual gains for a total investment of under €500k, "
        "with an average return on investment of under 3 months. Cash flow is strengthened by €62M from the first year. "
        "All 2022 CEO strategic objectives are met or exceeded."
    )

    objectives_df = pd.DataFrame(
        [
            ("+5% Net Revenue", 108),
            ("-20% Inventory", 195),
            ("-9% Transport Cost", 233),
            ("Cash-to-Cash 30d", 100),
            ("+9% Customer Retention", 112),
        ],
        columns=["CEO Objective", "Achievement (%)"],
    )
    fig_obj = px.bar(
        objectives_df,
        x="CEO Objective",
        y="Achievement (%)",
        color="Achievement (%)",
        color_continuous_scale=["#f59e0b", "#22c55e"],
        title="CEO Objective Achievement Gauge",
        range_y=[0, 240],
    )
    st.plotly_chart(fig_obj, use_container_width=True)

    st.subheader("Compliance")
    st.markdown("**Badges:** ✅ ASLOG   |   ✅ ISO 9001   |   ✅ SCOR v12")
    check_df = pd.DataFrame(
        [
            ("ASLOG", "Flow management, process standardisation", "OK"),
            ("ISO 9001", "Continuous improvement loop, customer satisfaction", "OK"),
            ("SCOR v12", "KPIs plan-source-make-deliver-return", "OK"),
        ],
        columns=["Standard", "Points Verified", "Status"],
    )
    st.table(check_df)

st.markdown("<div class='footer'>Lean Six Sigma Project - Dyntech 2022</div>", unsafe_allow_html=True)
