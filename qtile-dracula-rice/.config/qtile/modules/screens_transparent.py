import os
from libqtile.config import Screen
from libqtile import bar, qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, BorderDecoration

from modules.prefs import terminal, launcher, power_menu
from modules.pallete import colors

widget_defaults = dict(
    font="JetBrainsMono",
    fontsize = 14,
    padding = 1,
)

decoration_group = {
    "decorations": [
        RectDecoration(colour=colors['bg'], radius=6, filled=True, padding_y=6, group=True)
    ],
}
decoration_group_blue = {
    "decorations": [
        RectDecoration(colour=colors['blue'], radius=6, filled=True, padding_y=6, group=True)
    ],
}

extension_defaults = widget_defaults.copy()

def init_screens():
    return [
        Screen(top=bar.Bar(
            [
                widget.Sep(linewidth=0, padding=15, size_percent=40),
                widget.TextBox(
                    text='󰣇 ',
                    foreground=colors['blue'],
                    padding=20,
                    fontsize=22,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(launcher)},
                    **decoration_group
                ),
                widget.Sep(linewidth=0, padding=20, size_percent=40),
                widget.GroupBox(
                    borderwidth=1,
                    active = colors['blue'],
                    inactive = colors['fg'],
                    highlight_method = "text",
                    this_current_screen_border = colors['green'],
                    disable_drag = True,
                    hide_unused=False,
                    padding=10,
                    spacing=5,
                    **decoration_group
                ),
                widget.Spacer(),
                widget.WindowName(
                    foreground = colors['gray'],
                    width=bar.CALCULATED,
                    decorations=[
                        BorderDecoration(
                            colour = colors['gray'],
                            border_width = [0, 0, 2, 0],
                        )
                    ],
                 ),
                widget.Spacer(),
                widget.Systray(
                    icon_size = 16,
                    padding = 20,
                    background=colors['transparent'],
                ),
                widget.Sep(linewidth=0, padding=20, size_percent=40),
                widget.Clock(
                    foreground=colors['red'],
                    padding = 10,
                    format="  %I:%M %p",
                    **decoration_group
                ),
                widget.Sep(linewidth=0, padding=15, size_percent=40),
                widget.TextBox(
                    text='  ',
                    foreground=colors['red'],
                    padding=20,
                    **decoration_group,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(power_menu)},
                ),
                widget.Sep(linewidth=0, padding=14, size_percent=40),

            ], opacity=1.0, size=44, margin=0, background=colors['transparent']
        ))
    ]

screens = init_screens()
