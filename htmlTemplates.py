css = """
<style>
body {background-color: #f5f5f5;}
.chat-message {padding: 10px; border-radius: 8px; margin: 5px 0; max-width: 80%;}
.user-message {background-color: #111B21; text-align: left;}
.bot-message {background-color: #014D1D; text-align: left;}
</style>
"""

user_template = """<div class="chat-message user-message">{{MSG}}</div>"""
bot_template = """<div class="chat-message bot-message">{{MSG}}</div>"""
