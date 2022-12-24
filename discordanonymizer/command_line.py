import argparse
import os

from discordanonymizer import DiscordAnonymizer


def main():
    parser = argparse.ArgumentParser(description="Starts the DiscordAnonymizer bot")
    parser.add_argument("--token",
                        type=str,
                        default=os.environ.get("TOKEN"),
                        help="Bot token used to access Discord API. If omitted, the value of the `TOKEN` environment variable will be used"
                        )
    parser.add_argument("--channel",
                        type=int,
                        default=os.environ.get("CHANNEL"),
                        help="Channel ID where message will be reposted. If omitted, the value of the `CHANNEL` environment variable will be used"
                        )
    parser.add_argument("--log-level",
                        type=str,
                        default=os.environ.get("LOG_LEVEL") or "INFO",
                        help="Log level. If omitted, the value of the `LOG_LEVEL` environment variable will be used. Defaults to `INFO`"
                        )
    parser.add_argument("--watching",
                        type=str,
                        default=os.environ.get("WATCHING") or "your DMs",
                        help="Watching status of the bot. If omitted, the value of the `WATCHING` environment variable will be used. Defaults to `your DMs`"
                        )
    parser.add_argument("--user",
                        action="append",
                        type=int,
                        default=[int(user) for user in list(filter(None, (os.environ.get("USERS") or "").split(",")))],
                        help="The list of user IDs that are allowed to use the bot, if left empty, all users are allowed"
                        )
    args = parser.parse_args()
    bot = DiscordAnonymizer(args.token, args.channel, args.log_level, args.watching, args.user)
    bot.run()
