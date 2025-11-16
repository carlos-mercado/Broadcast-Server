import asyncio
import random
import json


from websockets.asyncio.server import serve

users = set()

artistTitle = "infinity frequencies - between two worlds"
image = "https://i.scdn.co/image/ab67616d0000b273574def96e0fcaa13fe2dd620"


async def broadcast(message):
    to_remove = set()
    for user in users:
        try:
            await user.send(message)
        except:
            to_remove.add(user)
    users.difference_update(to_remove)

async def sendMusicInfo(websocket):
    global artistTitle, image
    users.add(websocket)
    message = json.dumps({"artistTitle": artistTitle, "image": image})
    await broadcast(message)
    try:
        async for data_back in websocket:
            obj = json.loads(data_back)
            artistTitle = obj["artistTitle"]
            image = obj["image"]
            message = json.dumps({"artistTitle": artistTitle, "image": image})
            await broadcast(message)
    finally:
        users.discard(websocket)

def getUsers():
    print(users)

async def main():
    async with serve(sendMusicInfo, "", 8000) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
