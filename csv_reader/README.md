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
clone https://github.com/serinko/python_fun
cd python_fun/csv_reader
chmod +x table.py
```

Add to `~/.bashrc` or `~/.zshrc`:

```bash
alias csv=~/{path_to_file}/table.py
```
Restart the shell.

**Usage**

```bash
# simple use
csv {file.csv}
# to get help menu
csv -h 
```

Prints with index by default, to display without an index, use:

```
csv -i {file.csv}

```

**Examples**

`$ cat` command output: 

```bash
$ cat data/example.csv

Q1,January,February,March
1st,Monday,Thursday,Thursday
2nd,Tuesday,Friday,Friday
3rd,Wednesday,Saturday,Saturday
4th,Thursday,Sunday,Sunday
5th,Friday,Monday,Monday
6th,Saturday,Tuesday,Tuesday
7th,Sunday,Wednesday,Wednesday
...
```
Using the script by default `csv {file}`:
```bash
$ csv data/example.csv

|    | Q1   | January   | February   | March     |
|---:|:-----|:----------|:-----------|:----------|
|  0 | 1st  | Monday    | Thursday   | Thursday  |
|  1 | 2nd  | Tuesday   | Friday     | Friday    |
|  2 | 3rd  | Wednesday | Saturday   | Saturday  |
|  3 | 4th  | Thursday  | Sunday     | Sunday    |
|  4 | 5th  | Friday    | Monday     | Monday    |
|  5 | 6th  | Saturday  | Tuesday    | Tuesday   |
|  6 | 7th  | Sunday    | Wednesday  | Wednesday |
|  7 | 8th  | Monday    | Thursday   | Thursday  |
...
```
Using the script with tabulate option without index `csv -t -i {file}`:
```bash
 csv -t -i data/example.csv
+------+-----------+------------+-----------+
| Q1   | January   | February   | March     |
+======+===========+============+===========+
| 1st  | Monday    | Thursday   | Thursday  |
+------+-----------+------------+-----------+
| 2nd  | Tuesday   | Friday     | Friday    |
+------+-----------+------------+-----------+
| 3rd  | Wednesday | Saturday   | Saturday  |
+------+-----------+------------+-----------+
| 4th  | Thursday  | Sunday     | Sunday    |
+------+-----------+------------+-----------+
| 5th  | Friday    | Monday     | Monday    |
+------+-----------+------------+-----------+
| 6th  | Saturday  | Tuesday    | Tuesday   |
+------+-----------+------------+-----------+
| 7th  | Sunday    | Wednesday  | Wednesday |
+------+-----------+------------+-----------+
| 8th  | Monday    | Thursday   | Thursday  |
+------+-----------+------------+-----------+
...
```
