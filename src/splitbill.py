"""
Splitbill

A simple module to fairly split bills among a group of people based on what each person consumed.
Includes proportional tax and tip distribution.
"""
import csv
import datetime as dt

def splitbill():
    """
    Splitbill function
    """
    print("***  Welcome to Split-Bill !!  ***")
    n = int(input("Enter number of people: "))
    group = []
    comment = "\n"
    for i in range(1, n + 1):
        name = input("Enter name of person " + str(i) + ": ")
        group.append(name)
        comment = comment + str(i) + "=" + name + ", "
    comment = comment[0:-2]

    rows = []
    places_count = int(input("\nEnter the number of places you visited today: "))
    if places_count > 1:
        total_table = [["Final Bill"] + group + ["Total"]]  # Try /b for bold
        last_row_total_table = [0] * n
    for k in range(places_count):
        if places_count == 1:
            place = input("\nEnter the name of place: ")
        else:
            place = input("\nEnter the name of place " + str(k + 1) + ": ")
        first_row = [place] + group + ['Total']
        rows.append(first_row)
        items = []
        prices = []
        total = [0] * n

        flag = 1
        while flag:
            new_item = input("\nEnter Item " + str(flag) + " Name: ")
            items.append(new_item)
            amount = float(input("Enter total amount spent on " + new_item + ": "))
            prices.append(amount)
            more = input("Are there more items to add?[Y/n]: ")
            if more == "" or more[0] == 'y' or more[0] == 'Y':
                flag += 1
            else:
                flag = 0

        size = len(items)
        for z in range(size):
            new_row = [items[z]] + [0] * n
            print(comment)
            vals = input("Enter assigned number of people to split for " +
                        items[z] + " seperated by comma: ")
            vals = vals.split(",")
            m = len(vals)
            equal_flag = 'y'
            if m != 1:
                equal_flag = input("Do you want to split the bill among " +
                                str(m) + " members equally?[y/n]: ")
            if equal_flag[0] == 'N' or equal_flag[0] == 'n':
                # unequal_splits = []  # What if it does not equal to 100
                for i in vals:
                    split_perc = float(input("Enter the split percentage for "
                                            + group[int(i) - 1] + ": "))
                    rate = float(prices[z]) * (split_perc / 100)
                    total[int(i) - 1] += rate
                    new_row[int(i)] += rate
            else:
                rate = float(prices[z]) / m
                for j in vals:
                    total[int(j) - 1] += rate
                    new_row[int(j)] += rate
            new_row.append(prices[z])
            rows.append(new_row)
            print(total)

        last_row = ["Total"] + total + [sum(total)]
        print("\nFinal Totals of ", place, ":")
        for i in range(len(total)):
            print(group[i], "=", round(total[i], 2))

        print("\nTotal Bill of ", place, " = ", sum(total))
        rows.append(last_row)
        rows.append([])
        if places_count > 1:
            total_row = [place] + total + [sum(total)]
            total_table.append(total_row)
            for j in range(len(last_row_total_table)):
                last_row_total_table[j] += round(total[j], 2)

    if places_count > 1:
        print("\nTotal Bill: ", sum(last_row_total_table))
        last_row_total_table = ["Total"] + last_row_total_table + [sum(last_row_total_table)]
        total_table.append(last_row_total_table)
        rows += total_table

    time_script_run = dt.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    filename = f"{time_script_run}_bill.csv"

    with open(filename, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

splitbill()
