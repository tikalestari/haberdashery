# [2,3,1,0,5,6]
# k = 3
# [1, 0, 0, 0]
# [0,5,6] => 0


# [5,4,3,2]
# k = 2
# [4]

from queue import PriorityQueue

# pq = PriorityQueue
# pq.put(1)
# pq.put(0)
# pq.get() # 0
# pq.get() # 1
# pq.remove(5)

def min_window(numbers, k):
  i = 0
  j = k
  result = []
  while j <= len(numbers): # what is the complexity of this loop
    temp_min = numbers[i]
  	for n in range(k): # what is the complexity of this loop
      if numbers[i+n] < temp_min:
        temp_min = numbers[i+n]
    result.append(temp_min)
    i += 1
    j += 1

  return result

def min_window_2(numbers, k):
  i = 0
  j = k
  result = []
  pq = PriorityQueue
  for n in range(k):
    pq.put(numbers[n])
  while j < len(numbers):
    min_element = pq.get()
  	result.append(min_element)
    pq.put(min_element)
    pq.remove(numbers[i])
    pq.put(numbers[j])
    i+=1
    j+=1

  return result
