from tabulate import tabulate

intro = ("\n\nCOMMAND EXPLANATION:\n"
         "----------","\n$ = Bash terminal command\n: = Tmux command\n"
    "[KEY] = shortcut Tmux")

session = ("TMUX SESSIONS:\n----------\n",)
run = ("Run tmux:\n","$ tmux")
run_new = ("Start new session:\n", "$ tmux new\n$ tmux new-session\n: new")
start_session = ("Starts new session called 'one':","\n$ tmux new -s one\n"
                                                    ": new -s one")
ls_sessions = ("Shows all sessions:","\n$ tmux ls\n$ tmux list-sessions"\
    "\n[Ctrl]+[b] .. [s]")

sessions = [intro, session, run, run_new, start_session, ls_sessions]

print(tabulate(sessions))

