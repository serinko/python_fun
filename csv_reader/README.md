# CSV READER

**Dependencies**

* Python3
* pip modules:
    - argparse
    - pandas
    - sys
    - pathlib

**Setup**

```bash
https://github.com/serinko/python_fun
cd python_fun/csv_reader
chmod +x table.py
```

Add to `~/.bashrc` or `~/.zshrc`:

```
alias csv=~/{path_to_file}/table.py
```
Restart the shell.

**Usage**

```
csv {file.csv}
```

Prints with index by default, to display without an index, use:

```
csv -i {file.csv}
```

