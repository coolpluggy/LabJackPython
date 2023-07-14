import asyncio
from lj_cp import u6, LabJackPython
import sys
print(sys.path)


async def main():
    qqq = LabJackPython.staticLib
    print(qqq)
    d=u6.U6(autoOpen = False)
    await d.open()
    print(d)
    d.close()

    # await asyncio.gather(LabJackPython.count(), LabJackPython.count(), LabJackPython.count())

if __name__ == "__main__":
    asyncio.run(main())