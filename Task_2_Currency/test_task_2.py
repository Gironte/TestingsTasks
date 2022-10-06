import json
import task_2
import pytest

with open("config.json", "r") as jsonfile:
    config = json.load(jsonfile)

def test_run_currency_withMultiplePath_GBP_EUR_pathfound():
    assert task_2.run("GBP", "EUR", config) == [['GBP/USD'], ['USD/CZK'], ['CZK/EUR']]

def test_run_currency_withOnePath_DKK_EUR_pathfound():
    assert task_2.run("DKK", "EUR", config) == [['DKK/EUR']]

def test_run_currency_onlyInputLink_AUD_exception():
     with pytest.raises(Exception):
        task_2.run("AUD", "CZK", config)

def test_run_currency_withoutOutputLink_USD_AUD_exception():
     with pytest.raises(Exception):
        task_2.run("USD", "AUD", config)

def test_run_onlyOneInputCurrency_exception():
     with pytest.raises(Exception):
        task_2.run("USD", "", config)

def test_run_incorrectCurrency_exception():
     with pytest.raises(Exception):
        task_2.run("ERR", "QQQ", config)

def test_run_incorrectInput_exception():
     with pytest.raises(Exception):
        task_2.run(True, 123, config)