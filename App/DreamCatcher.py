#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################################################################
#                                                                                                                      #
#   AUTHOR: Morgan Pothoff                                                                                             #
#   LAST UPDATED: 11/15/2021                                                                                           #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from flask import *
from datetime import datetime

#import DB_Connections


app = Flask(__name__, static_url_path="/static")


@app.route("/")
def home():
	return render_template("Home.html")


@app.route("/NewDream")
def newDream():
	return render_template("NewDream.html")


app.run(host="localhost", port=8000, debug=True)