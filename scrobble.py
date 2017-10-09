#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import re
from login import lastfm_network

#Open the log file. I use a static location, so I set an environment variable for it.
def open_log():
    try:
        with open(os.environ['LASTFM_LOG_LOCATION'], 'r') as f:
            plays = f.readlines()
    except KeyError:
        print("\033[1;31;40m" + "Error: " + "\033[1;37;40m" + "LASTFM_LOG_LOCATION env var not set")
    except IOError:
        print("\033[1;31;40m" + "Error: " + "\033[1;37;40m" + "Log file not found")
    
    print(os.environ['LASTFM_LOG_LOCATION'])
    return plays

def submit_track(artist, track, unix_timestamp):
    lastfm_network.scrobble(
        artist=artist, title=track, timestamp=unix_timestamp)

#line[0] = "Artist"
#line[2] = "Track"
#line[5] = Played flag (L = Listened, S = Skipped). I only check for L here.
#line[6] = "Unix Timestamp"
def scrobble(log):
    for line in log:
        line = re.split(r'\t+', line)
        if (line[5] == "L"):
            print("\033[1;32;40m" + "Scrobbling: " + "\033[1;37;40m" + line[0]  + " - " + line[2])
            submit_track(line[0], line[2], line[6])
        else:
            print("\033[1;33;40m" + "Skipped: " + "\033[1;37;40m" + line[0] + " - " + line[2])

scrobble(open_log())
