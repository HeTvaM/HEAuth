import pytest
import request

URL = "http://127.0.0.1:8100/app/input"

def create_token():
    data = {
        "login": "Test",
        "ip":"22.22.22.22",
        "status": "open"
    }

    return request.post(URL, data=data)

def test_len_token():
    assert 25 == len(create_token())
