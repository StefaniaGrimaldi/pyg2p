import unittest
from pyg2p.util import strings


class TestStrings(unittest.TestCase):

    def test_to_argdict_for_short_options(self):
        d = strings.to_argdict(' -a foo -b bar')
        self.assertItemsEqual(d, {'-a': 'foo', '-b': 'bar'})

    def test_to_argdict_for_short_and_long_options(self):
        d = strings.to_argdict('-a foo --bar=baz')
        self.assertItemsEqual(d, {'-a': 'foo', '--bar': 'baz'})

    def test_to_argdict_for_odd_number_of_args(self):
        d = strings.to_argdict('a b c')
        self.assertItemsEqual(d, {'a': 'b'})
        # or maybe should raise exception?

    def test_to_argdict_for_empty_string(self):
        d = strings.to_argdict('')
        self.assertEqual(d, {})

