# -*- coding: utf-8-*-
from wakeonlan import wol
import re

WORDS = ["WAKE", "UP"]


def handle(text, mic, profile):
    """
        Responds to user-input.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    wol.send_magic_packet(profile['wakeup']['PC'])

    mic.say("Starting PC")


def isValid(text):
    """
        Returns True if the input is related to this plugin.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\wake up\b', text, re.IGNORECASE))
