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
        print("Потрачено времени на выполнение кода", self.result, "\n")

with Manager():
    cook_book = {
  "салат":  
      [
        ["картофель", 100],
        ["морковь", 50],
        ["огурцы", 50],
        ["горошек", 30],
        ["майонез", 70],
      ],
  "пицца":  
      [
        ["сыр", 50],
        ["томаты", 50],
        ["тесто", 100],
        ["бекон", 30],
        ["колбаса", 30],  
      ],
  "фруктовый десерт":
      [
        ["хурма", 60],
        ["киви", 60],
        ["творог", 60],
        ["сахар", 10],
        ["мед", 50],  
      ]
}

person = 3

print("Приготовить блюда на", person, "персоны", "\n")
for meal, ingredient in cook_book.items():
  print("\n Для блюда", meal, "требуются ингредиенты:")
  for ing in ingredient:
    print(ing[0], " - ", ing[1]*person, "грамм")
