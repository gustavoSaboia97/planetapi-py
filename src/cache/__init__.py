from requests import Session
from cachecontrol import CacheControl
from cachecontrol.heuristics import ExpiresAfter

sess_one_day = CacheControl(Session(), heuristic=ExpiresAfter(days=1))


def get_requester_one_day_cache() -> CacheControl:
    return sess_one_day
