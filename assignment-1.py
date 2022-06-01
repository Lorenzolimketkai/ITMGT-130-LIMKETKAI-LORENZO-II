def classify_grade(number_grade):
    if number_grade >=92:
        return('"A"')
    elif number_grade >=86 and number_grade <92:
        return('"B+"')
    elif number_grade >=80 and number_grade <86:
        return('"B"')
    elif number_grade >=74 and number_grade <80:
        return('"C+"')
    elif number_grade >=67 and number_grade <74:
        return('"C"')
    elif number_grade >=60 and number_grade <67:
        return('"D"')
    elif number_grade <60:
        return('"F"')
      
      
number_grade = int(input())
classify_grade(number_grade)
print("The letter grade equivalent of the number grade is",classify_grade(number_grade))









def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    total_bag_1 = item_quantity_1*item_weight_1
    total_bag_2 = item_quantity_2*item_weight_2
    average_weight = float((total_bag_1 + total_bag_2)/2)
    return average_weight
  
  
item_quantity_1 = int(input("Input the quantity of items in the first bag."))
item_weight_1 = float(input("Input the weight of each individual item in the first bag."))
item_quantity_2 = int(input("Input the quantity of items in the second bag."))
item_weight_2 = float(input("Input the weight of each individual item in the second bag."))

average_weight = average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2)

print("The weighted average weight of one item in this purchase is", average_weight)










import math
def distance(x_1, y_1, x_2, y_2):
    difference_between_x = abs(x_1 - x_2)
    difference_between_y = abs(y_1 - y_2)
    sum_of_differences = difference_between_x + difference_between_y
    distance_between = math.sqrt(sum_of_differences)
    return distance_between
  
  
x_1 = float(input("Input the first x-coordinate. ="))
y_1 = float(input("Input the first y-coordinate. ="))
x_2 = float(input("Input the second x-coordinate. ="))
y_2 = float(input("Input the second y-coordinate. ="))

distance_between = distance(x_1, y_1, x_2, y_2)

print("The distance between the two coordinates is", distance_between)






