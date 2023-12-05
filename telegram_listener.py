from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import InputMediaPhoto
import helpers


class TelegramListener:
    def __init__(self):
        self.api_id = 13418929  # yussef_dev
        self.api_hash = "1a4781dc5b7bc4e7155c0d4f3c7a455f"
        self.CHAT_IDs = ['fx_news_34', 'me']
        self.target = 'Stock_market_earnings1'
        self.app = None

    async def run(self):
        try:
            # Create a Pyrogram client
            self.app = Client('my_account', api_id=self.api_id, api_hash=self.api_hash)

            # Define the message handler with the specific filters for each chat ID

            @self.app.on_message(filters.chat(self.CHAT_IDs))
            async def handle_message(client, message):
                # Call the message handler function passed during instance creation
                await self.message_handler(message)

            # Start the client asynchronously
            await self.app.start()
        except RPCError as e:
            print(f"An error occurred: {e}")

    async def stop(self):
        # Stop the client gracefully
        if self.app is not None:
            await self.app.stop()

    async def message_handler(self, message):

        if message.text:
            if helpers.filter_msg(message.text): return
            formatted_msg = helpers.format_msg(message.text)
            await self.send_text(self.target, formatted_msg)

        elif message.photo:
            formatted_caption = ''
            if message.caption:
                if helpers.filter_msg(message.caption): return
                formatted_caption = helpers.format_msg(message.caption)
            await self.send_photo(self.target, message.photo.file_id, formatted_caption)
        elif message.video:
            formatted_caption = ''
            if message.caption:
                if helpers.filter_msg(message.caption): return
                formatted_caption = helpers.format_msg(message.caption)
            await self.send_video(self.target, message.video.file_id, formatted_caption)

    async def send_text(self, target, text):
        try:
            await self.app.send_message(chat_id=target, text=text, disable_web_page_preview=True)
            print('successfully text sent!')
        except RPCError as e:
            print(e)

    async def send_photo(self, target, file_id_or_url, caption):
        try:
            await self.app.send_photo(chat_id=target, photo=file_id_or_url, caption=caption)
            print('Successfull photo sent!')
        except RPCError as e:
            print(e)

    async def send_video(self, target, file_id_or_url, caption):
        try:
            await self.app.send_video(chat_id=target, video=file_id_or_url, caption=caption)
            print('Succefull video sent!')
        except RPCError as e:
            print(e)
