"""
This module deals with E2E testing (majorly focussing on happy flow)

Author: Anubhav Sanyal
Last Updation Date: 25/11/2023
"""
import pytest
import sys
sys.path.append('')
import requests
import e2e_constants
import redislogic,model,controller


def test_happy_flow_scenario_for_url_generation():
    actual_url=e2e_constants.ACTUAL_URL
    hashed_url=controller.shorten_url(actual_url)
    response=requests.post(url="http://app:1215/generate",data={"input_url":actual_url})
    pytest.assume(response.status_code==200,"For Valid URL, status code must be 200")
    result_count=model.check_record_exists_in_db(actual_url)
    pytest.assume(result_count==1,"Exactly one record should exists in the DB for this URL")
    value=redislogic.get_mapping_from_redis(hashed_url=hashed_url)
    pytest.assume(value,"The value fetched from Redis should not be null or empty")

def test_negative_scenario_for_url_generation():
    actual_url=e2e_constants.INVALID_URL
    response=requests.post(url="http://app:1215/generate",data={"input_url":actual_url})
    assert response.status_code==400,f"Since invalid URL was supplied, expected status code of 400"

def test_happy_flow_scenario_for_redirection():
    actual_url=e2e_constants.ACTUAL_URL
    hashed_url=controller.shorten_url(actual_url)
    response=requests.get("http://app:1215/s/"+hashed_url,allow_redirects=False)
    assert response.status_code==302,f"Since the URL exists,it should be redirected"


