from src.importing.importTestData import get_file_pathAsd


def setup():
    print("SETUP!")


def teardown():
    print("TEAR DOWN!")


def test_importTestData():
    assert get_file_pathAsd() == 1

test_importTestData()
