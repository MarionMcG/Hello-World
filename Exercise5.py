# Marion McGowan 03/03/2018
# Write a Python script that reads the Iris data set in and 
# prints the four numerical values on each # row in a nice format. 
# Decimal points aligned and spaces between columns.


with open ("data/iris-data.csv") as f:
    for line in f:
        print('{} '' {} '' {} '' {}'.format(line.split(',')[0], 
        line.split(',')[1], line.split(',')[2], line.split(',')[3]))

# I'm not sure if I did this right, as the decimal points automatically aligned.
# Hope this is what you were looking for. 
# It seemed too easy, so I think I missed something.