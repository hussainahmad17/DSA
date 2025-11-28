prices = [17,4,12,6,8,9]

def task(prices):
    max_profit = 0

    for i in range(len(prices)):
         for j in range(i+1, len(prices)):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
    return max_profit

print(task(prices))


# optimum solution

array = [7,1,5,3,6,4]

def task(array):
    max_prof = 0
    min_price = float('inf')
    for i in range(len(array)):
        min_price = min(min_price, array[i])
        max_prof = max(max_prof, array[i] - min_price)
    return max_prof