import os
from libqtile.config import Screen
from libqtile import bar, qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

from modules.prefs import terminal, launcher, power_menu
from modules.pallete import colors

widget_defaults = dict(
    font="Azeret Mono",
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
                widget.Sep(linewidth=0, padding=14, size_percent=40, background=colors['green'],**powerline),
                widget.TextBox(
                    text=' 󰣇 ',
                    foreground=colors['black'],
                    background=colors['green'],
                    padding=2,
                    fontsize=22,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(launcher)},
                ),
                widget.CurrentLayout(
                    padding=1,
                    foreground=colors['black'],
                    background=colors['green'],
                ),
                widget.Sep(linewidth=0, padding=14, size_percent=40, background=colors['green'],**powerline),
                widget.GroupBox(
                    background=colors['bg'],
                    borderwidth=1,
                    active = colors['yellow'],
                    inactive = colors['magenta'],
                    highlight_method = "line",
                    highlight_color = colors['bg'],
                    this_current_screen_border = colors['yellow'],
                    disable_drag = True,
                    hide_unused=False,
                    padding=10,
                    spacing=5,
                ),
                widget.WindowName(
                    foreground=colors['bluegray'],
                    background=colors['bg'],
                    width = bar.CALCULATED,
                    padding=10,
                    **powerline
                ),
                widget.Spacer(background=colors['black']),
                widget.Wttr(
                    location={
                        'Maricopa': 'Maricopa',
                    },
                    #format='%l: %C, temp: %t, feels: %f',
                    format="%l: %C %t",
                    units='m',
                    update_interval=30,
                    padding = 1,
                    background=colors['black'],
                    foreground=colors['fg'],
                ),
                widget.Spacer(background=colors['black'],**powerline),
                widget.Mpris2(
                    format = "{xesam:title} - ({xesam:artist})",
                    foreground=colors['bluegray'],
                    playing_text = " 契 {track}",
                    paused_text  = "  {track}",
                    width = bar.CALCULATED,
                    scroll = False,
                    poll_interval = 1,
                ),
                widget.Systray(
                    background=colors['bg'],
                    icon_size = 16,
                    padding = 20,
                ),
                widget.Sep(linewidth=0, padding=14, size_percent=40, background=colors['bg'],**powerline),
                widget.Clock(
                    foreground=colors['bg'],
                    background=colors['red'],
                    padding = 10,
                    format="󱡼  %I:%M %p",
                    timezone="Asia/Kolkata",
                ),
                widget.Clock(
                    foreground=colors['black'],
                    background=colors['red'],
                    padding = 10,
                    format="  %I:%M %p "
                ),
                widget.TextBox(
                    text='  ',
                    foreground=colors['black'],
                    background=colors['red'],
                    padding=2,
                    fontsize=22,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(power_menu)},
                ),
            ], opacity=1.0, size=38, margin=0,
        ))
    ]

screens = init_screens()
