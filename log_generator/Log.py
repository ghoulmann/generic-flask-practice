from random import choice

class Log(object):
    def __init__(obj):
        obj._timezone = choice(["-1100", "-1000", "-0900", "-0800", "-0700", "-0600", "-0500", "-0400", '-0300', \
        "-0200", "-0100", "0", "+0100", "+0200", "+0300", "+0400", "+0500", "+0400", "+0500", "+0600", \
            "+0700", "+0800", "+0900", "+1000", "+1100"])
