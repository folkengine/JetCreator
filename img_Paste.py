#----------------------------------------------------------------------
# This file was generated by C:\Python25\Lib\site-packages\wx-2.8-msw-unicode\wx\tools\img2py.py
#
from wx import Image, Bitmap, EmptyIcon
import cStringIO, zlib


def getData():
    return zlib.decompress(
'x\xda\x01\xdd\x01"\xfe\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\
\x00\x00 \x08\x06\x00\x00\x00szz\xf4\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\
\x08d\x88\x00\x00\x01\x94IDATX\x85\xed\x97\xbdN\xc30\x14\x85OJ\x06gK6\x18;\
\xa6\x1bk^\xa1\x8fS\xb5\x08\x18\x10\x03c\x07\x84X\x902\xb6o\x90\x951\xdd\xca\
\xd6\x8c\x1e\x93\xcd\x06\x06\xdf\xad\x0c\xb4\x15HIs\x9dDD\x958[,\xfb\x9e/\
\xbe\xd7\x7f\x8e38C\x9fr\x01\xe0\xe9\xe5qKZw\x1cZ`:\xbbrX\x00\xa45&\x93\xdbN\
\xed\xe7\xf3\x07V?\xf7\xe7\x87\xeeh\x16|\xdfg\xf7\x1dt\xe2\xd8B\xff\x00nYc\
\x96e\x8d\x82\r\x87C\x08!\xda\x03\x84a\xd8\x08\xa0\x89N#\x05i\x9aB)\xb2\x0e~\
s}\xbf\x05\x80 \x00\xa6\xb3\xbb\xd2M\x89\x95\x82$y\x85\x94\xd6\xfe,\x9dF\n\
\xfe\x1c\xa0,\x05{\x8dF\xe7\x10\xc2\xab\rLd\xb0\xd9\x14\xcd\x00\x8e\xc9\x18\
\x821\x9c\x9e\xbc\xa2\xb5N\x81\xd6\xc4\nN\xccUS\x99\x02\xa2\xf2\x00ax\xc1\
\xda\xedV+\t\x98z\x88R\x80*s\x00H\xd3n\xd7\xe3/\x80c\xc6{\x8d\xc7\x97\xa8\
\x9b\x80\xf5ZBJ\xde\xdd\xc2\xba\x08\x93\xe4\xcdv\x08\x0f\x80\xf3\xf7\x00\x10\
E\xbc\x13\x8f\x88X\xe9\xb2\x9e\x81,\xcbm\x87t\x0b\xd0\xe4Pb\x01\x10\x91\xf5e\
\xa2L\x9e\x07\xf8>v\x85*vm\xd5\xd0;\x00\x818~nm\x0e|\x1bGQx\xb8\x19\x17E\x81\
<\xaf\xae\x05\x17@\xed\x03b\x7f\xae\xf3!\xc4\xc1\\)\x05)\xab\xeb\xc6\xba\x06\
8\xd2Z\xc3\x18\x03M\x1aRJ,\x16\x8bv\x00A\xc07\xf7< \xcfs(RX\xc6K(\xa5\xf0\
\xfe\xf1Y9\xc3N\xdf\x8f\xd3\xdeoD\xbd\x03|\x01\xd0i\x97\xf5j]\xc4\xe0\x00\
\x00\x00\x00IEND\xaeB`\x82q\x05\xc6\xef' )

def getBitmap():
    return Bitmap(getImage())

def getImage():
    stream = cStringIO.StringIO(getData())
    return Image(stream)

def getIcon():
    icon = EmptyIcon()
    icon.CopyFromBitmap(getBitmap())
    return icon

