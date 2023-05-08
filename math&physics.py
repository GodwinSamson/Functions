class Maths:
    def divide(self,x,y):
        if y == 0:
            raise ValueError("cannot divide by 0")
        return x/y

    def multiply(self,x,y):
        return x*y
    def add(self,x,y):
        return x+y
    def subtract(self,x,y):
        return x-y
    def power(self,x,y):
        return x**y


class Physics:
    def force(self,mass,accelaration):
        return mass * accelaration
    def work(self,force,distance):
        return force * distance
    def accelaration(self,initial_velocity,final_velocity,time):
        return initial_velocity-final_velocity/time
    def velocity(self,ditance,time):
        return ditance/ time
    def power(self,work,time):
        return work/time
#ask user to choose a class and operation
print("which class do you want to use")
print("1 maths")
print("2 physics")

class_select_choice = int(input("input choice(1 or 2):"))
if class_select_choice == 1
    my_class = Maths()

elif class_select_choice == 2:
    my_class = physics()

else:
    print("not a valid class_choice")
    exit()
    print("which operation do you wish to perform")
    print("1 divide")
    print("2 multiply")
    print("3 add")
    print("4 subtract")
    print("5 power")

operation_choice = int(input("input prefared choice (1-5):"))
# ask user for prefarred values
x= float(input("input first value:"))
y = float(input("input second value:"))

# call right method and display answer
if operation_choice == 1:
    answer = my_class.divide(x,y)
elif operation_choice == 2:
    answer = my_class.multiply(x,y)
elif operation_choice == 3:
    answer = my_class.add(x,y)
elif operation_choice == 4:
    answer = my_class.subtract(x,y)
elif operation_choice == 5:
    answer = my_class.power(x,y)
else:
    print("not a valid choice")
    exit()
    print("answer is , answer")







