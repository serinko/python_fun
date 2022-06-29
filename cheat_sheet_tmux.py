from tabulate import tabulate

intro = ("\n\nCOMMAND EXPLANATION:\n"
         ,"\n$ = Bash terminal command\n: = Tmux command\n"
    "[KEY] = shortcut Tmux")

session = ("\nTMUX SESSIONS:\n----------\n",)
run = ("Run tmux:\n","$ tmux")
run_new = ("Start new session:\n", "$ tmux new\n$ tmux new-session\n: new")
start_session = ("Starts new session called 'one':","\n$ tmux new -s one\n"
                                                    ": new -s one")
ls_sessions = ("Shows all sessions:","\n$ tmux ls\n$ tmux list-sessions"\
    "\n[Ctrl]+[b] .. [s]")

window = ("\nTMUX WINDOWS:\n----------\n",)
new_w = ("Starts new window with the name\n 'one' and window 'onewindow':",
         "\n$ tmux new -s one -n onewindow\n")
rnm_w = ("Rename current window:","[Ctrl]+[b] .. [,]")
cls_w = ("Close current window:","[Ctrl]+[b] .. [&]")
prv_w = ("Previous window:","[Ctrl]+[b] .. [p]")
nxt_w = ("Next window:","[Ctrl]+[b] .. [n]")
crt_w = ("Create window:","[Ctrl]+[b] .. [c]")
swt_w = ("Switch / select window by number:","[Ctrl]+[b] .. [0-9 numbers]")

pane = ("\nTMUX PANES:\n----------\n",)
tgl_lst = ("Toggle last active pane:","[Ctrl]+[b] .. [;]")
splt_hrzn = ("Split pane with horizontal layout:","[Ctrl]+[b] .. [%]")
splt_vrt = ("Split pane with vertical layout:",'[Ctrl]+[b] .. ["]')
swt_pn = ("Switch to pane to the direction:","[Ctrl]+[b] .. [arrow_key]")
mv_pn_l = ("Move the current pane left:","[Ctrl]+[b] .. [{]")
mv_pn_r = ("Move the current pane left:","[Ctrl]+[b] .. [}]")
pn_n = ("Show pane numbers:","[Ctrl]+[b] .. [q]")
swt_pn_n = ("Switch pane by number:","[Ctrl]+[b] .. [q] [0-9 numbers]")
tg_pn_z = ("Toggle pane zoom:","[Ctrl]+[b] .. [z]")
pn_win = ("Convert pane into a window:","[Ctrl]+[b] .. [!]")
rs_pn = ("Resize current pane:","[Ctrl]+[b]+[arrow_key]")
tg_pn_lo = ("Toggle between pane layouts:","[Ctrl]+[b] .. [space]")
sw_nx_pn = ("Switch to next pane","[Ctrl]+[b] .. [0]")
cl_pn = ("Close current pane:","[Ctrl]+[b] .. [x]")



table = [
    intro,
    session,
    run,
    run_new,
    start_session,
    ls_sessions,
    window,
    new_w,
    crt_w,
    rnm_w,
    cls_w,
    prv_w,
    nxt_w,
    swt_w,
    pane,

]

print(tabulate(table))