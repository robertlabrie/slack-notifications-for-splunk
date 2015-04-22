#!/usr/bin/env python
"""Splunk App for Slack."""

__author__ = 'Greg Albrecht <gba@onbeep.com>'
__copyright__ = 'Copyright 2014 OnBeep, Inc.'
__license__ = 'Apache License, Version 2.0'


from .slack import (SlackException, Slack, extract_events,  # NOQA
    trigger_slack, get_slack_chat_url)
