#!/usr/bin/python3
"""Simple commandline tool to read csv files in terminal"""

import argparse
import pandas as pd
import sys
import pathlib
import csv

def create_table(args):
    file = args.file    
    csv = pd.read_csv(file)
    if args.index:
        if args.table:
            table = csv.to_markdown(tablefmt="grid")
        else:
            table = csv.to_markdown()
    else:
        if args.table:
            table = csv.to_markdown(tablefmt="grid", index=False)
        else:
            table = csv.to_markdown(index = False)
    return table
        
def import_csv(args):
    file = args.file
    csv = pd.read_csv(file)
    
      
def display_file(args):
    """Display csv file as a sorted page or a table"""
    table = create_table(args)
    
    print(table)
        
def panic(msg):
    """Error message print"""
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(-1)

def parser_main():
    """Main function initializing ArgumentParser, storing arguments and executing commands."""    
    # Top level parser
    parser = argparse.ArgumentParser(
            prog='CSV TERMINAL READER',
            description='''Quickly prints .csv files in terminal''',
            epilog='''Code is power!'''
        )
        
    # Parser arguments    
    parser.add_argument("-V","--version", action="version", version='%(prog)s 1.1.0')
    parser.add_argument("file", help="csv file name")
    parser.add_argument("-t","--table", default=False, action="store_true", help="output with a tabulate option")
    parser.add_argument("-i","--index", default=True, action="store_false", help="output without an index column")
    # possible to change default by: default = False, action="store_true"
    
    parser.set_defaults(func=display_file)
    args = parser.parse_args()
    
    try:
        args.func(args)
    except AttributeError as e:
        msg = f"{e}.\nPlease run: csv --help or read the error message in case your .csv file is corrupted."
        panic(msg)

if __name__ == '__main__':
    parser_main()
    
