# Simple Discord Server

A lightweight and extensible, basic Discord server linking a Discord client with FastAPI to convert REST API calls into Discord actions. 

This is 80% just for my own personal reference in the future.

## Installation

First, get the repository and install the requirements: 

```
git clone https://github.com/yo-wotop/simple-discord-server.git
cd simple-discord-server
pip install -r requirements.txt
```

You'll also want an ASGI server, such as Uvicorn:  

```
pip install uvicorn[standard]
```

Also, make sure you have Python3.9+ installed, as [other versions have problems with asyncio.add_signal_handler() being out of the main thread](https://bugs.python.org/issue34679).

## Running

Once it's all installed, running should be easy. In a terminal, navigate to your installation folder and run your ASGI server. For example, if you use Uvicorn:

```
uvicorn main:app --reload
```

## Use

First, you must put your Discord API key within `discord_credentials.json` where I noted. You'll need to get one from Discord.

Next, this basic server comes with two simple calls, listening on two endpoints. You can use, for example, the `requests` library to make these calls. 

#### Endpoint 1: `/chat`

This endpoint is for sending a message in a Discord channel on a Discord server. For example, if you want to send a chat message in server `1234567` and channel `9876543`, you can simply write: 

```
import requests

url = 'http://localhost:8000/chat'
body = {
    server: 1234567,
    channel: 9876543,
    text: 'Hello World'
}

requests.post(url, json=body)
```

#### Endpoint 2: `/dm`

This endpoint is for sending a direct message to a user in Discord. Please note that the user _must have a shared channel with your bot_ to make this work. For example, if you wish to send a DM to user `1029384`, you could write:   

```
import requests

url = 'http://localhost:8000/dm'
body = {
    recipient: 1029384,
    text: 'Hello World'
}

requests.post(url, json=body)
```

## Notes

I didn't test any of these documentation notes, so they are a best-effort. This repository is primarily for my future reminders whenever I want to work with expanding my home Discord alert system.

Additional documentation if I forget anything:

1. [FastAPI, the brains of the operation](https://fastapi.tiangolo.com/)
2. [Discord API](https://discordpy.readthedocs.io/en/stable/api.html)
