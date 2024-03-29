from tabulate import tabulate
from colorama import Fore, Back, Style


intro = (Fore.MAGENTA + Style.BRIGHT +  "\n\nCOMMAND EXPLANATION:\n" 
         ,"\n$ = Bash terminal command\n: = Tmux command\n"
    "[KEY] = Tmux key-binding" + Style.RESET_ALL)

line = ("=================================================",)

session = (Fore.YELLOW + Style.BRIGHT + "\nTMUX SESSIONS:\n----------\n"+ Style.RESET_ALL,)
run = ("Run tmux:\n","$ tmux")
run_new = ("Start new session:\n", "$ tmux new\n$ tmux new-session\n: new")
start_session = ("Starts new session called 'one':","\n$ tmux new -s one\n"
                                                    ": new -s one")
ls_sessions = ("Shows all sessions:","\n$ tmux ls\n$ tmux list-sessions"\
    "\n[Ctrl]+[b] .. [s]")
kll_all_sessions = ("Kill/delete all sessions but current","$ tmux kill-session -a")
kll_many = ("Kill/delete all but 'one'","$ tmux kill-session -t one")


window = (Fore.YELLOW + Style.BRIGHT + "\nTMUX WINDOWS:\n----------\n" + Style.RESET_ALL,)
new_w = ("Starts new window with the name\n 'one' and window 'onewindow':",
         "\n$ tmux new -s one -n onewindow\n")
rnm_w = ("Rename current window:","[Ctrl]+[b] .. [,]")
cls_w = ("Close current window:","[Ctrl]+[b] .. [&]")
prv_w = ("Previous window:","[Ctrl]+[b] .. [p]")
nxt_w = ("Next window:","[Ctrl]+[b] .. [n]")
crt_w = ("Create window:","[Ctrl]+[b] .. [c]")
swt_w = ("Switch / select window by number:","[Ctrl]+[b] .. [0-9 numbers]")


pane = (Fore.YELLOW + Style.BRIGHT + "\nTMUX PANES:\n----------\n" + Style.RESET_ALL,)
tgl_lst = ("Toggle last active pane:","[Ctrl]+[b] .. [;]")
splt_hrzn = ("Split pane with horizontal layout:","[Ctrl]+[b] .. [%]")
splt_vrt = ("Split pane with vertical layout:",'[Ctrl]+[b] .. ["]')
swt_pn = ("Switch to pane to the direction:","[Ctrl]+[b] .. [arrow_key]")
mv_pn_l = ("Move the current pane left:","[Ctrl]+[b] .. [{]")
mv_pn_r = ("Move the current pane right:","[Ctrl]+[b] .. [}]")
pn_n = ("Show pane numbers:","[Ctrl]+[b] .. [q]")
swt_pn_n = ("Switch pane by number:","[Ctrl]+[b] .. [q] [0-9 numbers]")
tg_pn_z = ("Toggle pane zoom:","[Ctrl]+[b] .. [z]")
pn_win = ("Convert pane into a window:","[Ctrl]+[b] .. [!]")
rs_pn = ("Resize current pane:","[Ctrl]+[b]+[arrow_key]")
tg_pn_lo = ("Toggle between pane layouts:","[Ctrl]+[b] .. [space]")
sw_nx_pn = ("Switch to next pane","[Ctrl]+[b] .. [0]")
cl_pn = ("Close current pane:","[Ctrl]+[b] .. [x]")

