import matplotlib.pyplot as plt
import seaborn as sns
import plotly.io as pio
import plotly.graph_objects as go


sns.set_theme(
    style='white',
    font='Serif',
    rc={
    'figure.figsize': [10, 5],
    'figure.facecolor': 'white',
    'figure.titlesize': 12,
    'axes.axisbelow': False,
	'axes.edgecolor': 'lightgrey',
	'axes.facecolor': 'None',
	'axes.grid': False,
	'axes.labelcolor': 'black',
    'axes.labelsize': 10,
	'axes.spines.right': False,
	'axes.spines.top': False,
	'lines.solid_capstyle': 'round',
	'patch.edgecolor': 'w',
	'patch.force_edgecolor': True,
	'text.color': 'black',
	'xtick.bottom': False,
	'xtick.color': 'black',
	'xtick.direction': 'out',
	'xtick.top': False,
    'xtick.labelsize': 8,
	'ytick.color': 'black',
	'ytick.direction': 'out',
	'ytick.left': False,
	'ytick.right': False,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'legend.title_fontsize': 10,
    'legend.frameon': False
    }
)


PLOTLY_TEMP = go.layout.Template(
    layout=dict(
        title_x=.042,
        title=dict(font={'size': 14, 'color': 'white'}),
        legend=dict(
            font=dict({'size': 8, 'color': 'white'}),
            title=dict(font=dict(size=10)),
            borderwidth=0,
        ),
        xaxis=dict(
            tickfont=dict(size=10),
            linewidth=1,
            ticklen=5,
            tickwidth=1,
            tickcolor='white',
            showgrid=False
        ),
        yaxis=dict(
            tickfont=dict(size=10),
            linewidth=1,
            ticklen=5,
            tickwidth=1,
            tickcolor='white',
            showgrid=False
        ),
        margin=dict(l=60, r=40, t=50, b=50),
        plot_bgcolor='black',
        paper_bgcolor='black',
    )
)

# custom_dark = pio.templates['plotly_dark'].layout
# pio.templates.default = 'custom_black'
