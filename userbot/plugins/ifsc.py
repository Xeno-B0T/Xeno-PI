import json

import requests

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd

CmdHelp("ifsc").add_command("ifsc", None, "search ifsc code of bank").add()


@bot.on(admin_cmd(pattern="ifsc(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    url = "https://ifsc.razorpay.com/{}".format(input_str)
    r = requests.get(url)
    if r.status_code == 200:
        b = r.json()
        a = json.dumps(b, sort_keys=True, indent=4)
        # https://stackoverflow.com/a/9105132/4723940
        await event.edit(str(a))
    else:
        await event.edit("`{}`: {}".format(input_str, r.text))
