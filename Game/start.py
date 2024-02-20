import Tiktok_connector.TiktokConnector
from Game.Interface.GameWindow import GameWindow
from threading import Thread
import asyncio
giftlist=[]
def main():
    game = GameWindow()
    thread=Thread(target=Tiktok_connector.TiktokConnector.runTiktokClient, args=(giftlist,))
    thread.daemon = True
    thread.start()
    print(giftlist,"3")
    print(id(giftlist),"4")
    game.run_game(giftlist)
main()
