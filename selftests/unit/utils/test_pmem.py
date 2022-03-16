import unittest.mock

from afutils import pmem


class PMem(unittest.TestCase):

    def test_no_binaries(self):
        with unittest.mock.patch('afutils.path.find_command',
                                 return_value=False):
            with self.assertRaises(pmem.PMemException):
                pmem.PMem()


if __name__ == '__main__':
    unittest.main()
