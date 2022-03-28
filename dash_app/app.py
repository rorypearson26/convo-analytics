from dash_app.main_dash import app
from dash_app.main_layout import create_main_layout

if __name__ == "__main__":
    app.layout = create_main_layout()
    app.run_server(debug=True)
