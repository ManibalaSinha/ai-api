def test_rag():
    from app.services.rag_service import rag_pipeline
    response = rag_pipeline("What is Python?")
    assert "Python" in response
