'''
    File name: routes.py
    Project: aXe reporter
    Author: Björn-Olle Rylander
    Date created: 2019-07-07
    Python Version: 3.7.4
    Description: Main routes
'''

from flask import (
    Blueprint,
    current_app as app,
    render_template,
    redirect,
    flash,
    abort, 
    url_for,
    request
)
import json


main_bp = Blueprint('main_bp', __name__)
axe_path = app.config['AXE_PATH']


@main_bp.route('/')
def home():
    current_page = request.args.get('page')
    import csv

    with open(axe_path + 'pages.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        pages = []
        for row in csv_reader:
            pages.append(row)

    # with open(axe_path + 'pages.json') as json_file:
    #     pages = json.load(json_file)
    
    with open(axe_path + 'riktlinjer.json') as json_file:
        riktlinjer = json.load(json_file)

    report = []

    for page in pages:
        with open(axe_path + 'reports/' + page[0] + '.json') as json_file:
            file_data = json.load(json_file)
            
            for row in file_data:
                row['page'] = page[0]
                report.append(row)


    sortorder={"critical": 0, "serious":1, "moderate":2, "minor":3}
    report.sort(key=lambda x: (sortorder[x["impact"]], x['page']))
    

    templateData = {
        'title': "aXe - report",
        'pages': pages,
        'report': report,
        'riktlinjer': riktlinjer,
        'current_page': current_page
    }
    
    return render_template('page.html', **templateData)
