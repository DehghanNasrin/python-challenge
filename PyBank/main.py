import os
import csv

def calculate_financial_analysis():

    csvPath = os.path.join('Resources', 'budget_data.csv')
    total_month_count = 0
    total = 0
    average_change = 0
    greatest_increase_in_profits = 0
    greatest_decrease_in_losses = 0
    greatest_increase_profits_date = ''
    greatest_decrease_losses_date = ''
    diff_sum = 0
    previous_row_value = 0
    total_diff_sum = 0
    with open(csvPath) as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')

        next(csvReader)
        for row in csvReader:
            total_month_count += 1
            total += int(row[1])

            if previous_row_value == 0:
                previous_row_value = int(row[1])
                diff_sum = previous_row_value
            else:
                diff_sum = int(row[1]) - previous_row_value
                total_diff_sum += diff_sum
                previous_row_value = int(row[1])

            if diff_sum > 0:
                if diff_sum > greatest_increase_in_profits:
                    greatest_increase_in_profits = diff_sum
                    greatest_increase_profits_date = row[0]

            if diff_sum < 0:
                if diff_sum < greatest_decrease_in_losses:
                    greatest_decrease_in_losses = diff_sum
                    greatest_decrease_losses_date = row[0]

        average_change = float(total_diff_sum) / float(total_month_count - 1)

    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {total_month_count}')
    print(f'Total: ${abs(total)}')
    print('Average  Change:', float('{:.2f}'.format(average_change)))
    print(f'Greatest Increase in Profits: {greatest_increase_profits_date} (${greatest_increase_in_profits})')
    print(f'Greatest Decrease in Losses: {greatest_decrease_losses_date} (${greatest_decrease_in_losses})')

    csvwriter = open('analysis\\analysis.txt', 'w')
    print('Financial Analysis', file=csvwriter)
    print('----------------------------', file=csvwriter)
    print(f'Total Months: {total_month_count}', file=csvwriter)
    print(f'Total: ${abs(total)}', file=csvwriter)
    print('Average  Change:', float('{:.2f}'.format(average_change)), file=csvwriter)
    print(f'Greatest Increase in Profits: {greatest_increase_profits_date} (${greatest_increase_in_profits})', file=csvwriter)
    print(f'Greatest Decrease in Losses: {greatest_decrease_losses_date} (${greatest_decrease_in_losses})', file=csvwriter)



calculate_financial_analysis()
