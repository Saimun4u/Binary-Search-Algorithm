# a function that takes a list and target parameter
# variable assignment: start, middle, end, steps
# use recursion or while loop
# conditions to track position of middle item in the list

def binary_search(list, element):
    start = 0
    middle = 0
    end = len(list)
    steps = 0

    while start<=end:
      print(f'"Steps",steps, ":", str(list[start:end+1])')

      steps = steps + 1
      middle = (start + end) // 2

      if element == list[middle]:
        return middle
      if element < list[middle]:
         end = middle - 1
      else:
         start = middle + 1   