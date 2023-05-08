class Maths:
    def divide(self, x , y):
        if x == 0:
            raise ValueError("Zero can not be divided")
        return x / y

    def multiply(self, x , y):
        return x * y

    def add(self, x , y):
        return x + y

    def subtract(self,x , y):
        return x - y

    def power(self, x, y):
        return x ** y


class Physics:
    def force(self, mass, acceleration):
        return mass * acceleration

    def work(self, force, distance):
        return force * distance

    def acceleration(self, initial_velocity, final_velocity, time):
        return  (final_velocity - initial_velocity) / time

    def velocity(self, distance, time):
        return distance / time

    def power(self, work, time):
        return work / time

# ask the user to pick a class and operation they want to perform

print("Which class do You wish to use?")
print("1. Maths")
print("2. Physics")

class_select_choice = int(input("Input choice (1 or 2): \n") )

if class_select_choice == 1:
    my_class = Maths()

elif class_select_choice == 2:
    my_class = Physics()

else:
    print("Not a valid class choice")
    exit()

print("Which operation do You wish to perform")
print("1. maths operation")
print("2. Physics operation")

select_operation = int(input("Input operation (1 or 2): \n"))
if select_operation == 1:
    my_class = Maths()
elif select_operation == 2:
    my_class = Physics()
else:
    print("not valid")

print("1. Divide")
print("2. Multiply")
print("3. Add")
print("4. Subtract")
print("5. Power")

operation_choice = int(input("Input preferred choice (1-5): \n"))


# Ask the user for input values

x = float(input("input first value: "))
y = float(input("input second value: "))

# Call the right method and display the answer

if operation_choice == 1:
    answer = my_class.divide(x, y)

elif operation_choice == 2:
    answer = my_class.multiply(x, y)

elif operation_choice == 3:
    answer = my_class.add(x, y)

elif operation_choice == 4:
    answer = my_class.subtract(x, y)

elif operation_choice == 5:
    answer = my_class.power(x, y)

else:
    print("Not a valid choice")
    exit()

print("The answer is:", answer)







