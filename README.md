# Discord Anonymizer

Discord Anonymizer is a simple bot that reposts received DMs on a guild channel.

This bot was designed to allow guild members to talk about various topics without being recognised.
It supports sending text, files (including images and gifs), embeds (ie: Youtube links), emotes, stickers and TTS.

None of the messages sent to the bot are recorded. They are just sent back directly on the desired channel without any way to identify the person who sent it in the first place

The docker images can be used on `amd64` and `arm64` systems.

## Starting the bot

You can run this bot using docker CLI, docker-compose or running it directly on the host machine.

### Parameters

The various arguments the bots takes can be set using a command line flag or using an environment variable :
If the same option is set using both the command flag and the environment variable, the environment variable will be ignored.

| CLI flag              | Environment variable      | Description                                                                                               | Required | Default    |
|-----------------------|---------------------------|-----------------------------------------------------------------------------------------------------------|----------|------------|
| `--token`             | `TOKEN`                   | The Discord bot token used to access the Discord API                                                      | Yes      |            |
| `--channel`           | `CHANNEL`                 | The channel ID where all received messages will be reposted                                               | Yes      |            |
| `--log-level`         | `LOG_LEVEL`               | The log level of the bot. The bot will never log the content of the received message or its author        | No       | `INFO`     |
| `--watching`          | `WATCHING`                | The watching status of the bot                                                                            | No       | `your DMs` |
| `--user` (repeatable) | `USERS` (comma separated) | The list of users IDs that are allowed to use the bot. If left empy, all users are allowed to use the bot | No       | `<empty>`  |


### Docker CLI

```bash
docker run \
  -d \
  --name discordanonymizer \
  --restart unless-stopped \
  -e TOKEN=yourtoken \
  -e CHANNEL=123123 \
  -e LOG_LEVEL=INFO \
  -e WATCHING=your\ DMs \
  -e USERS=111111,222222,333333 \
  ghcr.io/renaud11232/discordanonymizer
```

### Docker-compose

`docker-compose.yml`:

```yml
version: "3"
services:
  discordanonymizer:
    container_name: discordanonymizer
    image: "ghcr.io/renaud11232/discordanonymizer"
    environment:
      TOKEN: yourtoken
      CHANNEL: 123123
      LOG_LEVEL: INFO
      WATCHING: your DMs
      USERS: 11111,22222,33333
    restart: unless-stopped
```

```bash
docker-compose up -d
```

### Bare metal

You can install this bot by running the following command (a venv is recommended) :

```bash
pip install "https://github.com/Renaud11232/discord-anonymizer/archive/refs/heads/master.zip"
```

Once it's installed you can start it either by setting the environment variables :
```bash
export TOKEN=yourtoken
export CHANNEL=123123
export LOG_LEVEL=INFO
export WATCHING=your\ DMs
export USERS=11111,22222,33333
discordanonymizer
```

Or by providing the correct flags :
```bash
discordanonymizer \
  --token yourtoken \
  --channel 123123 \
  --log-level INFO \
  --watching "your DMs" \
  --user 11111 \
  --user 22222 \
  --user 33333
```
