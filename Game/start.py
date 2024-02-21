import Tiktok_connector.TiktokConnector
from Game.Interface.GameWindow import GameWindow
from threading import Thread
import asyncio
giftlist=[]
def main():
    game = GameWindow()
    #Dont remove giftlist argument or it breaks, idk why
    '''thread=Thread(target=Tiktok_connector.TiktokConnector.runTiktokClient, args=(giftlist,))
    thread.daemon = True
    thread.start()'''
    game.run_game(giftlist)
main()
