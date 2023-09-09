from libqtile.config import Group, ScratchPad, DropDown, Key
from libqtile.lazy import lazy
from modules.keys import keys
from modules.prefs import mod, terminal 

groups = []
group_names = ["1","2","3","4","5"]
group_labels = ["󰉢 "," "," ","󰽚 ","󰎉 "]

for g in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[g],
            label=group_labels[g],
        )
    )

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False), desc="Switch to & move focused window to group {}".format(i.name)),
    ])

# Scratchpads
groups.append( ScratchPad("music",[DropDown("tunes", terminal + " -e musikcube", x=0.15, y=0.15, width=0.70, height=0.70, on_focus_lost_hide=False)]) )
groups.append( ScratchPad("stats",[DropDown("top", terminal + " -e btop", x=0.25, y=0.2, width=0.50, height=0.50, on_focus_lost_hide=False)]) )

keys.extend([
    Key([mod, "control"], "m", lazy.group['music'].dropdown_toggle('tunes')),
    Key([mod, "control"], "t", lazy.group['stats'].dropdown_toggle('top')),
])