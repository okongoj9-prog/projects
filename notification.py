# pip install plyer

from plyer import  notification

notification.notify (title="Hello",
                    message="This is from python",
                    timeout = 10)
print("Notification sent succesfully")