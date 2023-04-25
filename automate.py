import pandas as pd
import sys

df = pd.read_excel('display.xlsx')

counter = 0


while True: 

    
    assignments = []
    assignment = input("Assignment: ")


    dates = []
    date = input("Due Date: ")

    classes = []
    className = input ("Class: ")

    if assignment != "done" :
        assignments.append(assignment)
        dates.append(date)
        classes.append(className)

        data = {'Assignments': assignments, 'Due Dates': dates, 'Class': classes}

        new_row = pd.Series(data, index=df.columns)

        df = df._append(new_row, ignore_index=True)


        writer = pd.ExcelWriter('display.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=True)
        writer._save()
        print("Done.")
        counter = counter + 1
    else: 
        sys.exit()
