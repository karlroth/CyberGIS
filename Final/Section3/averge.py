
if __name__ != '__lib__':
    def outputSchema(empty):
        return lambda x: x



@outputSchema("fromAverage:double")
def getAverage(cpm):
    cpmList = []
    #extract cpm values
    for record in cpm:
        cpmList.append(record[0])

    #calculate inner fences and outer fences
    #inner_fences, outer_fences = getOutlierRanges(cpmList)

    inputSum = 0.0
    i = 0.0
    #sum up cpm
    for record in cpm:
        inputSum += record[0]
        i = i + 1
    if i == 0:
        return 0;
    else:
        return inputSum/i

