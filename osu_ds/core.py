# coding=utf-8
import logging
from .connector import OsuConnector
from .utils import Endpoints, Modes
from .osutypes import User

__author__ = "DefaltSimon"

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class OsuApi:
    def __init__(self, api_key):
        """
        Creates an Osu instance to connect to osu!api
        :param api_key: the api key gotten from https://osu.ppy.sh/p/api
        :type api_key: str
        """
        self.api_key = str(api_key)

        self.req = OsuConnector(self.api_key)
        log.debug("Ready")

    def get_user(self, username, mode=Modes.OSU, history=1):
        payload = dict(
            u=str(username),
            m=mode,
            type="id" if isinstance(username, int) else "string",
            event_days=history,
        )

        return self._handle_user(Endpoints.USER, payload)

    def _handle_user(self, endpoint, payload):
        data = self.req.get(endpoint, payload)

        if not data:
            return None

        # One-item list is returned by the api so we flatten it out
        return User(data[0])
