from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    """counter that remembers the order of elements as first seen"""
    # def __repr__(self):
    #     return "{}({})".format(self.__class__.__name__, OrderedDict(self))
    #
    # def __reduce__(self):
    #     return  self.__class__, (OrderedDict(self),)

oc = OrderedCounter("abracadabra")
print(oc)
