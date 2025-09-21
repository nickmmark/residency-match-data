# US Residency Applicants (2025) Sankey as a self-contained HTML
# Data source: NRMP Match (https://www.nrmp.org/match-data-analytics/)
# Author: Nick Mark, MD (@nickmmark)

import pandas as pd
import plotly.graph_objects as go

# --------------------------- Data (NRMP 2025) ---------------------------
data = {
    "Applicant Group": [
        "U.S. MD senior applicants",
        "U.S. DO senior applicants",
        "U.S.-citizen IMG applicants",
        "Non-U.S.-citizen IMG applicants",
    ],
    "Applicants": [20368, 8392, 4587, 11465],
    "Matched PGY-1": [19044, 7773, 3108, 6653],
}
df = pd.DataFrame(data)
df["Unmatched"] = df["Applicants"] - df["Matched PGY-1"]
df["Match rate"] = df["Matched PGY-1"] / df["Applicants"]
df["Unmatch rate"] = df["Unmatched"] / df["Applicants"]

# Totals
pgy1_offered  = 40041
pgy1_filled   = 37667
pgy1_unfilled = pgy1_offered - pgy1_filled  # 2,374
other_matched = int(pgy1_filled - df["Matched PGY-1"].sum())
total_unmatched = int(df["Unmatched"].sum())

# --------------------------- Nodes & Labels ---------------------------
# Indices (including invisible anchor at end)
US_MD, US_DO, US_IMG_US, IMG_NONUS, OTHER_APPS, MATCHED, UNFILLED_MID, UNMATCHED, PGY1_OFFERED, ANCHOR = range(10)

node_labels = [
    f"{df.loc[0,'Applicant Group']} ({df.loc[0,'Applicants']:,})",
    f"{df.loc[1,'Applicant Group']} ({df.loc[1,'Applicants']:,})",
    f"{df.loc[2,'Applicant Group']} ({df.loc[2,'Applicants']:,})",
    f"{df.loc[3,'Applicant Group']} ({df.loc[3,'Applicants']:,})",
    f"Other applicants (matched {other_matched:,})",
    f"Matched to PGY1 positions ({pgy1_filled:,})",
    f"Unfilled positions ({pgy1_unfilled:,})",
    f"Unmatched ({total_unmatched:,})",
    f"PGY1 positions offered ({pgy1_offered:,})",
    "",  # invisible anchor
]

# Colors
COLOR_MATCHED_BLUE_LINK = "rgba(99, 155, 235, 0.55)"
COLOR_UNMATCHED_RED_LINK = "rgba(241, 99, 99, 0.65)"
COLOR_UNFILLED_GRAY_LINK = "rgba(160, 160, 160, 0.6)"
COLOR_NODE_GRAY = "rgba(180,180,180,0.55)"
COLOR_NODE_BLUE = "rgba(99, 155, 235, 0.85)"
COLOR_NODE_RED = "rgba(241, 99, 99, 0.85)"
COLOR_NODE_GRAY_DARK = "rgba(140,140,140,0.85)"
COLOR_TRANSPARENT = "rgba(0,0,0,0)"

node_colors = [
    COLOR_NODE_GRAY,      # US MD
    COLOR_NODE_GRAY,      # US DO
    COLOR_NODE_GRAY,      # US IMG US
    COLOR_NODE_GRAY,      # IMG non-US
    COLOR_NODE_GRAY,      # Other applicants
    COLOR_NODE_BLUE,      # Matched
    COLOR_NODE_GRAY_DARK, # Unfilled
    COLOR_NODE_RED,       # Unmatched
    COLOR_NODE_GRAY_DARK, # Offered
    COLOR_TRANSPARENT,    # Anchor
]

# Layout (snap + hint positions)
node_x = [0.0, 0.0, 0.0, 0.0, 0.0,   0.5, 0.5, 0.5,   1.0, 1.0]
node_y = [0.00, 0.14, 0.28, 0.42, 0.66,   0.10, 0.42, 0.74,   0.40, 0.95]

# --------------------------- Links ---------------------------
sources = []
targets = []
values  = []
link_colors = []
customdata_links = []
link_labels = []

def pct(x):
    return f"{x*100:.1f}%"

