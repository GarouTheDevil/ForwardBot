from os import environ
class Config(object):
    API_ID = environ.get("API_ID", 1695333)
    API_HASH = environ.get("API_HASH", "acfb6f602239fc52a93d1847a3d850d1")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5527448498:AAECjLx626Z5AaGOUZUIvIlq7rtWFQh6kDQ")
    STRING_SESSION = environ.get("STRING", "1BVtsOLMBu2ZUMRLZYoK305QsFwWUk9YC1uvhJMIpUqph0lz6_OZ91MoZNTrBqaglM2sq7QJIQi9sDKCePbykGpp_Qargelhfsg8wLzuxY8adKFJHySv9HzL4A9qzl3qch6tFXYQDwTukB4nAMexnSNcifg0nO5fFO-fcXUp6DERuZrTerGoEN2D8RAbJJrVwNEqnDCQtudT7FuG7FCpXdFCdzOC3k3eYiHXjIeIDCD2ibPMq9ngi2mTkSrGHbubHGB0cwV5qfQ7TuQSBpwMXDxz__BdQVVdNG3sVBBPTYuwC1GvU0H6pwr5k3BglO-RuIspDBlD4zkucZBgxQn1JtCWGjvHuAOo=")
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
