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
crt_w = ("Create window:","[Ctrl]+[b] .. [c]")

swt_w = ("Switch / select window by number:","[Ctrl]+[b] .. [0-9 numbers]")

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
    swt_w
]

print(tabulate(table))