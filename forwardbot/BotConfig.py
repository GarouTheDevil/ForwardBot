from os import environ
class Config(object):
    API_ID = environ.get("API_ID", 1695333)
    API_HASH = environ.get("API_HASH", "acfb6f602239fc52a93d1847a3d850d1")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5527448498:AAECjLx626Z5AaGOUZUIvIlq7rtWFQh6kDQ")
    STRING_SESSION = environ.get("STRING", "1BVtsOLMBuzsthN_aF44Xyc3CdtH9DtfyTm2Wdmrlpzz2QETOd3SJ85kvdHC9xBFasPManzRS0vo5NUrb_JcTAIP3Xr9IKMDGfH4tx5f0X8KrWoA6pa_eY6k1iJP4lRFf5PHVBqoc8cpJPYKrbNbxo-1Q-BRoqBOMecpzeQK0xmYHbiVWCGyRnuT3paW6NTBXNwye_rWO9pQdNrkmtO9pL5qRhUn_FEUvhkRQieM69O2eVBsh30HIOTypKxY2T4urOlyqxaLtctf0E-Y579E1ynO21t7TV9rr4dOUWKPEqTKExFBJ0nrRG6eaxLNbhIlmkesirg7FfPV4uJrNsxPTsEa3kZHi2wU=")
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
