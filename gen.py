

import random
import time
# Put words here (._.)
start  =  ["example " "example2 "]
middle = ["example3 ", "foo "]
middle2 = ["foo2 ", "foo3 " ]
end = ["foo4", "foo5"]
while True:
    # Sleep for 100ms before running code ('o')
    time.sleep(0.1)
    # Generate sentence (O_O)
    a = random.choice(start)
    d = random.choice(end)
    b = random.choice(middle)
    c = random.choice(middle2)
    post = a + b + c + d
    print(post)