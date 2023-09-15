import os
import subprocess
from libqtile import hook

from modules.keys import *
from modules.groups import *
from modules.screens import *
from modules.layouts import *

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/modules/autostart.sh')
    subprocess.call([home])

