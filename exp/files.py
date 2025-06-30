from fastapi import FastAPI, File, UploadFile
import uvicorn
from fastapi.responses import StreamingResponse,FileResponse

app = FastAPI()

@app.post("/files", tags=['Файлы'])
async def upload_file(uploaded_file: UploadFile):
    file = uploaded_file.file
    filename = uploaded_file.filename
    size = uploaded_file.size
    with open(f"1_{filename}", "wb") as f:
        f.write(file.read())

@app.post("/multi_files", tags=['Файлы'])
async def upload_files(uploaded_files: list[UploadFile]):
    for uploaded_file in uploaded_files:
        file = uploaded_file.file
        filename = uploaded_file.filename
        size = uploaded_file.size
        with open(f"1_{filename}", "wb") as f:
            f.write(file.read())

@app.get("/get_file/{filename}",tags=["Файлы"])
async def get_file(filename: str):
    return FileResponse(filename)


def iterfile(filename: str):
    with open(filename, "rb") as file:
        while chunk := file.read(1024 * 1024):
            yield chunk


@app.get("/get_file/streaming/{filename}",tags=["Файлы"])
async def get_streaming_file(filename: str):
    return StreamingResponse(iterfile(filename), media_type="audio/mpeg")




if __name__ == "__main__":
    uvicorn.run("files:app", reload=True)