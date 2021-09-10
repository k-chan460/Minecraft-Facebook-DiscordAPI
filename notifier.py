from mcstatus import MinecraftServer
import fbchat
import threading

townlist = ["Minecraft_UserNames"]#array
client = fbchat.Client("<USERNAME>", "<PASSWORD>")
currentTownPlayers = [] #list of names of all online players from our town 
friends = client.searchForUsers('FB Name')
friend = friends[0]
def refresh():
    threading.Timer(20, refresh).start() #refreshes every 10 seconds
    server = MinecraftServer.lookup("SERVER_IP")
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
            client.sendMessage('Current players in Server: n/a',
                thread_id=friend.uid)
        else:
            #use client.uid instead of friend.uid to msg self
            client.sendMessage("Current players in Server: " +
                ", ".join(currentTownPlayers), thread_id=friend.uid)
    print('refreshed')
refresh()
