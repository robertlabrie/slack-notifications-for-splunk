#!/usr/bin/env python

"""Slack Splunk Setup REST Handler."""

__author__ = 'Greg Albrecht <gba@onbeep.com>'
__copyright__ = 'Copyright 2014 OnBeep, Inc.'
__license__ = 'Apache License, Version 2.0'


import os
import logging
import shutil

import splunk.admin


class ConfigSlackApp(splunk.admin.MConfigHandler):

    """Slack Splunk Setup REST Handler."""

    def setup(self):
        if self.requestedAction == splunk.admin.ACTION_EDIT:
            self.supportedArgs.addOptArg('api_key')

    def handleList(self, confInfo):
        conf = self.readConf('slack')
        if conf is not None:
            for stanza, settings in conf.items():
                for key, val in settings.items():
                    confInfo[stanza].append(key, val)

    def handleEdit(self, confInfo):
        del confInfo
        if self.callerArgs.data['api_key'][0] in [None, '']:
            self.callerArgs.data['api_key'][0] = ''

        self.writeConf('slack', 'slack_config', self.callerArgs.data)
        install_slack_py(os.environ.get('SPLUNK_HOME'))


def install_slack_py(splunk_home):

    """Copies slack.py to Splunk's bin/scripts directory."""

    script_src = os.path.join(
        splunk_home, 'etc', 'apps', 'slack-notifications-for-splunk', 'bin',
        'slack.py')
    script_dest = os.path.join(splunk_home, 'bin', 'scripts')

    logging.info(
        'Copying script_src=%s to script_dest=%s', script_src, script_dest)
    shutil.copy(script_src, script_dest)


if __name__ == '__main__':
    splunk.admin.init(ConfigSlackApp, splunk.admin.CONTEXT_NONE)
