def filter_list(inputList):
    filterList = []
    for obj in inputList:
        if type(obj) != str:
            filterList.append(obj)
    return filterList


def first_non_repeating_letter(inputText):
    counter = dict()
    for el in inputText:
        lowerChar = el.lower()
        if lowerChar in counter:
            counter[lowerChar] += 1
        else:
            counter[lowerChar] = 1
    for el in inputText:
        lowerChar = el.lower()
        if counter[lowerChar] == 1:
            return el
    return None


def digital_root(number):
    totalSum = 0
    while number > 0:
        totalSum += number % 10
        number = number // 10
    if totalSum // 10 > 0:
        totalSum = digital_root(totalSum)
    return totalSum


def number_of_pairs(array, pairSum):
    counter = 0
    storage = set()
    for el in array:
        if pairSum - el in storage:
            counter += 1
        storage.add(el)
    return counter


def meeting(friends):
    storage = []
    guestList = friends.replace(':', ' ').split(sep=';')
    for human in guestList:
        name, surname = human.split()
        storage.append((surname.upper(), name.upper()))
    sortedList = sorted(storage, key=lambda x: (x[0], x[1]))
    final = ' '
    for human in sortedList:
        final += f"({human[0]}, {human[1]}) "
    return final


def next_biggest(number):
    fixIter = -1
    listStorage = list(str(number))
    i = len(listStorage)-1
    while i > 0:
        if int(listStorage[i]) <= int(listStorage[i-1]):
            i -= 1
        else:
            fixIter = i-1
            break
    if fixIter == -1:
        return -1
    for i in range(len(listStorage)-1, 0, -1):
        if listStorage[i] > listStorage[fixIter]:
            listStorage[i], listStorage[fixIter] = listStorage[fixIter], listStorage[i]
            listStorage[fixIter+1:] = reversed(listStorage[fixIter+1:])
            return ''.join(listStorage)


def unsigned_converter(numberUnsigned):
    binary = '{:032b}'.format(numberUnsigned)
    octets = [str(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    return '.'.join(octets)


if __name__ == '__main__':
    # Task1
    inputList = [1, 2, 'aasf', '1', '123', 123]
    print(f"Filtered list : {filter_list(inputList=inputList)}")

    # Task2
    text = 'sTtrrEeSS'
    print(f"First non-repeating letter : {first_non_repeating_letter(inputText=text)}")

    # Task3
    number = 493193
    print(f"Digital root : {digital_root(number=number)}")

    # Task4
    array = [1, 3, 6, 2, 2, 0, 4, 5]
    pairSum = 5
    print(f"Number of pairs in the array : {number_of_pairs(array=array, pairSum=pairSum)}")

    # Task5
    friends = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull; Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    print(f"Ordered friends : {meeting(friends=friends)}")

    # Extra task 1
    number = 28731
    print(f"Next bigger : {next_biggest(number=number)}")

    # Extra task 2
    numberUnsigned = 2149583361
    print(f"{numberUnsigned} => {unsigned_converter(numberUnsigned=numberUnsigned)}")
