#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pixel Hello Service:
# Knows when you last said hi, and can check if you've said it recently
from PixelsModel_Module import Pixel
from PixelState_Module import PixelState
from TimeService_Module import TimeService

class PixelHelloService:
    PixelsChatting = {}
    HiPhrases = []

    def __init__(self, hiPhrases, timeoutInSeconds):
        self.HiPhrases = hiPhrases
        self.timeoutInSeconds = timeoutInSeconds

    def addNewUser(self, username):
        pixel = Pixel(username)
        self.PixelsChatting[pixel.name] = pixel
        return

    def getPixelState(self, username, message):
        if not self.messageIsHi(message):
            return PixelState.DidntSayHi
        elif not self.PixelsChatting.has_key(username):
            return PixelState.SaidHiButNotRecently
        else:
            lastTimeChatted = self.PixelsChatting[username].time
            currentTime = TimeService.getCurrentSeconds()
            if currentTime - lastTimeChatted >= self.timeoutInSeconds:
                return PixelState.SaidHiButNotRecently
            else:
                return PixelState.SaidHiButRecently

        return

    def messageIsHi(self, message):
        phrase = message.lower()
        for hi in self.HiPhrases:
            # Parent.Log("immer", '{} starts with: {} = {}'.format(phrase, hi, phrase.startswith(hi)))
            if phrase.startswith(hi):
                return bool(True)

        return bool(False)
