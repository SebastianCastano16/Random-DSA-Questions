num_items = int(input())
items = [eval(i) for i in input().split()]
num_orders = int(input())
orders = [eval(i) for i in input().split()]
amount = max(orders)



def restaurant(amount, items):
  dp = [[0] * (len(items)+1) for i in range(amount +1)]
  dp[0] = [1] * (len(items)+1)

  for a in range(1, amount+1):
    for i in range(len(items) -1, -1, -1):
      dp[a][i] = dp[a][i+1]
      if a - items[i] >= 0:
        dp[a][i] += dp[a - items[i]][i]
  return dp

dp = restaurant(amount, items)

def combinationSum(arr, sum):
	ans = []
	temp = []

 	# first do hashing nothing but set{}
 	# since set does not always sort
	# removing the duplicates using Set and
	# Sorting the List

	arr = sorted(list(set(arr)))
	findNumbers(ans, arr, temp, sum, 0)
	return ans

def findNumbers(ans, arr, temp, sum, index):
	
	if(sum == 0):

        # Adding deep copy of list to ans
		ans.append(list(temp))
		return

    # Iterate from index to len(arr) - 1
	for i in range(index, len(arr)):

        # checking that sum does not become negative
		if(sum - arr[i]) >= 0:

	        # adding element which can contribute to sum
			temp.append(arr[i])
			findNumbers(ans, arr, temp, sum-arr[i], i)

            # removing element from list (backtracking)
			temp.remove(arr[i])


yo = []
for i in orders:
  if dp[i][0] == 0:
   print('Impossible')
  elif dp[i][0] >= 2:
    print ('Ambiguous')
  else:
    arr = items
    sum = i
    ans = combinationSum(arr, sum)
# If result is empty, then  # If result is empty, then
    if len(ans) <= 0:
      print("empty")

# print all combinations stored in ans
    for i in range(len(ans)):

      for j in range(len(ans[i])):
        yo.append(items.index(ans[i][j])+1)

    print(*yo, sep=' ')
