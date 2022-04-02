import argparse
import os

from discordanonymizer import DiscordAnonymizer


def main():
    parser = argparse.ArgumentParser(description="Starts the discordanonymizer bot")
    parser.add_argument("--token", type=str, default=os.environ.get("TOKEN"))
    parser.add_argument("--channel", type=int, default=os.environ.get("CHANNEL"))
    parser.add_argument("--log-level", type=str, default=os.environ.get("LOG_LEVEL") or "INFO")
    args = parser.parse_args()
    bot = DiscordAnonymizer(args.token, args.channel, args.log_level)
    bot.run()
