import json
import os
import glob
import recastbackend.resultaccess

from flask import Blueprint, render_template, jsonify, request
blueprint = Blueprint('capbackend_result', __name__, template_folder='templates')

@blueprint.route('/result/<basicreqid>')
def result_view(basicreqid):

    resultdir =  recastbackend.resultaccess.resultfilepath(basicreqid,'capbackend','').rstrip('/')
    resultsfiles = []
    for dirpath,subdirs,files in os.walk(resultdir):
        for fl in files:
            resultsfiles.append('/'.join([dirpath.replace(resultdir,''),fl]).lstrip('/'))
    return render_template('cap_result.html', basicreqid = basicreqid, resultsfiles = resultsfiles)
