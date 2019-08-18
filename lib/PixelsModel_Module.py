#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TimeService_Module import TimeService


class Pixel:
    name = '<NULL>'
    time = 0

    def __init__(self, username):
        self.name = username
        self.time = TimeService.getCurrentSeconds()

