from os import environ
class Config(object):
    API_ID = environ.get("API_ID", 1695333)
    API_HASH = environ.get("API_HASH", "acfb6f602239fc52a93d1847a3d850d1")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5527448498:AAECjLx626Z5AaGOUZUIvIlq7rtWFQh6kDQ")
    STRING_SESSION = environ.get("STRING", "1BVtsOLMBu4DM2nIOUQ3uWrmSuLbBosHLhMeK-rDNoFHsjugVKfw_bW8XUx6P-xLlsXRe0XYJZbj3kHq67OVKuHa0aHVn3UpBXXdrWMH_kUT1O-vkQAqhZaj3uuMlERpbA_-mscsEudI9ihQOKhDKC0MJN97x1xH7lCkuvaRcNQKz_M9yqG_H9YRRKQC8AeY4iK8tZNY9bT4pvFBmrUErPuxZs3dkTGEVGdKvW2JIFjEBOxpvcjZGX0E1-nft_LPFBVv7_lLSXTUeiXhBygP3f7PB_L-xz5hbmckM_21ENOPuZj4dxcYFEEeLqK9LemsQ3LlLmpOTvuHaxRb-BdvwcwC2CAh9GxU=")
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
