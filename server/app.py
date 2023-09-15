from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from server.routes.event_route import event_router
from server.scheduler import job

app = FastAPI()

app.include_router(event_router, tags=["Event"], prefix="/event")

@app.get("/")
async def root():
    return {"message": "Mohang API"}


@app.on_event('startup')
async def startup():
    scheduler = BackgroundScheduler(demon=True, timezone='Asia/Seoul')
    scheduler.add_job(job, 'cron', hour="17", minute="26", second="0")
    scheduler.start()