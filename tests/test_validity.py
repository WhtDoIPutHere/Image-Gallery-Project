"""
Test for HTML requirements
"""
import pytest
from webcode_tk import html_tools as html
from webcode_tk import validator_tools as validator

project_dir = "project/"

html_validation_results = validator.get_project_validation(project_dir)
css_validation_results = validator.get_project_validation(
    project_dir, "css"
)

@pytest.fixture
def html_files():
    html_files = html.get_all_html_files(project_dir)
    return html_files


def test_passes_html_validation(html_files):
    errors = []
    if not html_files:
        assert "html files" in html_files
    for file in html_files:
        results = validator.get_markup_validity(file)
        for result in results:
            errors.append(result.get("message"))
    assert not errors


@pytest.mark.parametrize("results", css_validation_results)
def test_css_validation(results):
    assert "pass" == results[:4]
