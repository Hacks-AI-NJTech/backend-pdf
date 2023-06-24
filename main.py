import uvicorn
from fastapi import  APIRouter, FastAPI, File, UploadFile, Request
from os import getcwd
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
import os
from os import listdir
from os.path import isfile, join
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


router = APIRouter(
    prefix="",
    tags=["/apisite"]
)

@app.get('/')
async def main(request: Request):
    content_type = request.headers.get('Content-Type')
    
    if content_type is None:
        return 'No Content-Type provided.'
    elif content_type == 'application/json':
        try:
            json = await request.json()
            return json
        except Error:
            return 'Invalid JSON data.'
    else:
        return 'Content-Type not supported.'
@app.get("/pdf")
async def upload_file1(file: UploadFile = File(...)):
    with open(file.filename, 'wb') as image:
        content = await file.read()
        image.write(content)
        image.close()
    return JSONResponse(content={"filename": file.filename},status_code=200)
@app.post("/pdf")
async def upload_file2(file: UploadFile = File(...)):
    with open(file.filename, 'wb') as image:
        content = await file.read()
        image.write(content)
        image.close()
    return JSONResponse(content={"filename": file.filename},status_code=200)
@app.put("/pdf")
async def upload_file3(file: UploadFile = File(...)):
    with open(file.filename, 'wb') as image:
        content = await file.read()
        image.write(content)
        image.close()
    return JSONResponse(content={"filename": file.filename},status_code=200)  
@app.patch("/pdf")
async def upload_file4(file: UploadFile = File(...)):
    with open(file.filename, 'wb') as image:
        content = await file.read()
        image.write(content)
        image.close()
    return JSONResponse(content={"filename": file.filename},status_code=200)
@app.get("/download/{name_file}")
def download_file(name_file: str):
    return FileResponse(path=getcwd() + "/" + name_file, media_type='application/octet-stream', filename=name_file)

@app.get("/state")
def get_file():
    cwd = os.getcwd()
    files = [{'FileName':os.path.join(cwd, f),'Status':'Status','Download':'Download'} for f in os.listdir(cwd) if 
    os.path.isfile(os.path.join(cwd, f))]
    return JSONResponse(content={'files':files},status_code=200)


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)