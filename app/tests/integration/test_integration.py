import pytest
import sys
sys.path.append('')
import controller,redislogic,model
import integration_constants


actual_url=integration_constants.ACTUAL_URL



def test_01_hashing_of_url():
    hashed_url=controller.shorten_url(actual_url)
    pytest.assume(hashed_url,"Hashed URL shouldnt be empty or null")
    pytest.assume(len(hashed_url)==integration_constants.EXPECTED_HASHED_URL_LENGTH,f"Expected length of the hashed URL must be 7 characters long")


def test_02_insertion_of_hashed_url_in_db():
    hashed_url=controller.shorten_url(actual_url)
    model.insert_hashed_url_into_db(integration_constants.ACTUAL_URL,hashed_url)
    result_count=model.check_record_exists_in_db(integration_constants.ACTUAL_URL)
    assert result_count==1,f"Expected Exactly 1 record in the DB for the URL"



def test_03_insertion_and_fetch_data_from_redis():
    hashed_url=controller.shorten_url(actual_url)
    redislogic.store_key_value_pair_in_redis(actual_url,hashed_url)
    value=redislogic.get_mapping_from_redis(hashed_url)
    assert value,f"The value fetched from Redis shouldnt be empty"



