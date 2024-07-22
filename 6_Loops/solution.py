for i in range(6):
    if i ==3:   #skips only this particular iteration
        continue
    print(i)

# reverse a string

input_string="lokesh"
reverse_string=""

for char in input_string:
    reverse_string=char+reverse_string

print(reverse_string)


import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
