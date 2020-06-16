'''
    File name: cli.py
    Project: aXe reporter
    Author: Björn-Olle Rylander
    Date created: 2019-07-07
    Python Version: 3.7.4
    Description: Command line interface functionality
'''

import click
from flask.cli import AppGroup
import csv
import json
import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from axe_selenium_python import Axe

from flask import current_app as app


axe_path = app.config['AXE_PATH']
axe_cli = AppGroup('axe')


def test_page(page):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(page[1])
    axe = Axe(driver)

    # Inject axe-core javascript into page.
    axe.inject()

    # Run axe accessibility checks.
    results = axe.run()

    # Relevant tags
    tags = ['wcag2aa', 'wcag2aa', 'best-practice']
    report =\
        [violation for violation in results['violations']
            if bool(set(violation['tags']) & set(tags))]

    # Write results to file
    axe.write_results(report, axe_path + 'reports/' + page[0] + '.json')

    driver.close()
    return True


@axe_cli.command("run")
def validate_content(source=False):
    """Parse urls.json and run a11y test"""
    click.echo('')
    click.echo('-----------------------------')

    # with open(axe_path + 'pages.json') as json_file:
    #     pages = json.load(json_file)
    
    with open(axe_path + 'pages.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        pages = []
        for row in csv_reader:
            pages.append(row)

    for page in pages:
        click.echo("Creating report: {0} ({1})".format(page[0], page[1]))
        test_page(page)

    click.echo('-----------------------------')
    click.echo('')
