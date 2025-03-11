<h1 align="center">
Discord Wordle Processor
</h1>

![A screenshot of https://ramity.github.io/discord-wordle-processor/ showing a leaderboard and their respective average scores across all games](https://github.com/user-attachments/assets/13b3c900-7cec-48fe-92fd-1e59687d1547)

> Do you have a discord channel where you and your friends post your daily wordles? Have you ever wanted to know who ranks supreme? If so, this repo is for you.

# Requirements

Docker, Discord, Git

# Installation

> (HTTPS)
>
> ```
> git clone https://github.com/ramity/discord-wordle-processor.git
> ```
>
> (SSH)
>
> ```
> git clone git@github.com:ramity/discord-wordle-processor.git
> ```

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

Enter the created `wordle_discord` docker container:

> (Linux/Unix)
>
> ```
> docker exec -it wordle_discord bash
> ```
>
> (Windows)
>
> ```
> winpty docker exec -it wordle_discord bash
> ```

Run the `scrape.py` script to generate a `dump.pkl` file:

```
python scrape.py
```

> Example output displayed below:

```
Logged on as WordleBot#9999
Pulling messages from the #wordle text channel
Calculating stats
Complete
```

When complete, exit the container via the `exit` command.

Commit and push the changes to wordle-stats-by-author.json and wordles-by-author.json.

```
git add.
git commit -m "scrape data"
git push origin master
```

Create github page:

`Settings > Pages > Set folder to "/docs"`

Navigate to the created site.

# Example

https://ramity.github.io/discord-wordle-processor/

![](https://i.imgur.com/sCC8gNL.png)

![](https://i.imgur.com/tYkOJOj.png)

# Comments or Questions?

Open a [new git issue](https://github.com/ramity/discord-wordle-processor/issues/new) thread with the `question` label.

# Requests or Suggestions?

Open a [new git issue](https://github.com/ramity/discord-wordle-processor/issues/new) thread with the `enhancement` label.
