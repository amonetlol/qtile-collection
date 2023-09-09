from libqtile import layout
from libqtile.lazy import lazy
from libqtile.config import Click, Drag, Match

from modules.prefs import mod, alt
from modules.pallete import colors

layout_theme = {
    "border_width": 2,
    "margin": 10,
    "border_focus": colors['gray'],
    "border_normal": colors['black'],
    "grow_amount": 1,
}

layouts = [
    layout.MonadThreeCol(max_ratio=0.6,ratio=0.5, main_centered=True, new_client_position="bottom", align="right", **layout_theme),
    layout.MonadTall(max_ratio=0.75,ratio=0.60,**layout_theme),
    layout.MonadWide(max_ratio=0.75,ratio=0.60,**layout_theme),
    layout.Floating(**layout_theme),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="Pavucontrol"),  
        Match(wm_class="Nitrogen"),
        Match(wm_class="Lxappearance"),
    ],
    **layout_theme
)

# Drag floating layouts.
mouse = [
    Drag([alt], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([alt], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = [] 
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = False
auto_minimize = True

wmname = "Qtile"
