<h1 align="center">
Discord Wordle Processor
</h1>

![image](https://i.imgur.com/Oadz4qQ.gif)

> Do you have a discord channel where you and your friends post your daily wordles? Have you ever wanted to know who ranks supreme? If so, this repo is for you.

# Example output

```
Name            1%      2%      3%      4%      5%      6%      X%      count   score
---------------------------------------------------------------------------------------
DB2             0.0     7.6     25.7    41.3    17.4    5.6     2.4     288     3.95
Cuddles         0.0     4.1     27.0    40.1    19.1    8.2     1.5     267     4.05
WannaBePro      0.0     6.7     26.5    32.8    21.8    9.7     2.5     238     4.09
BigRed          0.0     5.4     24.3    39.6    22.8    6.4     1.5     202     4.05
crazyism        0.0     0.0     40.0    20.0    20.0    10.0    10.0    10      4.30
Buck 50         0.0     100.0   0.0     0.0     0.0     0.0     0.0     1       2.00
```

# Requirements

Docker

# Installation

```
git clone https://github.com/ramity/discord-wordle-processor.git
```

# Configuration

Follow these [steps](https://www.writebots.com/discord-bot-token/) to integrate your self hosted bot.

Create the needed `.env` file in `docker/python/` directory with `TOKEN` set to the bot's token and `CHANNEL` to the name of the text channel you wish to scrape. `.env.dist` shows a sample `.env` file.

# Start

```
docker compose up -d
```

# Usage

To start your bot (which scrapes your "wordle" text channel and produces a `dump.pkl` file):

```
docker exec -it discord_bot bash
python scrape.py
```

> Example output displayed below:

```
Logged on as WordleBot#9999!
Pulling messages from #wordle textchannel.
Loaded all messages.
Saved all messages.
Exiting.
```

To process the created `dump.pkl` file

```
docker exec -it discord_bot bash
python process.py
```