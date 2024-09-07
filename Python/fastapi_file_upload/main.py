import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(f"./data/{file.filename}","wb") as fp:
        shutil.copyfileobj(file.file,fp)
    return {"filename": file.filename}

@app.get("/downloadfile/")
async def download_file(filename: str):
    response = FileResponse(
                            path=f"./data/{filename}",
                            filename=filename
                            )
 
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)