import redis
import logging
import constants

def establish_connection_with_redis():
    r = redis.StrictRedis(host=constants.REDIS_HOST, port=constants.REDIS_PORT, db=constants.REDIS_DB)
    return r

def store_key_value_pair_in_redis(actual_url,hashed_url):
    r = establish_connection_with_redis()
    r.setex(hashed_url,constants.REDIS_TTL,actual_url)
    logging.info("Mapping Stored Successfully")
    r.close()


def get_mapping_from_redis(hashed_url):
    print("Hashed URL Received from input is ",hashed_url)
    r = redis.StrictRedis(host=constants.REDIS_HOST, port=constants.REDIS_PORT, db=constants.REDIS_DB)
    value=r.get(hashed_url)
    if value is not None:
        value=value.decode('utf-8')
        r.close()
        return value
    else:
        r.close()
        return ""
    
    
