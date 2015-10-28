__author__ = 'Quintin Martinus'


# creates the function cheese_and_crackers and gives it two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# runs the function with new values for its arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# assigns value to the arguments by using them as variables
print "OR, we can use variables from out script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# assign values to the function with math
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# combination of adding value to the function by using variables and math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


