#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

print(admin_login("sudo", "12345"))    # Output: "Access denied"
print(admin_login("admin", "12345"))   # Output: "Access granted"
print(admin_login("ADMIN", "12345"))   # Output: "Access granted"


def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

print(hows_the_weather(33))   # Output: "It's brisk out there!"
print(hows_the_weather(99))   # Output: "It's too dang hot out there!"
print(hows_the_weather(75))   # Output: "It's perfect out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

print(fizzbuzz(1))   # Output: 1
print(fizzbuzz(2))   # Output: 2
print(fizzbuzz(3))   # Output: Fizz
print(fizzbuzz(4))   # Output: 4
print(fizzbuzz(5))   # Output: Buzz
print(fizzbuzz(15))  # Output: FizzBuzz


def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None

print(calculator("+", 1, 1))   # Output: 2
print(calculator("-", 3, 1))   # Output: 2
print(calculator("*", 3, 2))   # Output: 6
print(calculator("/", 4, 2))   # Output: 2
print(calculator("nope", 4, 2))  # Output: "Invalid operation!" and None
