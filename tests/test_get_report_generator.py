import pytest

from improvado.services.base import ReportType


@pytest.mark.parametrize(
    "report_type",
    [
        ReportType.csv,
        ReportType.tsv,
        ReportType.json
    ]
)
def test_get_report_generator(report_type):
    assert report_type in ReportType
