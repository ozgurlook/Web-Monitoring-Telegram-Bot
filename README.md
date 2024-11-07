
# Web Monitoring Telegram Bot

This project creates a Telegram bot that searches for a specific text (e.g., "High odds") on a specified webpage. When the target text is found, the bot sends a notification to a designated Telegram chat. The bot includes commands that allow you to start and stop monitoring as well as change the target text.

## Features

- Search for specific text on a designated webpage
- Send a notification to a Telegram chat when the text is found
- Start monitoring with the `/start` command
- Stop monitoring with the `/stop` command
- Change the target text with the `/change` command

## Requirements

- Python 3.7 or higher
- Telegram Bot API Token
- `aiogram`, `aiohttp`, and `lxml` packages

## Installation

### Step 1: Install the required packages

```bash
pip install aiogram aiohttp lxml
```

### Step 2: Set up Telegram Bot API Token and Chat ID

- `API_TOKEN`: Add your bot's API token here. This token can be obtained from [Telegram BotFather](https://core.telegram.org/bots#botfather).
- `CHAT_ID`: The chat ID of the Telegram chat where the bot will send messages. This can be a user or group chat.

Fill in the following fields in the code:

```python
API_TOKEN = 'your-telegram-bot-api-token'
CHAT_ID = 'your-chat-id'
```

### Step 3: Define the URL

Specify the URL of the webpage to be monitored in the `URL` variable:

```python
URL = 'https://your-url-here.com'
```

## Usage

### Run the Bot

To start the bot, run the following command in the terminal:

```bash
python bot.py
```

### Commands

- **/start**: Starts monitoring. The bot will begin checking the specified page at regular intervals.
- **/stop**: Stops monitoring.
- **/change [text]**: Changes the target text to monitor. For example, use `/change new text` to set the bot to monitor for new text.

## How the Code Works

1. When the bot is started (with the `/start` command), it will check the specified URL at 10-second intervals.
2. When the `target_text` is found on the page, the bot will send a notification to the specified `CHAT_ID` in Telegram.
3. Use the `/change` command to modify the target text and monitor for different text.

## Error Handling

The bot logs any connection errors or other HTTP errors to the terminal and continues running.

## Example

- Use the `/start` command to start the bot. The bot will begin monitoring the specified URL.
- Change the target text with `/change Target Text`.
- When the bot finds the target text, it will send a message to the Telegram chat.
