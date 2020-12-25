#!/usr/bin/env python
# coding: utf-8
import dash
from layout import layout


app = dash.Dash(__name__)

app.layout = layout(app)

if __name__ == "__main__":
    app.run_server(debug=True)
