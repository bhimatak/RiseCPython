# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binarySearch(l, key):
	low = 0
	high = len(l) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# If x is greater, ignore left half
		if l[mid] < key:
			low = mid + 1

		# If x is smaller, ignore right half
		elif l[mid] > key:
			high = mid - 1

		# means x is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1


# Test array
l = [ 2, 3, 4, 10, 40 ]
key = 10

# Function call
result = binarySearch(l, key)

if result != -1:
	print("Found Key at index", str(result))
else:
	print("Key is not present in the list")
