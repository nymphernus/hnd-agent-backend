from fastapi import FastAPI, HTTPException, Response, Depends
import uvicorn
from authx import AuthX, AuthXConfig
from pydantic import BaseModel

app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY" # Никто не должен знать, желательно убрать в .env
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)


class UserLoginSchema(BaseModel):
    username: str
    password: str

@app.post("/login", tags=['Аутентификация'], summary="Вход")
def login(creds: UserLoginSchema, response: Response):
    if creds.username == "test" and creds.password == "test":
        token = security.create_access_token(uid="12345")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Incorrecr username or password")

@app.get("/protected", tags=['Аутентификация'], summary="Проверка", dependencies=[Depends(security.access_token_required)])
def protected():

    return {"data": "secret"}
















if __name__ == "__main__":
    uvicorn.run("auth:app", reload=True)