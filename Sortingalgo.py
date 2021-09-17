import time
def bubble_sort (data , drawData, timee):
    for x in range (len (data) -1):
        for y in range (len (data) -1):
            if data [y] > data [y+1]:
                data[y], data[y+1] = data [y+1], data[y]
                drawData(data, ['green' if z == y or z == y+1 else 'red' for z in range (len(data))])
                time.sleep(timee)
    drawData (data, ['green' for x in range (len (data))])
##############################################################
def partition (data, head, tail, drawData, timee):
    border =  head
    pivot = data [tail]
    drawData (data, get_colorArr(len(data), head, tail, border, border, False))
    time.sleep(timee)
    for j in range (head, tail):
        if data [j] < pivot:
            drawData (data, get_colorArr(len(data), head, tail, border, j, True))
            time.sleep(timee)
            data[border], data [j] = data[j], data[border]
            border += 1
        drawData (data, get_colorArr(len(data), head, tail, border, j, False))
        time.sleep(timee)

    drawData (data, get_colorArr(len(data), head, tail, border, tail, True))
    time.sleep(timee)
    data [border], data [tail] = data[tail], data[border]
    return border 
def quick_sort (data, head, tail, drawData, timee):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timee)
        quick_sort (data, head, partitionIdx-1, drawData, timee)
        quick_sort (data, partitionIdx+1, tail, drawData, timee)
    
def get_colorArr(dataLen, head, tail, border, currIdx, isSwaping):
    colorArr = []
    for i in range (dataLen):
        if i >= head and i <= tail :
            colorArr.append ('gray')
        else :
            colorArr.append('white')
        if i == tail:
            colorArr[i]= 'blue'
        elif i == border :
            colorArr[i] = 'red'
        elif i == currIdx:
            colorArr[i] = 'yellow'
        if isSwaping:
            if i == border or i == currIdx:
                colorArr [i] = 'green'
    return colorArr