import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import networkx as nx

# Plotly figure
def networkGraph(EGDE_VAR):

    edges = [[EGDE_VAR, 'B'], ['B', 'C'], ['B', 'D']]
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)

    # edges trace
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(color='black', width=1),
        hoverinfo='none',
        showlegend=False,
        mode='lines')

    # nodes trace
    node_x = []
    node_y = []
    text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        text.append(node)

    node_trace = go.Scatter(
        x=node_x, y=node_y, text=text,
        mode='markers+text',
        showlegend=False,
        hoverinfo='none',
        marker=dict(
            color='pink',
            size=50,
            line=dict(color='black', width=1)))

    # layout
    layout = dict(plot_bgcolor='white',
                  paper_bgcolor='white',
                  margin=dict(t=10, b=10, l=10, r=10, pad=0),
                  xaxis=dict(linecolor='black',
                             showgrid=False,
                             showticklabels=False,
                             mirror=True),
                  yaxis=dict(linecolor='black',
                             showgrid=False,
                             showticklabels=False,
                             mirror=True))

    # figure
    fig = go.Figure(data=[edge_trace, node_trace], layout=layout)

    return fig

# Dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Dash Networkx'

app.layout = html.Div([
        html.I('Write your EDGE_VAR'),
        html.Br(),
        dcc.Input(id='EGDE_VAR', type='text', value='K', debounce=True),
        dcc.Graph(id='my-graph'),
    ]
)

@app.callback(
    Output('my-graph', 'figure'),
    [Input('EGDE_VAR', 'value')],
)
def update_output(EGDE_VAR):
    return networkGraph(EGDE_VAR)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=1234)