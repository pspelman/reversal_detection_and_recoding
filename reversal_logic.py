# declare the data


def reversal_count(data):

    count = 0
    locations = []

    # loop through the array
    for i in range(0, len(data)-1):
        if(data[i+1] > data[i]):
            print "there is a reversal at ", i+1
            count += 1
            locations.append(i+1)

    result_key = {
        'count': count,
        'locations': locations
    }

    return result_key


def recode_data(data):
    reversal_data = reversal_count(data)


    #todo: start the loop at the first reversal point
    # reversal_point = reversal_data.pop()
    count = 0
    while len(reversal_data['locations']) > 0:
        print " reversal locations: ", reversal_data['locations']
        reversal_data = reversal_count(data)

        print "popping...location: ", reversal_data['locations'][len(reversal_data['locations'])-1]
        i = reversal_data['locations'].pop()

        reference_value = data[i]
        while i >= 0 and data[i-1] < reference_value:
            print "reassigning"
            data[i-1] = reference_value
            i -= 1

        print "current data: ", data

    return data

data4 = [0, 7, 0, 2, 3, 4, 0]

# print "data1"
# reversal_count(data1)
# print "data2"
# reversal_count(data2)
# print "data3"
# reversal_count(data3)
print "data4"
result = reversal_count(data4)
# recode_data(data4)

new_data = recode_data(data4)
print "new data: ", new_data

