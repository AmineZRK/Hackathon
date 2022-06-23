# -*- coding: utf-8 -*-

"""

Created on Sun Mar 14 06:52:54 20 Mon Jun 20 15:45:00

app web

@author: Thierno Sadou BARRY

"""




from flask_cors import cross_origin,CORS
from flask import Flask, flash, redirect, render_template, request, session, abort
from saagieapi import *


#configure the app

app = Flask(__name__)
cors = CORS(app, resources={r"/project/info": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
saagie = SaagieApi(url_saagie="https://demo-workspace.a4.saagie.io/",
                   id_platform="2",
                   user="ESTIAM_G04_thierno-sadou.barry",
                   password="Hackathong4",
                   realm="demo")

#main page

@app.route("/project")

def projet():
    project=saagie.projects.list()
    return project

@app.route("/pro")

def projet_inf():
    return null
    

@app.route("/project/info")
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def projet_info():
    id = request.args['id']
    id = chr(id)
    info=saagie.projects.get_info(id)
    return info



@app.route("/jobs", methods=['POST','GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def jobs():
    id = request.args.get('pro')
    project=saagie.jobs.list_for_project(project_id=id, instances_limit=2)
    return project


#contact page

@app.route('/contact')

def contact():

   

    return "mail: "+mail+" --- phone: "+tel



#member page

@app.route("/members",methods=['POST','GET'])

def members():

    inf=request.args['inf']
    #info=saagie.projects.get_info('ff6d44b0-141e-435d-a4c3-a2642fac2d78')
    inf = chr(inf)
    info=saagie.projects.get_info(inf)
    return info



#member name page

@app.route("/members/<string:name>/")

def getMember(name):
    info=saagie.jobs.list_for_project(project_id=name, instances_limit=2)
    return info



#run the app

app.run()