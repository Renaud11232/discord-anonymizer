import argparse
import os

from discordanonymizer import DiscordAnonymizer


def main():
    parser = argparse.ArgumentParser(description="Starts the discordanonymizer bot")
    parser.add_argument("--token", type=str, default=os.environ.get("TOKEN"))
    parser.add_argument("--channel", type=int, default=os.environ.get("CHANNEL"))
    parser.add_argument("--log-level", type=str, default=os.environ.get("LOG_LEVEL") or "INFO")
    parser.add_argument("--watching", type=str, default=os.environ.get("WATCHING") or "your DMs")
    args = parser.parse_args()
    bot = DiscordAnonymizer(args.token, args.channel, args.log_level, args.watching)
    bot.run()
