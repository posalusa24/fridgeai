import threading
import asyncio
from bleak import BleakClient

UART_RX = '6e400002-b5a3-f393-e0a9-e50e24dcca9e'


class MicroBlue:
    def __init__(self, address):
        self.address = address
        self.data = {}
        self.sync_enabled = False
        self.sync_thread = threading.Thread(
            target=self._sync,
            args=(asyncio.get_event_loop(),)
        )

    def __enter__(self):
        self.start_sync()
        return self

    def __exit__(self, type, value, traceback):
        self.stop_sync()

    def start_sync(self):
        if self.sync_enabled:
            return
        self.sync_enabled = True
        self.sync_thread.start()

    def stop_sync(self):
        self.sync_enabled = False

    def get(self, key):
        try:
            return self.data[key]
        except KeyError:
            return None

    def _sync(self, async_loop):
        async def run():
            while self.sync_enabled:
                try:
                    async with BleakClient(self.address) as client:
                        def listener(sender, data):
                            key, value = data.decode().split(':')
                            self.data[key] = value
                        await client.start_notify(UART_RX, listener)
                        while self.sync_enabled:
                            await asyncio.sleep(1)
                        await client.stop_notify(UART_RX)
                        break
                except:
                    print("Retrying microbit connection...")
        asyncio.set_event_loop(async_loop)
        async_loop.run_until_complete(run())
