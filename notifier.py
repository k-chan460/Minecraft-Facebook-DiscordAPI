from mcstatus import MinecraftServer
import fbchat
import threading

townlist = ["Ninja_Master_99", "RegalSweets", "Its_Falken", "steakfrog", "Handsanitizer01", "Player1Jessica", "SenexEU", "PandaDrone", "Pucker97"]#array
client = fbchat.Client("<USERNAME>", "<PASSWORD>")
currentTownPlayers = [] #list of names of all online players from our town 
friends = client.searchForUsers('Kevin Chan')
friend = friends[0]
def refresh():
    threading.Timer(20, refresh).start() #refreshes every 10 seconds
    server = MinecraftServer.lookup("144.217.11.33:25565")
    query = server.query()
    #list of names all online players
    currentServerPlayers = query.players.names 
    hasChanged = False #did the citizenslist change?
    for citizen in townlist:
        #if citizen is on serverlist but not on townlist, add them to townlist
        if citizen in currentServerPlayers:
            if citizen not in currentTownPlayers:
                currentTownPlayers.append(citizen)
                hasChanged = True
        #if citizen is not on serverlist but on townlist, remove them from
        #townlist
        if citizen not in currentServerPlayers:
            if citizen in currentTownPlayers:
                currentTownPlayers.remove(citizen)
                hasChanged = True
    if(hasChanged):
        if (currentTownPlayers.__len__ == 0 ):
            #use client.uid instead of friend.uid to msg self
            client.sendMessage('Current players in Netherverse town: n/a',
                thread_id=friend.uid)
        else:
            #use client.uid instead of friend.uid to msg self
            client.sendMessage("Current players in Netherverse town: " +
                ", ".join(currentTownPlayers), thread_id=friend.uid)
    print('refreshed')
refresh()
