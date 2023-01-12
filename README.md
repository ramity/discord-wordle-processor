<h1 align="center">
Discord Wordle Processor
</h1>

![image](https://i.imgur.com/Oadz4qQ.gif)

> Do you have a discord channel where you and your friends post your daily wordles? Have you ever wanted to know who ranks supreme? If so, this repo is for you.

# Requirements

Docker

# Installation

```
git clone https://github.com/ramity/discord-wordle-processor.git
```

# Configuration

Follow these [steps](https://www.writebots.com/discord-bot-token/) to integrate your self hosted bot.

Create the needed `.env` file in `docker/python/` directory with `TOKEN` defined.

# Start

```
docker compose up -d
```

# Usage

To start your bot (which scrapes your "wordle" text channel and produces a `dump.pkl` file):

```
docker exec -it discord_bot bash
python bot.py
```

To process the created `dump.pkl` file

```
docker exec -it discord_bot bash
python process.py
```