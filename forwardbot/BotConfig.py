from os import environ
class Config(object):
    API_ID = environ.get("API_ID", 1695333)
    API_HASH = environ.get("API_HASH", "acfb6f602239fc52a93d1847a3d850d1")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5527448498:AAECjLx626Z5AaGOUZUIvIlq7rtWFQh6kDQ")
    STRING_SESSION = environ.get("STRING", "1BVtsOLMBu7UGZfwOZkP6EPFm02jHDr2SUqcAjImKCtAl-OiekhlBpSIrcSgiBd-93ikktI1kQkCfhE8YFanLHn-BQ6_8jPxfn0TT3XOmeIviEOKZ37mxrHGGrml3ercl6x3ZFxc4CvuvpH5ywTVVQmJANvIx6SAqKVEdJls9OT9C4qijVXScalo3YGmxn4NM6tfk9wNX9tQXZZsBNxveHuvgcAA1x4x1_19vOWCZsJXiUeoZ7ai9Yr-Q6YiWXpPjZ-nPE7JCIXU5kyIZ59ifemgmqyeKKilT2meClpWLpwppA1iXNCuf-bm3FInj00ibnuYv3LadGYBVaLo3Nz-OtapnSyQ54yo=")
    SUDO_USERS = environ.get("SUDO_USERS", "1016768333")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    The Commands in the bot are:
    
    **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    **Command :** /reset
    **Usage : ** Resets the message count to 0.
    **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    **Command :** /join
    **Usage : ** Joins the channel.
    **Command :** /help
    **Usage : ** Get the help of this bot.
    **Command :** /status
    **Usage :** Check current status of Bot.
    **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    Bot is created by @lal_bakthan and @subinps
    """
