import click

from improvado.clients.vk_client import VkClient
from improvado.config import settings
from improvado.services.base import ReportType
from improvado.services.get_report_generator import get_report_generator


@click.command
@click.option(
    "-t",
    "--type",
    "report_type",
    required=True,
    type=click.Choice(
        [e for e in ReportType]
    )
)
@click.option("-id", "--user_id", "user_id", required=True)
@click.option("-o", "--output", 'output_file', required=True, type=click.File('w'))
def cli_command(user_id, report_type, output_file):
    with VkClient(
        token=settings.TOKEN
    ) as client:
        report_generator_class = get_report_generator(report_type)
        report_generator = report_generator_class(client=client)
        report = report_generator.generate_report(user_id)
        output_file.write(report.read())


if __name__ == "__main__":
    cli_command()