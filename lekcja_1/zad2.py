import random
from datetime import datetime

sigma = random.randint(1, 100) # 1 - 100
sigma2 = random.randrange(1, 100) # 1 - 99
sigma3 = random.random() # 0 - 1

print(sigma, sigma2, sigma3)

today = datetime.today()
print(today)