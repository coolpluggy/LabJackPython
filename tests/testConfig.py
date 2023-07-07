import asyncio
from lj_cp import u6
import sys
print(sys.path)
d=u6.U6()
print(asyncio.run(d.configU6()))

d.close()