import click

from improvado.clients.vk_client import VkClient
from improvado.config import settings
from improvado.exceptions import BadIDType
from improvado.logger import logger
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
@click.option("-o", "--output", 'output_file', required=True)
@click.option('--quiet', default=True, is_flag=True)
def cli_command(user_id, report_type, output_file, quiet):
    if quiet:
        logger.level("INFO")
    else:
        logger.level("DEBUG")

    if not user_id.isdigit():
        raise BadIDType(type(user_id), user_id)

    with VkClient(
        token=settings.TOKEN
    ) as client:
        logger.info(f"user_id: {user_id}")
        logger.info(f"report type: {report_type.name}")

        report_generator_class = get_report_generator(report_type)
        report_generator = report_generator_class(client=client)
        report = report_generator.generate_report(user_id)
        filename = f"{output_file}.{report_type.name}"
        with open(filename, "w", newline="", encoding="utf-8") as file:
            file.write(report.read())
        click.echo(f"Report file has been generated to {filename}")


if __name__ == "__main__":
    cli_command()
