from fastapi import FastAPI
from enum import Enum
app = FastAPI()

#Fix params to be consistent with the rest of the code. So place them in the start.
@app.get("/users/me")
def read_user_me():
    return { "user_id": "the current user" }


@app.get("/users/{user_id}")
def read_user(user_id : str):
    return {"user_id": user_id}

#path cannot be redefined. So remove the duplicate path.

#If the Enum is not used in the path, then the class Item cannot be iterated and thus cannot be used as path parameter.
class ModelName(str, Enum):
    model1 = "model1"
    model2 = "model2"
    model3 = "model3"


@app.get("/models/{model_name}")
def read_model(model_name: ModelName):
    if model_name is ModelName.model1:
        return {"model_name": model_name, "message": "Model 1 selected"}
    if model_name == ModelName.model2:
        return {"model_name": model_name, "message": "Model 2 selected"}
    # if model_name == ModelName.model3:
    #     return {"model_name": model_name, "message": "Model 3 selected"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

#return a path inside a path.
#The path can be: /files//home/users1/file.txt(return path is: /home/users1/file.txt)
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}