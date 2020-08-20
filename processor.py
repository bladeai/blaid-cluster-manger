from base import BaseModel
import asyncio

class AsyncProcessor(BaseModel):
    """docstring for AsyncProcessor."""

    def __init__(self, data):
        super(AsyncProcessor, self).__init__(data)

    async def _read_stream(self, stream, cb):
        while True:
            line = await stream.readline()
            if line:
                cb(line)
            else:
                break

    async def _stream_subprocess(self, cmd, stdout_cb, stderr_cb):
        process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE)

        await asyncio.wait([
            self._read_stream(process.stdout, stdout_cb),
            self._read_stream(process.stderr, stderr_cb)
        ])
        return await process.wait()


    def execute(self, cmd, stdout_cb, stderr_cb):
        loop = asyncio.get_event_loop()
        rc = loop.run_until_complete(
            self._stream_subprocess(
                cmd,
                stdout_cb,
                stderr_cb,
        ))
        loop.close()
        return rc
