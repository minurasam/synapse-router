"""Tests for the health and readiness endpoints."""

from fastapi.testclient import TestClient

from synapse.main import create_app


def test_healthz_returns_ok():
    client = TestClient(create_app())
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readyz_returns_ready():
    client = TestClient(create_app())
    response = client.get("/readyz")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}
