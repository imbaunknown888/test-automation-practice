import pytest
import requests

def status(response, expected):
    assert response.status_code == expected, f"Expected {expected}, got {response.status_code}"