from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "***Drink Water Eat Food***",
            message = "Please drink water to be hydrated or eat something.",
            # app_icon = "3.ico",
            timeout = 5)
        time.sleep(30*60)

#to run file in background open file in cmd as
#pythonw Desktop notifier.py
# To close file end process from task manager