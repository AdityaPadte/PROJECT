import time
from plyer import notification


if __name__=="__main__":
    while   True:
        notification.notify(
            title="Go take a small walk!!!",
            message='''increased cardiovascular and pulmonary (heart and lung) fitness. reduced risk of heart disease and stroke. improved management of conditions such as hypertension (high blood pressure), high cholesterol, joint and muscular pain or stiffness, and diabetes.''',
            app_icon=r"C:\Users\HP\Desktop\Python\Project\walk.ico",
            timeout=20
        )
        time.sleep(60*6)