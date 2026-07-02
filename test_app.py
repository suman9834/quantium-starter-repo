import pytest
from dash.testing.application_runners import import_app
from webdriver_manager.chrome import ChromeDriverManager
import os

# ChromeDriver auto download
os.environ["PATH"] += os.pathsep + os.path.dirname(ChromeDriverManager().install())

# App import
app = import_app("app")


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal(
        "h1",
        "Pink Morsels Sales Visualiser",
        timeout=10
    )


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-chart", timeout=10)


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)