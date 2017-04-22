# struct : bytes data

import struct

# convert data to bytes format
format1 = 'iiif'
data1 = [5, 18, 33, 6.72]
data2 = struct.pack(format1, *data1)
print(data2)
print(struct.calcsize('i'), struct.calcsize('f'))
print(struct.calcsize(format1))

# convert data to normal format
data3 = struct.unpack(format1, data2)
print(data3)
print(struct.unpack(format1, b'\x05\x00\x00\x00\x12\x00\x00\x00!\x00\x00\x00=\n\xd7@'))
