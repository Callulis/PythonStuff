# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
  answer = 0
  prices.sort()
  while rupees > prices[0] and len(prices) > 0:
        temp = prices[0]
        rupees -= temp
        answer+=1
        del prices[0]
  return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)