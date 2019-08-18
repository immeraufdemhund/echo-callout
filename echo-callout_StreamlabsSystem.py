# ---------------------------
#   Import Libraries
# ---------------------------
import os
import sys
import clr

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))  # point at lib folder for classes / references
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

from PixelHelloService_Module import PixelHelloService
from PixelState_Module import PixelState

# ---------------------------
#   [Required] Script Information
# ---------------------------
ScriptName = "echo-callout"
Website = "https://twitch.tv/pixelgumtv"
Description = "say hi back to users"
Creator = "PixelBoy"
Version = "1.0.0.0"

HiPhrases = ['hi', 'hai', 'hello', 'howdy', 'waddup', 'ciao']
TimeoutSinceSaidHi = 5 # 30 * 60 # 30 minutes
global _PixelHelloService
_PixelHelloService = PixelHelloService(HiPhrases, TimeoutSinceSaidHi)

def Log(message):
    Parent.Log(ScriptName, message)
    return


# ---------------------------
#   [Required] Initialize Data (Only called on load)
# ---------------------------
def Init():
    # delete everyone who said hi (just in case it wasn't deleted)
    # create new said hi file
    return


def Execute(data):
    if not data.IsChatMessage():
        return
    pixelState = _PixelHelloService.getPixelState(data.UserName, data.Message)
    if pixelState == PixelState.SaidHiButNotRecently:
        _PixelHelloService.addNewUser(data.UserName)
        Parent.SendStreamMessage('I HAS A MESSAGE FOR @{user}: YOU ARE COOOL!'.format(user=data.UserName))
    elif pixelState == PixelState.SaidHiButRecently:
        Parent.SendStreamMessage("you already said hi @{user}".format(user=data.UserName))
    else:
        Parent.SendStreamMessage("I heard you...")
    # if they said hi not that long ago
    #     return
    # fire a websocket event
    # Say hi back to user
    # Parent.SendStreamMessage(joke)    # Send your message to chat
    return


def Tick():
    return


def Unload():
    # delete everyone who said hi
    return
