import asyncio
from telegram_listener import TelegramListener


async def main():
    listener = TelegramListener()

    try:
        # Start listening for messages
        await asyncio.gather(listener.run())

        # Wait for user interruption
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Stop the message listener
        await listener.stop()
        # await reactor.stop()


if __name__ == '__main__':
    asyncio.run(main())
