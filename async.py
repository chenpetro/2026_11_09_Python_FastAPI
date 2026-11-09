def name():
    return "name"


print(name)
print(name())

async def aname():
    return "async name"

async def main():
    print(aname)
    print(aname())
    print (await aname())
    print (name())

import asyncio
asyncio.run(main())