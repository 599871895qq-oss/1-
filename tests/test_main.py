from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_health():
    res = client.get('/health')
    assert res.status_code == 200
    assert res.json()['status'] == 'ok'


def test_materials_ranked():
    res = client.get('/materials')
    assert res.status_code == 200
    data = res.json()
    assert len(data) >= 1
    assert data[0]['hot_score'] >= data[-1]['hot_score']


def test_materials_filter():
    res = client.get('/materials', params={'category': '美妆'})
    assert res.status_code == 200
    data = res.json()
    assert all(item['category'] == '美妆' for item in data)
