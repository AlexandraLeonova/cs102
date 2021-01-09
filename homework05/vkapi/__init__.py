from vkapi import config
from vkapi.session import Session  # type: ignore

session = Session(config.VK_CONFIG["domain"])
