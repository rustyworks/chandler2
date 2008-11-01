import doctest, unittest, os
import pkg_resources

from test_birefs import *

def additional_tests():
    files = [f for f in pkg_resources.resource_listdir(__name__, '.') if f.endswith(".txt")]
    return doctest.DocFileSuite(optionflags=doctest.ELLIPSIS, *files)

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(additional_tests())
