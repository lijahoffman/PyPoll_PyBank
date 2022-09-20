import os
import csv
# Dependencies imported. 


month = []
change = []
profit_loss = []
# Empty lists created for use in later code. 



py_bank_csv = os.path.join("Resources", "budget_data.csv")
# CSV filepath created. 

with open(py_bank_csv) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader, None)
    # Opening and reading csv file. Header row skipped. 

    for row in csv_reader:
        split_date = row[0].split("/")
        month.append(split_date[0])
        profit_loss.append(int(row[1]))
    # For loop using csv to populate list month with the month extracted from each entry in date column and list profit_loss with value extracted from entry in profit/loss column. 


net = 0 
# Variable created for use in below code. 
for i in profit_loss: 
    net = net + i
# For loop adding together all elements in list  profit_loss and storing as variable net. 


for i in range(1,len(profit_loss)): 
    diff = profit_loss[i] - profit_loss[(i- 1)]
    change.append(diff)
# For loop used to populate list change with the difference between all values in profit_loss (starting with the second value).
    

change_sum = 0 
# Variable created for use in below code. 
for i in change: 
    change_sum = change_sum + i 
# For loop adding together all elements in list change and storing as variable change_sum. 



increase = max(change)
increase_index = change.index(increase)
increase_month = month[increase_index + 1]
# Greatest profit and associated month stored as variables. 

decrease = min(change)
decrease_index = change.index(decrease)
decrease_month = month[decrease_index + 1]
# Greatest loss and associated month stored as variables. 



total_months = len(month)
# Total_months variable defined as the number of elements in list month. 
average_change = round(float(sum(change) / len(change)), 2)
# Average_change defined as the sum of list change divided by the length of list change, rounded to two decimal points. 


output_path = os.path.join("Analysis", "financial_analysis.txt")
# Output path created to store text file in analysis folder. 
financial_analysis = open(output_path,"w")
# Text file created and opened for writing. 

financial_analysis.write("Financial Analysis" + "\n")
financial_analysis.write("--------------------" + "\n")
financial_analysis.write("Total Months: " + str(total_months) + "\n")
financial_analysis.write("Total: $" + str(net) + "\n")
financial_analysis.write("Average Change: $" + str(average_change) + "\n")
financial_analysis.write("Greatest Increase in Profits: " + str(increase_month) + " ($" + str(increase) + ")" + "\n")
financial_analysis.write("Greatest Decrease in Profits: " + str(decrease_month) + " ($" + str(decrease) + ")" + "\n")
# Text file populated. 

financial_analysis.close()
# Text file closed. 

print("Financial Analysis")
print("--------------------")
print("Total Months: ", total_months)
print("Total: $", net)
print("Average Change: $", average_change)
print("Greatest Increase in Profits: ", increase_month, " ($", increase, ")")
print("Greatest Decrease in Profits: ", decrease_month, " ($", decrease, ")")
# Results printed to terminal. 



    
