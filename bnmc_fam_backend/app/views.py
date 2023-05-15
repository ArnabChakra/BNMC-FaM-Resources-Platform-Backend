from flask import Flask, render_template, redirect, url_for, request, session, abort, flash, make_response, jsonify
from app.models import get_categories,get_resources
from app.utils import fuzzy_match_resource
from app import app
import json

@app.route('/categories',methods=['GET'])
def categories():
    response = jsonify({"categories":get_categories()})
    return response

@app.route('/getFamResources',methods=['POST'])
def getFamResources():
    req = json.loads(request.data)
    non_coa,coa = get_resources(req['category'],req['agencyName'],req['zipCode'],req['distance'])
    if req['agencyName']!="":
        non_coa = fuzzy_match_resource(req['agencyName'].lower(),non_coa,int(app.config["FUZZY_THRESHOLD"]))
        coa = fuzzy_match_resource(req['agencyName'].lower(), coa,int(app.config["FUZZY_THRESHOLD"]))
    non_coa_list=[]
    coa_list=[]

    for res in non_coa:
        non_coa_list.append({"name":res['ResourceName'],"address":res['Address'],
                            "tele":res['Telephone'],"email":res['Email'],"website":res['Website'],
                            "info":res['Service Description'],"contact":res['Resource Contact Person']})

    for res in coa:
        coa_list.append({"name":res['ResourceName'],"contact":res['Resource Contact Person'],"email":res['Email']})

    limit=8
    if len(non_coa_list)<8:
        limit=len(non_coa_list)

    response = jsonify({"coalition":coa_list,
                "external":non_coa_list[:limit]})
    return response
