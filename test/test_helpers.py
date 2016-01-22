from twisted.internet import defer
from txhelpers import then
from twisted.trial import unittest

defer.Deferred.then = then

def return_value(value):
    return value
            
class OperatorTest(unittest.TestCase):
    def test_then(self):
        test_d = defer.succeed(2)
        test_d.then(return_value, 3)
        test_d.addCallback(self.assertEquals, 3)
        return test_d

    def test_then_unbound(self):
        test_d = defer.succeed(2)
        then(test_d, return_value, 3)
        test_d.addCallback(self.assertEquals, 3)
        return test_d