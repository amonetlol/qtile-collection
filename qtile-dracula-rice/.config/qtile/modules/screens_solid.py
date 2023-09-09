import os
from libqtile.config import Screen
from libqtile import bar, qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

from modules.prefs import terminal, launcher, power_menu
from modules.pallete import colors

widget_defaults = dict(
    font="JetBrainsMono",
    fontsize = 14,
    padding = 1,
    background=colors['bg'],
)

powerline = {
    "decorations": [
        PowerLineDecoration(path="forward_slash")
    ]
}

extension_defaults = widget_defaults.copy()

def init_screens():
    return [
        Screen(top=bar.Bar(
            [
                widget.GroupBox(
                    background=colors['bg'],
                    borderwidth=1,
                    active = colors['fg'],
                    inactive = colors['fg'],
                    highlight_method = "block",
                    highlight_color = colors['fg'],
                    this_current_screen_border = colors['blue'],
                    disable_drag = True,
                    hide_unused=False,
                    padding=10,
                    spacing=5,
                ),
                widget.Spacer(background=colors['bg']),
                widget.WindowName(
                    foreground=colors['fg'],
                    background=colors['bg'],
                    width = bar.CALCULATED,
                    padding=10,
                ),                widget.Spacer(background=colors['bg'],),
                widget.Systray(
                    background=colors['bg'],
                    icon_size = 16,
                    padding = 20,
                ),
                widget.Sep(linewidth=0, padding=14, size_percent=40),
                widget.TextBox(
                    text='  ',
                    foreground=colors['red'],
                    padding=2,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(power_menu)},
                ),
                widget.Sep(linewidth=0, padding=14, size_percent=40),
                widget.Clock(
                    foreground=colors['black'],
                    background=colors['blue'],
                    padding = 10,
                    format="%I:%M %p 󱑇 "
                ),
            ], opacity=1.0, size=38, margin=0,
        ))
    ]

screens = init_screens()
