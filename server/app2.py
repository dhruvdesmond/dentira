import uvicorn
from fastapi import FastAPI

from controller import search_controller


app = FastAPI()
app.include_router(search_controller.search_router)




# register event handlers here
@app.on_event("startup")
async def startup_event():
    print("Startup Event Triggered")


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutdown Event Triggered")


if __name__ == "__main__":
    uvicorn.run("app2:app", host="127.0.0.1", port=9999, reload=True)