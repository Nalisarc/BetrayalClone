import unittests
import sys
from trator import housemap

class MapUnitTests(unittest.TestCase):

    def setUp(self):
        self.MAP = housemap.__init__()

    def test_check_connections(self):
        self.assertEqual(self.MAP['000'].edges['north'],MAP['001'])




if __name__ == '__main__':
    unittest.main()
    sys.exit()
