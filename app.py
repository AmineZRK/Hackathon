# -*- coding: utf-8 -*-

"""

Created on Sun Mar 14 06:52:54 20 Mon Jun 20 15:45:00

app web

@author: Thierno Sadou BARRY

"""



from flask import Flask, flash, redirect, render_template, request, session, abort
from saagieapi import *


#configure the app

app = Flask(__name__)



#main page

@app.route("/projet")

def projet():
    saagie = SaagieApi(url_saagie="https://demo-workspace.a4.saagie.io/",
                   id_platform="2",
                   user="ESTIAM_G04_thierno-sadou.barry",
                   password="Hackathong4",
                   realm="demo")
    project=saagie.jobs.list_for_project(project_id="aad54160-3a4b-485d-896f-0e04bd96bcb7", instances_limit=2)
    
  
    return project

#contact page

@app.route('/contact')

def contact():

    mail = "john@doe.com"

    tel = "01 02 03 04 05"

    return "mail: "+mail+" --- phone: "+tel



#member page

@app.route("/members")

def members():

    name = "john doe"

    return name



#member name page

@app.route("/members/<string:name>/")

def getMember(name):

    return name



#run the app

app.run()