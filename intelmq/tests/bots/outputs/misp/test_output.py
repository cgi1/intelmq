# -*- coding: utf-8 -*-
import os
import unittest

import intelmq.lib.test as test
from intelmq.bots.outputs.misp.output import MispOutputBot


INPUT1 = {"__type": "Event",
          "source.ip": "75.127.10.159",
          "source.fqdn": "www.appleid.apple.com.service-mamang-secure.tk",
          "source.geolocation.longitude": -78.8781,
          "source.asn": 36352,
          "feed.accuracy": 100.0,
          "time.observation": "2018-02-27T08:47:13+00:00",
          "time.source": "2018-02-27T09:47:09+00:00",
          "source.geolocation.cc": "US",
          "source.geolocation.city": "Buffalo",
          "source.geolocation.latitude": 42.8864,
          "feed.name": "CertStream",
          "source.network": "75.127.10.0/23"
          }

OUTPUT1 = {"__type": "Event",
          "source.ip": "75.127.10.159",
          "source.fqdn": "www.appleid.apple.com.service-mamang-secure.tk",
          "source.geolocation.longitude": -78.8781,
          "source.asn": 36352,
          "feed.accuracy": 100.0,
          "time.observation": "2018-02-27T08:47:13+00:00",
          "time.source": "2018-02-27T09:47:09+00:00",
          "source.geolocation.cc": "US",
          "source.geolocation.city": "Buffalo",
          "source.geolocation.latitude": 42.8864,
          "feed.name": "CertStream",
          "source.network": "75.127.10.0/23"
          }

class TestMispOutputBot(test.BotTestCase, unittest.TestCase):

    @classmethod
    def set_bot(cls):
        cls.bot_reference = MispOutputBot
        cls.default_input_message = INPUT1

    def test_event(self):
        self.run_bot()
        result = self.db['events'].find_one_and_delete({"source.asn": 64496})
        del result['_id']
        self.assertDictEqual(OUTPUT1, result)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
