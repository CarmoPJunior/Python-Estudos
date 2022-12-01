import asyncio
from desktop_notifier import DesktopNotifier

notify = DesktopNotifier()

async def main():
    n = await notify.send(title="Hello world!", message="Sent from Python")
    
    await asyncio.sleep(5)  # wait a bit before clearing notification

    await notify.clear(n)  # removes the notification
    await notify.clear_all()  # removes all notifications for this app

asyncio.run(main())
    
    # time.sleep(15) 