# Copyright (C) 2020 Arrai Innovations Inc. - All Rights Reserved
from unittest import TestCase

from genpw import pronounceable_passwd


class TestGenPW(TestCase):
    def test_desired_length(self):
        for x in range(256, 0, -1):
            pwd = pronounceable_passwd(x)
            self.assertGreaterEqual(len(pwd), 3)
            self.assertLessEqual(len(pwd), max(x, 3))
