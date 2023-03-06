from improvado.services.base import ReportGenerator, ReportType

import typing as t

from improvado.utils import all_subclasses


def get_report_generator(report_type: ReportType) -> t.Type[ReportGenerator] | None:
    for class_ in all_subclasses(ReportGenerator):
        if class_.REPORT_TYPE == report_type:
            return class_
    return None
