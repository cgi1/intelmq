# -*- coding: utf-8 -*-
"""
pymisp implementation for IntelMQ
@author: cgi1
"""

from intelmq.lib.bot import Bot

try:
    import pymisp
except ImportError:
    pymisp = None


class MispOutputBot(Bot):

    def init(self):
        if pymisp is None:
            self.logger.error('Could not import pymisp. Please install it.')
            self.stop()

        self.connect()


    def process(self):

        event = self.receive_message()

        try:

            misp_object = pymisp.AbstractMISPObjectGenerator()

            # search for attributes in event


        except :
            self.logger.error('Error creating misp_object.')

        else:
            self.acknowledge_message()


BOT = MispOutputBot
