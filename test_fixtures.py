import pytest


@pytest.fixture
def sample_data():
    data = {"name": "Subha", "Age": 37}
    return data

def test_method_one(sample_data):
    assert sample_data["name"] == "Subha"
    assert sample_data["Age"] == 37
    print("Success")    