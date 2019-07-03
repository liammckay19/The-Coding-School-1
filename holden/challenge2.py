name = 'bob'

numberOfJeans = 5
priceOfJeans = 20
taxRate = 0.10

# Real Explanation
# The variable numberOfJeans is set to 5, priceOfJeans
# is 10 and taxRate is 0.10. The total price ((5 * 10) * (1 + .10)) = 55

# EXAMPLE
# 20$ is taxed at 10%
# 20 + (20 * taxRate)
# 20 + (20 * 0.10)

# OR
# 20 * (1+0.10)
# 20 * 1.10
# = 22

# Output format
" < name > will spend $ < total > on < numberOfJeans > pairs of jeans."
print(str(name)+" will spend $110 0n "+str(numberOfJeans)+" pairs of jeans")