import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import networkx as nx
import plotly.graph_objs as go


app = dash.Dash(__name__)
G = nx.karate_club_graph()
app.layout = html.Div([
    dcc.Graph(id='network-graph')
])


@app.callback(
    Output('network-graph', 'figure'),
    Input('network-graph', 'relayoutData')  # This can be replaced with other inputs
)
def update_graph(relayoutData):
    # Create Plotly figure from NetworkX graph
    pos = nx.spring_layout(G)  # Layout algorithm (e.g., spring_layout, circular_layout)
    edge_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace['x'] += (x0, x1, None)
        edge_trace['y'] += (y0, y1, None)

    node_trace = go.Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            )
        )
    )

    for node in G.nodes():
        x, y = pos[node]
        node_trace['x'] += (x,)
        node_trace['y'] += (y,)
        node_trace['text'] += (f'Node {node}',)

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=0),
                        height=800
                    ))

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
