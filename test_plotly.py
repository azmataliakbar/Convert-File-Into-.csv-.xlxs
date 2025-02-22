import plotly.graph_objects as go

# Create a simple line plot
fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[4, 1, 2], mode='lines'))
fig.show()