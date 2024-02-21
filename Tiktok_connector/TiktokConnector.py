from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import *
# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@the.sun9525")
path = "..\Game\events.txt"
fileopen=open(path,"w")
# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)


# Notice no decorator?
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")


@client.on("like")
async def on_like(event: LikeEvent):
    with open(path,"a") as file:
        file.write("like\n")

@client.on("gift")
async def on_gift(event: GiftEvent):
    # Streakable gift & streak is over
    if event.gift.streakable and not event.gift.streaking:
        with open(path,"a") as file:
            file.write(f"{event.gift.info.name}\n{event.gift.count}\n")


    # Non-streakable gift
    elif not event.gift.streakable:
        with open(path,"a") as file:
            file.write(f"{event.gift.info.name} 1 \n")


# Define handling an event via a "callback"
client.add_listener("comment", on_comment)
def runTiktokClient(giftlist):
    client.run()
