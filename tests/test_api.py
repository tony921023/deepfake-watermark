import io
from app import create_app

def test_health_ok():
    app = create_app()
    client = app.test_client()
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.get_json()['status'] == 'ok'

def test_embed_stub():
    app = create_app()
    client = app.test_client()
    data = {'file': (io.BytesIO(b'fakeimg'), 'x.png')}
    resp = client.post('/api/embed', data=data, content_type='multipart/form-data')
    assert resp.status_code == 200
    assert resp.get_json()['ok'] is True
