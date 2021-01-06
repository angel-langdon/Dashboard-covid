from server import app, server
from layout import layout
import platform

app.layout = layout

app.title = 'Dashboard COVID-19'
if __name__ == "__main__":
    if platform.system() in ('Darwin', 'Windows') :
        debug = True
    else:
        debug = False
    app.run_server(debug=debug)
