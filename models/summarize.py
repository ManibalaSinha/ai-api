from typing import Optional
from fastapi import Form
# 📄 Summarization from text input
class TextInput(BaseModel):
    text: str
@app.post("/summarize-text")
async def summarize_text_input(input: TextInput):
    try:
        summary = summarizer(input.text[:1024])[0]["summary_text"]
        return {"summary": summary}
    except Exception as e:
        return {"error": f"Summarization failed: {str(e)}"}
    
@app.post("/summarize")
async def summarize_input(
    file: Optional[UploadFile] = File(None),
    text: Optional[str] = Form(None)
):
    try:
        if file:
            contents = await file.read()
            # Detect encoding to handle binary/text properly
            import chardet
            encoding = chardet.detect(contents)['encoding']
            text = contents.decode(encoding or "utf-8")

        if not text:
            raise HTTPException(status_code=400, detail="No text or file provided for summarization.")

        summary = summarizer(text[:1024])[0]["summary_text"]
        return {"summary": summary}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Summarization failed: {str(e)}"})
