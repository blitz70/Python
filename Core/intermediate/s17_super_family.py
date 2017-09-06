# Method resolution order
# https://www.youtube.com/watch?v=EiOglTERPEo

class Adam(object): pass
class Eve(object): pass
class CMK(Adam, Eve): pass
class WKN(Adam, Eve): pass
class SKK(CMK, WKN): pass
class OSK(Adam, Eve): pass
class ISB(Adam, Eve): pass
class OJE(OSK, ISB): pass
class Curie(SKK, OJE): pass

help(Curie)