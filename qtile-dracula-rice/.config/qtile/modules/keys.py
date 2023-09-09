from libqtile.config import Drag, Click, Key
from libqtile.lazy import lazy

from modules.prefs import mod, terminal, browser, private, file_manager, screenshot_tool, code_editor, launcher, power_menu

keys = [
    
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "p", lazy.spawn(launcher), desc="Launch Menu"),
    Key([mod], "q", lazy.spawn(power_menu), desc="Launch Power Menu"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),

    # Launche Applications
    Key([mod, "control"], "b", lazy.spawn(browser), desc="Launch Browser"),
    Key([mod, "control"], "p", lazy.spawn(private), desc="Launch Incognito Browser"),
    Key([mod, "control"], "e", lazy.spawn(code_editor), desc="Launch Editor"),
    Key([mod, "control"], "f", lazy.spawn(file_manager), desc="Launch File Manager"),
    
    # Take Screenshot
    Key([], "Print", lazy.spawn(screenshot_tool), desc="Take a Screenshot"),

    # Media hotkeys
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pactl set-sink-volume 0 +5%'), desc="Raise Volume"),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('pactl set-sink-volume 0 -5%'), desc="Lower Volume"),
    Key([], 'XF86AudioMute', lazy.spawn('pactl set-sink-mute 0 toggle'), desc="Mute Volume"),
    Key([], 'XF86AudioPlay', lazy.spawn('playerctl play-pause'), desc="Play / Pause Media"),
    Key([], 'XF86AudioNext', lazy.spawn('playerctl next'), desc="Play Next"),
    Key([], 'XF86AudioPrev', lazy.spawn('playerctl previous'), desc="Play Previous"),
    
    # More Window Stuff
    Key([mod], 'f', lazy.window.toggle_floating()),
    Key([mod], 'm', lazy.window.toggle_fullscreen()),
    Key([mod], 'n', lazy.window.toggle_minimize()),

    # Move Between Workspaces
    Key([mod, "shift"], 'Tab', lazy.screen.next_group()),
    Key([mod, "control"], 'Tab', lazy.screen.prev_group()),

    # Brigtness
    Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl s 10+'), desc="Increase Brightness"),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl s 10-'), desc="Decrease Brightness"), 

    # Switch Monitors
    Key([mod], 'period', lazy.next_screen(), desc="Next monitor"),

    # Hide/show bar
    Key([mod], 'b', lazy.hide_show_bar()),

]


