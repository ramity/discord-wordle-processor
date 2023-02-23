<h1 align="center">
Discord Wordle Processor
</h1>

![image](https://i.imgur.com/Oadz4qQ.gif)

> Do you have a discord channel where you and your friends post your daily wordles? Have you ever wanted to know who ranks supreme? If so, this repo is for you.

# Example outputs

```
Name            Count   Score   Oby1    Oby1%
DB2             328     3.95    117     35.67
Cuddles         306     4.08    84      27.45
WannaBePro      277     4.1     88      31.77
BigRed          222     4.06    82      36.94
crazyism        13      4.31    4       30.77
Buck 50         1       2.0     0       0.0
PastorMeatSauce 26      4.08    10      38.46
```

```
Name            Count   1%      2%      3%      4%      5%      6%      X%
DB2             328     0.0     7.01    26.83   40.55   17.68   5.79    2.13
Cuddles         306     0.0     3.59    25.49   40.85   20.59   7.84    1.63
WannaBePro      277     0.0     6.86    25.63   33.21   21.3    10.47   2.53
BigRed          222     0.0     5.41    23.87   39.64   22.97   6.76    1.35
crazyism        13      0.0     7.69    30.77   15.38   23.08   15.38   7.69
Buck 50         1       0.0     100.0   0.0     0.0     0.0     0.0     0.0
PastorMeatSauce 26      0.0     3.85    26.92   42.31   11.54   15.38   0.0
```

```
Name            Count   1 val   2 val   3 val   4 val   5 val   6 val
DB2             328     1.16    2.33    3.47    4.38    4.57    4.69
Cuddles         306     1.07    2.08    3.24    4.17    4.39    4.81
WannaBePro      277     1.05    2.16    3.25    3.98    4.3     4.75
BigRed          222     1.25    2.15    3.27    4.23    4.65    4.78
crazyism        13      1.42    1.85    3.42    3.44    4.33    4.67
Buck 50         1       2.0     5.0     0       0       0       0
PastorMeatSauce 26      1.06    2.23    3.52    4.36    4.14    5.0
```

```
Name            x-less st.      max x-less st.  post st.        max post st.    combined st.    max combined st.
DB2             97              126             64              64              64              64
Cuddles         0               131             31              32              0               30
WannaBePro      4               115             23              63              4               48
BigRed          84              84              1               20              1               20
crazyism        5               7               0               2               0               2
Buck 50         1               1               1               1               1               1
PastorMeatSauce 26              26              2               21              2               21
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

Name            Count   Score   Oby1    Oby1%
DB2             328     3.95    117     35.67
Cuddles         306     4.08    84      27.45
WannaBePro      277     4.1     88      31.77
BigRed          222     4.06    82      36.94
crazyism        13      4.31    4       30.77
Buck 50         1       2.0     0       0.0
PastorMeatSauce 26      4.08    10      38.46
```

When complete, exit the container via the `exit` command.

# Comments or Questions?

Open a [new git issue](https://github.com/ramity/discord-wordle-processor/issues/new) thread with the `question` label.

# Requests or Suggestions?

Open a [new git issue](https://github.com/ramity/discord-wordle-processor/issues/new) thread with the `enhancement` label.