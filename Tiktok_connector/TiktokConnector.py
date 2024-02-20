from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import *

ListofGifts = []
# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@the.sun9525")

# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)


# Notice no decorator?
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")


@client.on("like")
async def on_like(event: LikeEvent):
    global ListofGifts
    ListofGifts.append(event)

@client.on("gift")
async def on_gift(event: GiftEvent):
    # Streakable gift & streak is over
    global ListofGifts
    if event.gift.streakable and not event.gift.streaking:
        ListofGifts.append(event)


    # Non-streakable gift
    elif not event.gift.streakable:
        ListofGifts.append(event)
        print(ListofGifts)

# Define handling an event via a "callback"
client.add_listener("comment", on_comment)
def runTiktokClient(giftlist):
    global ListOfGifts
    ListOfGifts = giftlist
    ListOfGifts.append("lmao")
    print(id(giftlist),"1")
    print(id(ListofGifts),"2")
    client.run()

print(ListofGifts)
