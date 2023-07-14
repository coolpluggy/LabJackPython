import asyncio
from lj_cp import u6
import sys

async def main():
    print(sys.path)
    d=u6.U6(autoOpen = False)
    await d.open()
    print(await d.configU6())

    d.close()

if __name__ == "__main__":
    asyncio.run(main())