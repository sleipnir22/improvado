from aiohttp import ClientSession

from improvado.clients.vk_client import VkClient
from improvado.dataschemas.user_info import UserInfo
from improvado.services.base import ReportGenerator


def main():
    async with VkClient(VkClient.create_session(ClientSession)) as client:
        csv = ReportGenerator().create_report()
    return csv