copy = (Fore.YELLOW + Style.BRIGHT + "\nCOPY MODE:\n----------\n" + Style.RESET_ALL,)
cp_md = ("Enter copy mode:","[Ctrl]+[b] .. [[]")
cp_scr_pgup = ("Enter copy mode and scroll one page up:","[Ctrl]+[b] .. [PgUp]")
q_m = ("Quit mode:","[q]")
g_tl = ("Go to top line:","[g]")
g_bl = ("Go to bottom line:","[G]")
scr_up = ("Scroll up:","[arrow_up]")
scr_dw = ("Scroll down:","[arrow_down]")
mv_c_l = ("Move cursor left:","[h]")
mv_c_d = ("Move cursor down:","[j]")
mv_c_u = ("Move cursor up:","[k]")
mv_c_r = ("Move cursor right:","[l]")
mv_c_f = ("Move cursor forward one word at a time:","[w]")
mv_c_b = ("Move cursor backward one word at a time:","[b]")
sr_f = ("Serach forward:","[/]")
sr_b = ("Serach backward:","[?]")
n_k_o = ("Next keyward occurance:","[n]")
p_k_o = ("Previous keyward occurance:","[N]")
s_s = ("Start selection:","[Space]")
cl_s = ("Clear selection:","[Esc]")
co_s = ("Copy selection:","[Enter]")
ps_bf = ("Paste contents of buffer_0:","[Ctrl]+[b] .. []]")
ds_bf_c = ("Display buffer_0 contents:",": show-buffer")
cp_v_bf = ("Copy entire visible contents of pane to a buffer:",
           ": capture-pane")
sh_bf = ("Show all buffers:",": list-buffers")
sh_ps = ("Show all buffers and paste selected:",
         ": choose-buffer")
sv_bf = ("Save buffer contents to buf.xt:",": save-buffer buf.txt")
dl_bf = ("Delete buffer_1:",": delete-buffer -b 1")

misc = (Fore.YELLOW + Style.BRIGHT + "\nTMUX MISC:\n----------\n" + Style.RESET_ALL,)
cmd = (Fore.MAGENTA + Style.BRIGHT + "Enter command mode:","[Ctrl]+[b] .. [:]" + Style.RESET_ALL)
op_ss = ("Set OPTION for all sessions:",": set -g OPTION:")
op_wn = ("Set OPTION for all windows:",": setw -g OPTION")
ms_on = ("Enable mouse mode:",": set mouse on")

hlp = (Fore.YELLOW + Style.BRIGHT + "\nTMUX HELP:\n----------\n" + Style.RESET_ALL,)
lst = ("List key bindings(shortcuts):","$ tmux list-keys\n: list-keys"
                                       "\n[Ctrl]+[b] .. [?]")
inf = ("Show every session, window, pane, etc... :","$ tmux info")

custom = (Fore.YELLOW + Style.BRIGHT + "\nCUSTOMIZE TMUX:\n----------\n" + Style.RESET_ALL,)
clrs = ("256 colors to work in Tmux:","- open .bashrc file (usually home dir)"
                                      "\n- paste to a new line: "
                                      "'export TERM=screen-256color'"
                                      "\n- save and close .bashrc"
                                      "\n- restart Tmux.")

table = [
    intro,
    cmd,
    line,
    session,
    run,
    run_new,
    start_session,
    ls_sessions,
    kll_all_sessions,
    kll_many,
    line,
    window,
    new_w,
    crt_w,
    rnm_w,
    cls_w,
    prv_w,
    nxt_w,
    swt_w,
    line,
    pane,
    tgl_lst,
    splt_hrzn,
    splt_vrt,
    swt_pn,
    mv_pn_l,
    mv_pn_r,
    pn_n,
    swt_pn_n,
    tg_pn_z,
    pn_win,
    rs_pn,
    tg_pn_lo,
    sw_nx_pn,
    cl_pn,
    line,
    copy,
    cp_md,
    cp_scr_pgup,
    q_m,
    g_tl,
    g_bl,
    scr_up,
    scr_dw,
    mv_c_l,
    mv_c_d,
    mv_c_u,
    mv_c_r,
    mv_c_f,
    mv_c_b,
    sr_f,
    sr_b,
    n_k_o,
    p_k_o,
    s_s,
    cl_s,
    co_s,
    ps_bf,
    ds_bf_c,
    cp_v_bf,
    sh_bf,
    sh_ps,
    sv_bf,
    dl_bf,
    line,
    misc,
    cmd,
    op_ss,
    op_wn,
    ms_on,
    line,
    hlp,
    lst,
    inf,
    line,
    custom,
    clrs,
]

print(tabulate(table))
