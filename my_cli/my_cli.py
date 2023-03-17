# -*- coding: utf-8 -*-
  
"""Console script for my_cli."""
import sys
import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', help='input file name', required=True)
@click.option('--path', help='file path')
def read(name, path):
    click.echo('reading file...')
    click.echo(f'name: {name}, path: {path}')

@cli.command()
@click.option('--text', default='default text', help='echo text', required=True)
def echo(text):
    click.echo(text)
