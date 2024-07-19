
# Notion Discord Webhook

This project allows you to send notifications to a Discord channel through webhooks when certain conditions are met in a Notion database.

## Prerequisites

Before you begin, make sure you have the following:

-   A Discord server and a Discord channel where you want to receive the notifications
-   A Discord webhook URL for the channel (you can create one by following the instructions [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks))
-   A Notion account and a Notion database
-   The Notion API token, which you can get by following the instructions [here](https://developers.notion.com/docs/getting-started#step-2-share-a-database-with-your-integration)

## Installation

1.  Clone the repository:

Copy code

`git clone https://github.com/YanGusik/NotionDiscordBot.git` 

2.  Install the dependencies:

Copy code

`pip install -r requirements.txt` 


Or Create a virtual environment

`python3 -m venv myenv`

`source myenv/bin/activate`

`pip install -r requirements.txt`

3.  Replace the placeholders in the `.env` file with your actual values:

-   `DISCORD_WEBHOOK`: the Discord webhook URL
-   `NOTION_TOKEN`: your Notion API token
-   `NOTION_DATABASE_ID`: the ID of your Notion database

## Usage

`python3 main.py`