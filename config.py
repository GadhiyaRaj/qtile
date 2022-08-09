# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import extension

mod = "mod1"
super = "mod4"
terminal = guess_terminal()
wallpaper_path="/home/raj/Pictures/Wallpapers/"
wallpaper_image="tree.jpg"
user_terminal = "alacritty"


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    #Key([super], "l", lazy.run_extension(extension.WindowList(all_group=False))),
    #Key([super], "d", lazy.run_extension(extension.DmenuRun(dmenu_prompt=">",dmenu_font="Andika-8",background="15181a",foreground="ooff00",dmenu_height=24))),
    Key([mod], "Return", lazy.spawn(user_terminal), desc="Launch terminal"),
    #User Changes
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch Firefox browser"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Launch Thunar file manager"),
    Key([mod], "c", lazy.spawn("code"), desc="Launch Visual Studio Code"),
    #Run Launcher and Task Switcher
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Open application launcher program"),
    #Key([mod], "space", lazy.spawn("rofi -show window"), desc="Task switcher"),
    # Toggle between different layouts as defined below
    Key([super], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    #KeyChord([super,mod], "l", [Key([], "x", lazy.spawn("xfce4-terminal"))])
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
# Default layout configuration
default_layout_configuration = {
	"border_focus":"#9999ff",
	"border_normal":"#ea8304",
	"border_width":3,
	"border_on_single":True,
	"margin":3,
	"margin_on_single":12
}
treetab_layout_configuration = {
	"active_bg":"#9999ff",
	"active_fg":"#000000",
	"inactive_bg":"#ea8304",
	"inactive_fg":"#000000",
	"fontsize":12,
	"panel_width":120,
	"padding_y":5,
	"padding_left":0
}

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4, **default_layout_configuration),
    layout.Columns(**default_layout_configuration),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.Matrix(**default_layout_configuration),
    layout.MonadTall(**default_layout_configuration, single_margin=12),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(**treetab_layout_configuration),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    #layout.Floating())
]

widget_defaults = dict(
    font="Ubuntu Bold",
    foreground="#ffffff",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

##### Mouse Callbacks #####
# def open_speedtest_site():
#     cmd_spawn("firefox")

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(highlight_method="block", hide_unused=True),
                widget.Prompt(),
                widget.WindowName(font="sans"),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                #widget.Systray(),
                #widget.Wlan(),
                #widget.Clipboard(),
                #widget.TextBox("🢐", fontsize=39, foreground="#00d9ff", padding=-2),
                widget.CurrentLayoutIcon(scale=0.7),
                widget.CurrentLayout(font="Ubuntu Bold", foreground="#ff69b3"),
                widget.TextBox(" "),
                widget.CheckUpdates(colour_no_updates="#10d3a9", colour_have_updates="#10d3a9", no_update_string="System up to date", mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(f"{user_terminal} -e sudo pacman -Syu")}),
                widget.TextBox(" "),
                widget.Net(foreground="#99bc62", format="{down} ↓↑ {up}", mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("xdg-open https://fast.com")}),
                widget.TextBox(" "),
                widget.Volume(foreground="#ab96db"),
                widget.TextBox(" "),
                widget.Battery(format="{char} {percent}", low_foreground="#000000", low_background="#ff0000", foreground="#fc766a", charge_char="+", discharge_char="-"),
                widget.TextBox(" "),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", foreground="#78a7d3")#, foreground="#ffffff"),
                #widget.QuickExit(),
            ],
            24,
	    background="282a36"
	    #background="#9013FE",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    wallpaper=wallpaper_path+wallpaper_image
),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
