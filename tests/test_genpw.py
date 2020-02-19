# Copyright (C) 2020 Arrai Innovations Inc. - All Rights Reserved
from unittest import TestCase

from genpw import pronounceable_passwd


class TestGenPW(TestCase):
    def test_desired_length(self):
        for x in range(0, 32):
            pwd = pronounceable_passwd(x)
            self.assertEqual(len(pwd), max(x, 3))
