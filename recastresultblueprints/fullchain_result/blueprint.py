from flask import Blueprint, render_template, jsonify, request
blueprint = Blueprint('fullchain_analysis', __name__, template_folder='templates')

RECAST_ANALYSIS_ID = '19c471ff-2514-eb44-0d82-59563cc38dab'

import json
import os
import glob
from recastbackend.resultaccess import resultfilepath

@blueprint.route('/result/<requestId>/<parameter_pt>')
def result_view(requestId,parameter_pt):
  resultdir  = resultfilepath(requestId,parameter_pt,'dedicated','')
  feynmandiags = [x.rstrip('.pdf').replace(resultdir+'/','') for x in glob.glob('{}/feynmandiags/*.pdf'.format(resultdir))]
  return render_template('result.html',analysisId = RECAST_ANALYSIS_ID,requestId=requestId,parameter_pt=parameter_pt, feynmandiags = feynmandiags)
