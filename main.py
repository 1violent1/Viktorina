print("Добро пожаловать в квиз по стартапам!😊")
print("Ответь на следующие вопросы:")
scores = 0
questions = ["1. Как называется компания, которая создается для развития новой идеи или инновационного продукта?", "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?", "3. Как называется капитал, который дают инвесторы на развитие стартапа?", "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?", "5. Какой план создают перед тем, как открывать стартап и занимать деньги?", "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?", "7. Как называется разница между выручкой и затратами компании?"]
answers = ["Стартап", "Инвестор", "Инвестиция", "MVP", "Бизнес-план", "Конкуренты", "Прибыль"]
print(questions[0])
user_answer = input("Введите ответ: ")
if answers[0].lower() == user_answer.lower():
  print("Правильно!")
  scores = scores + 1
else:
  print("Неправильно.")

print(questions[1])
user_answer = input("Введите ответ: ")
if answers[1].lower() == user_answer.lower():
  print("Правильно!")
  scores += 1
else:
  print("Неправильно.")

print(questions[2])
user_answer = input("Введите ответ: ")
if answers[2].lower() == user_answer.lower():
  print("Правильно!")
  scores += 1
else:
  print("Неправильно.")

print(questions[3])
user_answer = input("Введите ответ: ")
if answers[3].lower() == user_answer.lower():
  print("Правильно!")
  scores += 1
else:
  print("Неправильно.")

print(questions[4])
user_answer = input("Введите ответ: ")
if answers[4].lower() == user_answer.lower():
  print("Правильно!")
  scores += 1
else:
  print("Неправильно.")

print(questions[5])
user_answer = input("Введите ответ: ")
if answers[5].lower() == user_answer.lower():
  print("Правильно!")
  scores += 1
else:
  print("Неправильно.")

print(questions[6])
user_answer = input("Введите ответ: ")
if answers[6].lower() == user_answer.lower():
  print("Правильно!")
  scores += 1
else:
  print("Неправильно.")
if scores == 1:
  print("Ты набрал",scores,"очко!")
elif scores >=2 and scores <5:
  print("Ты набрал",scores,"очка!")
else:
  print("Ты набрал",scores,"очков!")