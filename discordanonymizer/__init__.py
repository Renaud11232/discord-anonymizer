import logging
import sys
import nextcord


class DiscordAnonymizer(nextcord.Client):

    def __init__(self, token, channel, log_level, watching):
        self.__logger = logging.getLogger("DiscordAnonymizer")
        self.__logger.setLevel(logging.getLevelName(log_level))
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)
        self.__logger.info("Initializing bot...")
        nextcord.Client.__init__(self)
        self.__token = token
        self.__channel = channel
        self.__watching = watching

    async def on_ready(self):
        self.__logger.info("Changing presence...")
        watching = nextcord.Activity(name=self.__watching, type=nextcord.ActivityType.watching)
        await self.change_presence(status=nextcord.Status.online, activity=watching)
        self.__logger.info("Bot is ready")

    async def on_message(self, message):
        if not message.guild:
            length = len(message.content)
            tts = message.tts
            embeds = len(message.embeds)
            attachments = len(message.attachments)
            stickers = len(message.stickers)
            self.__logger.debug("Received message, content length is %d, tts is %r, with %d embeds, %d attachments and %d stickers" % (length, tts, embeds, attachments, stickers))
            await self.get_channel(self.__channel).send(
                content=message.content,
                tts=message.tts,
                embeds=message.embeds,
                files=[await attachment.to_file() for attachment in message.attachments],
                stickers=message.stickers
            )

    def run(self):
        self.__logger.info("Starting bot...")
        nextcord.Client.run(self, self.__token)
