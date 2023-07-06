import asyncio
import u6

d=u6.U6()
print(asyncio.run(d.configU6()))

d.close()