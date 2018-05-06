import unittest

from commonSpiders.utils.server_utils import get_mac_address, get_guid_by_mac


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    # def test_get_mac_address(self):
    #     mac = get_mac_address()
    #     print mac

    def test_get_guid(self):
        aa = get_guid_by_mac('defual')
        print aa


if __name__ == '__main__':
    unittest.main()
