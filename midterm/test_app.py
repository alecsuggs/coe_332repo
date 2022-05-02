#!/usr/bin/env python3

from app import data_upload, help, welcome_page,\
    epoch_info, all_epochs, countries, country_info, region_info, regions, city_info, cities
import xmltodict
import pytest
from app import app


global positionaldata
global sightings
with open('ISS.OEM_J2K_EPH.xml', 'r') as f:
    positionaldata = xmltodict.parse(f.read())
with open('XMLsightingData_citiesINT01.xml', 'r') as f:
    sightings = xmltodict.parse(f.read())

@pytest.fixture()
def client():
    return app.test_client()


def test_data_upload(client):
    resp = client.post('/load')
    assert resp.status_code == 200
    assert isinstance(data_upload(), str) == True

def test_help():
    assert isinstance(help(), str) == True


def test_welcome_page():
    assert isinstance(welcome_page(), str) == True


def test_epoch_info(client):
    resp = client.get('/epochs/2022-057T11:28:56.869Z')
    assert resp.status_code == 200
    assert isinstance(resp.json, dict) == True


def test_all_epochs(client):
    resp = client.get("/epochs")
    assert resp.status_code == 200
    assert isinstance(resp.json, dict) == True


def test_countries(client):
    resp = client.get("/countries")
    assert resp.status_code == 200
    assert isinstance(resp.json, dict) == True


def test_country_info(client):
    resp = client.get("/countries/Australia")
    assert resp.status_code == 200
    assert isinstance(resp.json, dict) == True


def test_region_info(client):
    resp = client.get("/countries/Australia/regions/Victoria")
    assert resp.status_code == 200
    assert isinstance(resp.json, dict) == True


def test_regions(client):
    resp = client.get("/countries/Australia/regions")
    assert resp.status_code == 200
    assert isinstance(resp.json, dict) == True


def test_cities(client):
    resp = client.get("/countries/Australia/regions/Victoria/cities")
    assert resp.status_code == 200
    assert isinstance(resp.json, dict) == True


def test_city_info(client):
    resp = client.get("/countries/Australia/regions/Victoria/cities/Melbourne")
    assert resp.status_code == 200
    assert isinstance(resp.json, dict) == True
