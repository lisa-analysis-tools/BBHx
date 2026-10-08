"""BBHx's constants come from lisaconstants (2026-10-08).

C side: ``src/bbhx/cutils/constants.h`` (and the SOBBH kernel through it)
reads the generated ``lisaconstants_values.h`` (LAT's
``lisatools.utils.lisaconstants_header``); Python side: ``bbhx.utils.constants``
imports lisaconstants. Both are checked here against the installed package.
"""
import os
import unittest

import lisaconstants as lc
from lisatools.utils import lisaconstants_header as H

HEADER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "src", "bbhx", "cutils", "lisaconstants_values.h")


class LisaconstantsTest(unittest.TestCase):
    def test_committed_header_is_the_generated_one(self):
        with open(HEADER) as fh:
            text = fh.read()
        self.assertEqual(H.parse(text), H.expected_values())
        self.assertEqual(text, H.render())

    def test_python_constants_are_lisaconstants(self):
        from bbhx.utils import constants as K
        self.assertEqual(K.MSUN_SI, lc.SOLAR_MASS)
        self.assertEqual(K.YRSID_SI, lc.ASTRONOMICAL_YEAR)
        self.assertEqual(K.C_SI, lc.SPEED_OF_LIGHT)
        self.assertEqual(K.GMSUN, lc.SOLAR_MASS_PARAMETER)
        self.assertEqual(K.PC_SI, lc.PARSEC)
        self.assertEqual(K.MTSUN_SI, H.expected_values()["LISACONSTANTS_MTSUN"])


if __name__ == "__main__":
    unittest.main()
