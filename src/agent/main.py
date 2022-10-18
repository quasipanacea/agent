import argparse
import sys
import typer

from agent import subcommands, util

def run():
    app()

app = typer.Typer()

@app.command()
def app_build():
    subcommands.app_build()

@app.command()
def app_install(
    dev: bool = typer.Option(False),
    nightly: bool = typer.Option(False)
):
    util.must_either_dev_or_nightly(dev, nightly)
    subcommands.app_install(dev, nightly)

@app.command()
def app_uninstall(
    dev: bool = typer.Option(False),
    nightly: bool = typer.Option(False)
):
    util.must_either_dev_or_nightly(dev, nightly)
    subcommands.app_uninstall(dev, nightly)

@app.command()
def launch():
    subcommands.launch()

@app.command()
def webext_native_client():
    subcommands.webext_native_client()

