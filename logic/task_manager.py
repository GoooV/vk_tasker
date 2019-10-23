import time

from datetime import datetime

class Task:
    def __init__(self, hours: int, minutes: int):
        self.minutes = hours * 60 + minutes
    
    def is_time(self):
        now = datetime.now()        
        return (now.hour * 60 + now.minute) == self.minutes

    def run(self):
        raise NotImplementedError()


class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def append_task(self, task):
        self.tasks.append(task)

    def main_loop(self):
        while True:
            print('[{}] checket time'.format(datetime.now()))
            for task in self.tasks:
                if task.is_time():
                    task.run()
            time.sleep(60)

    
    def run(self):
        print('=== Run main loop ===')
        self.main_loop()