def add_flows(idx_node, row_idx):
    matched = int(df.loc[row_idx, "Matched PGY-1"])
    apps = int(df.loc[row_idx, "Applicants"])
    unmatched = apps - matched
    mrate = df.loc[row_idx, "Match rate"]
    urate = df.loc[row_idx, "Unmatch rate"]
    group_name = df.loc[row_idx, "Applicant Group"]

    # to Matched
    sources.append(idx_node); targets.append(MATCHED); values.append(matched)
    link_colors.append(COLOR_MATCHED_BLUE_LINK)
    link_labels.append(f"{matched:,} ({pct(mrate)})")
    customdata_links.append(f"{group_name} — {pct(mrate)} matched")

    # to Unmatched
    sources.append(idx_node); targets.append(UNMATCHED); values.append(unmatched)
    link_colors.append(COLOR_UNMATCHED_RED_LINK)
    link_labels.append(f"{unmatched:,} ({pct(urate)})")
    customdata_links.append(f"{group_name} — {pct(urate)} unmatched")

# Add flows in desired order
add_flows(US_MD, 0)
add_flows(US_DO, 1)
add_flows(US_IMG_US, 2)
add_flows(IMG_NONUS, 3)

# Other applicants -> Matched
sources.append(OTHER_APPS); targets.append(MATCHED); values.append(other_matched)
link_colors.append(COLOR_MATCHED_BLUE_LINK)
link_labels.append(f"{other_matched:,}")
customdata_links.append("Other applicants — matched")

# Middle → Right
sources.append(MATCHED); targets.append(PGY1_OFFERED); values.append(pgy1_filled)
link_colors.append(COLOR_MATCHED_BLUE_LINK)
link_labels.append(f"{pgy1_filled:,}")
customdata_links.append("PGY1 positions offered — matched")

sources.append(UNFILLED_MID); targets.append(PGY1_OFFERED); values.append(pgy1_unfilled)
link_colors.append(COLOR_UNFILLED_GRAY_LINK)
link_labels.append(f"{pgy1_unfilled:,}")
customdata_links.append("PGY1 positions offered — unfilled")

# Invisible links to anchor node keep the correct ordering
EPS = 1e-6
for left_node in [US_MD, US_DO, US_IMG_US, IMG_NONUS, OTHER_APPS]:
    sources.append(left_node); targets.append(ANCHOR); values.append(EPS)
    link_colors.append(COLOR_TRANSPARENT)
    link_labels.append("")
    customdata_links.append("")

# Node-level tooltip (right node: % filled + absolute counts)
node_customdata = [""] * len(node_labels)
percent_filled_text = f"{pct(pgy1_filled/pgy1_offered)} of positions filled"
abs_counts_text = f"{pgy1_filled:,} filled, {pgy1_unfilled:,} unfilled"
node_customdata[PGY1_OFFERED] = percent_filled_text + "<br>" + abs_counts_text

fig = go.Figure(data=[go.Sankey(
    arrangement="snap",
    valueformat=",",
    node=dict(
        label=node_labels,
        pad=28,
        thickness=24,
        color=node_colors,
        x=node_x,
        y=node_y,
        customdata=node_customdata,
        hovertemplate="%{label}<br>%{customdata}<extra></extra>"
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        label=link_labels,
        color=link_colors,
        customdata=customdata_links,
        hovertemplate="%{customdata}<extra></extra>"
    )
)])

# Annotations: headers + source/byline
annotations = [
    dict(text="<b>Applicants</b>", x=0.0, y=1.05, xref="paper", yref="paper",
         showarrow=False, font=dict(size=13, color="#444")),
    dict(text="<b>Outcomes</b>", x=0.5, y=1.05, xref="paper", yref="paper",
         showarrow=False, font=dict(size=13, color="#444")),
    dict(text="<b>PGY1 positions</b>", x=1.0, y=1.05, xref="paper", yref="paper",
         xanchor="right", showarrow=False, font=dict(size=13, color="#444")),
    dict(text='<span style="color:#999">Source: <a href="https://www.nrmp.org/match-data-analytics/" target="_blank">NRMP Match 2025</a> • By: Nick Mark, MD (@nickmmark)</span>',
         x=1.0, y=-0.08, xref="paper", yref="paper", xanchor="right", showarrow=False)
]

fig.update_layout(
    title_text="US Residency Applicants (2025)",
    font_size=12,
    margin=dict(l=20, r=20, t=80, b=80),
    height=860,
    annotations=annotations
)

# Save a self-contained HTML (inline plotly.js)
fig.write_html("/mnt/data/us_residency_applicants_2025_sankey_inline.html", include_plotlyjs=True, full_html=True)
print("Saved /mnt/data/us_residency_applicants_2025_sankey_inline.html")
