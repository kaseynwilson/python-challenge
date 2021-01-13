# Import the os module to allow us to create file paths across operating systems
import os
#Module for reading CSV Files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as budget_handler:
    csvreader = csv.reader(budget_handler, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(csv_header)
    
    
    #create lists and dictionaries to hold values. 
    count = 0 
    profit_losses = 0.0
    profit_list = []
    net_change_list = []
    #change_profit_loss = 0.0
    change_profit_loss = next(csvreader[1])
    net_change_profit_loss = 0.0
    dict_month_profit_loss = {}

    for row in csvreader:    
        #Count the rows
        count = count + 1
        #track total amount profit losses 
        profit_losses = float(profit_losses) + float(row[1])
        #Add each profit (or loss) to a list
        profit_list.append(int(row[1]))
        #subtract the amount of the previous profit/loss row from current row
        net_change_profit_loss = float(row[1]) - change_profit_loss
        #Add the value of the change in profit/loss to a list
        net_change_list.append(net_change_profit_loss)
        #reset the profit/loss counter to the current row's value
        change_profit_loss = float(row[1])
        #Add the profit/loss and associated month to a dictionary
        dict_month_profit_loss[net_change_profit_loss] = row[0]

    average_net_change = sum(net_change_list)/(len(net_change_list))
   
    max_profit = 0.0
    max_losses = 0.0
    new_total_profit_loss = 0.0
    

    #Go through list to find max and min value of profit/loss
    for i in range(len(net_change_list)):
        if i == 0:
            continue
        if net_change_list[i] >= max_profit:
            max_profit = net_change_list[i]
        if net_change_list[i] <= max_losses:
            max_losses = net_change_list[i]
    

    #Print all results
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: " + str(count))
    print("Total: $" + str(profit_losses))
    print("Average Change: $" + str(average_net_change))
    print("Greatest Increase in Profits: " + str(dict_month_profit_loss[max_profit]) + " $ " + str(max_profit))
    print("Greatest Decrease in Profits: " + str(dict_month_profit_loss[max_losses]) + " $ " + str(max_losses))


    #output path for writing to text file.
    analysis_file = os.path.join("Analysis", "analysis.txt")
    
    with open(analysis_file, "w") as txt:
        txt.write("Financial Analysis\n")
        txt.write("-------------------------------\n")
        txt.write(f"Total Months:  {count}\n")
        txt.write(f"Total: $ + {profit_losses}\n")
        txt.write(f"Average Change: $ {average_net_change}\n")
        txt.write(f"Greatest Increase in Profits:  {dict_month_profit_loss[max_profit]} $ {max_profit}\n")
        txt.write(f"Greatest Decrease in Profits:  {dict_month_profit_loss[max_losses]} $ {max_losses}")