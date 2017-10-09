#!/usr/bin/env python

from __future__ import print_function
import os
import pylast
import sys

try:
    API_KEY = os.environ['LASTFM_API_KEY']
    API_SECRET = os.environ['LASTFM_API_SECRET']
except KeyError:
    API_KEY = ""
    API_SECRET = ""

try:
    lastfm_username = os.environ['LASTFM_USERNAME']
    lastfm_password_hash = os.environ['LASTFM_PASSWORD_HASH']
except KeyError:
    lastfm_username = ""
    lastfm_password_hash = ""


lastfm_network = pylast.LastFMNetwork(
    api_key=API_KEY, api_secret=API_SECRET,
    username=lastfm_username, password_hash=lastfm_password_hash)