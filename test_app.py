import pytest
from dash.testing.application_runners import import_app
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def app(dash_duo):
    dash_app = import_app("app")  
    dash_duo.start_server(dash_app)
    return dash_duo

# Test on header
def test_header_is_present(app):
    header = WebDriverWait(app.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert header is not None
    assert "Pink Morsel Sales" in header.text

# Test on graphic
def test_graph_is_present(app):
    graph = WebDriverWait(app.driver, 10).until(
        EC.presence_of_element_located((By.ID, "sales_chart"))
    )
    assert graph is not None

# Test on select region
def test_region_picker_is_present(app):
    radio = WebDriverWait(app.driver, 10).until(
        EC.presence_of_element_located((By.ID, "region_selector"))
    )
    assert radio is not None
