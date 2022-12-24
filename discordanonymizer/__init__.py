import logging
import sys
import nextcord


class DiscordAnonymizer(nextcord.Client):

    def __init__(self, token, channel, log_level, watching, users):
        self.__logger = logging.getLogger("DiscordAnonymizer")
        self.__logger.setLevel(logging.getLevelName(log_level))
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)
        self.__logger.info("Initializing bot...")
        intents = nextcord.Intents.default()
        intents.members = True
        intents.messages = True
        nextcord.Client.__init__(self, intents=intents)
        self.__token = token
        self.__channel = channel
        self.__watching = watching
        self.__users = users

    async def on_ready(self):
        self.__logger.info("Changing presence...")
        watching = nextcord.Activity(name=self.__watching, type=nextcord.ActivityType.watching)
        await self.change_presence(status=nextcord.Status.online, activity=watching)
        self.__logger.info("Bot is ready")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            self.__logger.debug("Received message from the bot, ignoring")
            return
        if message.guild:
            self.__logger.debug("Received message is not a DM, ignoring")
            return
        if all(guild.get_member(message.author.id) is None for guild in self.guilds):
            self.__logger.debug("Received message comes from a user with no mutual guild, ignoring")
            return
        if len(self.__users) > 0 and message.author.id not in self.__users:
            self.__logger.debug("Received message from an unauthorized user, ignoring")
            return
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
