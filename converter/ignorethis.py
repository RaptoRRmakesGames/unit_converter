import sqlite3
import json
import os

try:
    
    with open("foods.json", "r") as file:
        file.close()
        os.rename("foods.json", "foods.txt")
        print("Test 1 pass")
        
    with open("foods.txt", "w") as file:
        if len(file.read()) < 1:
            file.write("{}")
        file.close()
        os.rename("foods.txt", "foods.json")
        print("Test 2 pass")
        
    with open("foods.json", "r") as file:
        foods = json.load(file)
        print("Test 3 pass")


except FileNotFoundError:
    with open("foods.json", "w") as file:
        foods = {}
        print("File Created for the First time")

foodname = input("Give food name: ")

foods[foodname] = {
    "kg":      float(input("Enter in kg:")),
    "liter":   float(input("Enter in liters:")),
    "grams":   float(input("Enter in grams:")),
    "cups":    float(input("Enter in cups:")),
    "pieces":  float(input("Enter in pieces:")),
    "tbsp":    float(input("Enter in tbsp:")),
    "tsp":     float(input("Enter in tsp:")),
}

with open("foods.json", "w") as file:
    json.dump(foods, file)
    file.write("\n")
