from config import app
from flask import request,redirect,render_template,make_response,jsonify
import logging
import controller
import redislogic
from model import *



logging.basicConfig(level=logging.INFO)

@app.route("/api/home",methods=["GET"])
def show_form_for_user_input():
    return render_template("index.html")

@app.route("/generate",methods=["POST"])
def generate_hashed_url():
    input_url=request.form.get("input_url")
    is_valid=controller.find_if_valid_url(input_url)
    if(is_valid):
        logging.info("URL that we have recieved from user is ",input_url)
        result_count=check_record_exists_in_db(input_url)
        if(result_count==0):
            output_string=controller.shorten_url(input_url)
            insert_hashed_url_into_db(input_url,output_string)
            logging.info("Hashed String has been saved into the DB with result ",output_string)
            redislogic.store_key_value_pair_in_redis(input_url,output_string)
            redirection_string="s/"+output_string
            response=make_response(render_template("index.html",shortened_url=redirection_string),200)
            return response
        else:
            logging.info("Record already exists, hence not adding it into the DB")
            return jsonify({"message":"Record already exists in DB,not adding it again"}),409
    else:
    
        return jsonify({"message":"Are you sure the URL that you have entered is a valid URL?"}),400

@app.route("/s/<shorten_url>",methods=["GET"])
def redirect_to_actual_url(shorten_url):
    value=redislogic.get_mapping_from_redis(shorten_url)
    if(value==""):
        logging.info("The value is being fetched from DB and not Cache")
        actual_url=get_actual_url_from_hashed_url_db(shorten_url)
        response=make_response(redirect(actual_url),302)
        return response
    else:
        logging.info("The value is being read from Cache and not DB")
        response=make_response(redirect(value),302)
        return response
