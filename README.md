<h1 align="center">
Discord Wordle Processor
</h1>

![image](https://i.imgur.com/Oadz4qQ.gif)

> Do you have a discord channel where you and your friends post your daily wordles? Have you ever wanted to know who ranks supreme? If so, this repo is for you.

# Example outputs

```
Name            Count   Score   Streak  Max     Oby1    Oby1%
DB2             303     3.95    39      52      104     34.32
Cuddles         280     4.06    5       32      76      27.14
WannaBePro      253     4.08    48      63      77      30.43
BigRed          209     4.04    2       20      74      35.41
crazyism        10      4.3     1       2       3       30.0
Buck 50         1       2.0     1       1       0       0.0
PastorMeatSauce 1       4.0     1       1       0       0.0
```

```
Name            Count   1%      2%      3%      4%      5%      6%      X%
DB2             303     0.0     7.59    26.07   40.92   17.16   5.94    2.31
Cuddles         280     0.0     3.93    26.43   40.36   19.64   8.21    1.43
WannaBePro      253     0.0     6.72    26.88   33.2    20.95   9.88    2.37
BigRed          209     0.0     5.74    24.4    39.23   22.97   6.22    1.44
crazyism        10      0.0     0.0     40.0    20.0    20.0    10.0    10.0
Buck 50         1       0.0     100.0   0.0     0.0     0.0     0.0     0.0
PastorMeatSauce 1       0.0     0.0     0.0     100.0   0.0     0.0     0.0
```

```
Name            Count   1 val   2 val   3 val   4 val   5 val   6 val
DB2             303     1.14    2.33    3.44    4.39    4.56    4.68
Cuddles         280     1.1     2.1     3.28    4.16    4.37    4.83
WannaBePro      253     1.05    2.15    3.27    3.99    4.35    4.77
BigRed          209     1.22    2.15    3.27    4.22    4.67    4.75
crazyism        10      1.4     1.5     3.55    3.67    4.5     4.5
Buck 50         1       2.0     5.0     0       0       0       0
PastorMeatSauce 1       0.5     1.5     3.0     5.0     0       0
```

# Requirements

Docker

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

Process the created `dump.pkl` file:

```
python process.py
```

> Example output displayed below:

```
Select an output type (type the corresponding number key and press enter).
[0] - Short
[1] - Average results
[2] - Average values
[3] - Full

0

Name            Count   Score   Streak  Max     Oby1    Oby1%
DB2             303     3.95    39      52      104     34.32
Cuddles         280     4.06    5       32      76      27.14
WannaBePro      253     4.08    48      63      77      30.43
BigRed          209     4.04    2       20      74      35.41
crazyism        10      4.3     1       2       3       30.0
Buck 50         1       2.0     1       1       0       0.0
PastorMeatSauce 1       4.0     1       1       0       0.0
```

When complete, exit the container via the `exit` command.

# Comments or Questions?

Open a [new git issue](https://github.com/ramity/discord-wordle-processor/issues/new) thread with the `question` label.

# Requests or Suggestions?

Open a [new git issue](https://github.com/ramity/discord-wordle-processor/issues/new) thread with the `enhancement` label.