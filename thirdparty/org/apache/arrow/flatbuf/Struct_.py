# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers

# /// A Struct_ in the flatbuffer metadata is the same as an Arrow Struct
# /// (according to the physical memory layout). We used Struct_ here as
# /// Struct is a reserved word in Flatbuffers
class Struct_(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsStruct_(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Struct_()
        x.Init(buf, n + offset)
        return x

    # Struct_
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def Struct_Start(builder): builder.StartObject(0)
def Struct_End(builder): return builder.EndObject()
