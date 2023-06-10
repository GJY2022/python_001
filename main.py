# def average():
#     total = 0
#     count = 0
#     user_input = input("求平均数，退出为q\n")
#     while user_input != "q":
#         num = float(user_input)
#         total += num
#         count += 1
#         user_input = input("求平均数，退出为q\n")
#     if count == 0:
#         result = 0
#     else:
#         result = total / count
#     print("平均数为：" + str(result))
#     return result

class CurCat:
    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

    def speak(self):
        print("miao" * self.age)

    def think(self, content):
        print(f"cat{self.name}and{content}")


cat1 = CurCat("JOJO", 2, "orange")
print(cat1.name)
