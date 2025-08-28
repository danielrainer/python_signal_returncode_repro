#!/usr/bin/env python3

import asyncio


async def repro():
    proc = await asyncio.create_subprocess_shell("./sigint.sh")
    await proc.communicate()
    print(proc.returncode)
    assert proc.returncode == -2


asyncio.run(repro())
