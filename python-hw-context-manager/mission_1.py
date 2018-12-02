from datetime import datetime
import time

class Manager:
    def __enter__(self):
        launch_code = datetime.now().time()
        print("Время запуска кода в менеджере контекста: ", launch_code)
        self.start = datetime.now()
        return self
        
    def __exit__(self, type, value, traceback):
        completion_code = datetime.now().time()
        print("Время окончания работы кода: ", completion_code)
        self.end = datetime.now()
        self.result = self.end - self.start
        print("Потрачено времени на выполнение кода", self.result)

with Manager():
    print("Тест программы")
