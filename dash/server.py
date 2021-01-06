#!/usr/bin/env python
# coding: utf-8
import dash

app = dash.Dash(__name__,
                url_base_pathname='/dashboard/covid-19-spain/')

server = app.server