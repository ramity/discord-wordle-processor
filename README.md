<h1 align="center">
Discord Wordle Processor
</h1>

![image](https://i.imgur.com/Oadz4qQ.gif)

> Do you have a discord channel where you and your friends post your daily wordles? Have you ever wanted to know who ranks supreme? If so, this repo is for you.

# Requirements

Docker, Discord, Git

# Installation

(HTTPS)

```
git clone https://github.com/ramity/discord-wordle-processor.git
```

(SSH)

```
git clone git@github.com:ramity/discord-wordle-processor.git
```

# Configuration

Follow these [steps](https://www.writebots.com/discord-bot-token/) to integrate your self hosted bot.

Create the needed `.env` file in `docker/python/` directory. The `.env.dist` shows a sample `.env` file. Be sure to set the `TOKEN`, `CHANNEL`, and `LIMIT` vars:

- `TOKEN` - The provided token obtained via the discord interface.
- `CHANNEL` - The name of the text channel you wish to scrape from.
- `LIMIT` - The max number of messages you wish to scrape.

# Start

Ensure that the docker host is running, navigate to the root of the cloned repository, then run the following command:

```
docker compose up -d
```

# Usage

Enter the created `discord_bot` docker container:

(Linux/Unix)

```
docker exec -it discord_bot bash
```

(Windows)

```
winpty docker exec -it discord_bot bash
```

Run the `scrape.py` script to generate a `dump.pkl` file:

```
python scrape.py
```

> Example output displayed below:

```
Logged on as WordleBot#9999
Pulling messages from the #wordle text channel
Loaded all messages
Saved all messages
Exiting
```

When complete, exit the container via the `exit` command.

# Comments or Questions?

Open a [new git issue](https://github.com/ramity/discord-wordle-processor/issues/new) thread with the `question` label.

# Requests or Suggestions?

Open a [new git issue](https://github.com/ramity/discord-wordle-processor/issues/new) thread with the `enhancement` label.