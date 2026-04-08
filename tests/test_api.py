def test_query():
    res = client.post("/ask", json={"query": "hello"})
    assert res.status_code == 200
