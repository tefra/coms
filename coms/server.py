from fastapi import FastAPI

from coms.api import main
from coms.core import settings

app = FastAPI(
    debug=settings.debug,
    title=settings.title,
    description=settings.description,
    version=settings.version,
)


@app.on_event("startup")
def on_startup():
    pass


@app.on_event("shutdown")
def on_shutdown():
    pass


app.include_router(main.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "coms.server:app",
        host="0.0.0.0",
        reload=not settings.env.startswith("prod"),
        reload_dirs=["coms"],
    )
