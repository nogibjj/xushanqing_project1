#!/usr/bin/env python

import click
from process_data import filter_state

#build a click group
@click.group()
def cli():
    """query to research covid-19 cases data in US from 2020-1-21 to 2022-5-23!"""

#build a click command
@cli.command()
@click.option("--statename", default="Washington", help="Please type the state name to show the latest covid-19 data")
def cli_query(statename):
    """Execute query from covid-19 cases dataset to search covid-19 cases data in US from 2020-1-21 to 2022-5-23!"""
    result = filter_state(statename)
    print("Latest Result for {} is: \n {}".format(statename,result))
  #run the CLI
if __name__ == "__main__":
    cli()