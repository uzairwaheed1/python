# question1
for i in range(1, 11):
    print(f"Current: {i}, Previous: {i-1}, Sum: {i + (i-1)}")


# question2
for i in range(1, 6):
    print(' '.join(str(i) for _ in range(i)))




# question3
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5 == 0:
        if num > 150:
            continue
        elif num > 500:
            break
        else:
            print(num)




# question4
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b




# question5

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = 5  # Replace with the desired number
print(f"The factorial of {num} is: {factorial(num)}")





# question6
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count_dict = {}

for item in sample_list:
    count_dict[item] = count_dict.get(item, 0) + 1

print("Printing count of each item:")
for key, value in count_dict.items():
    print(f"{key}: {value}", end=', ')
    
    

# question7

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]


index1 = 0
index2 = 0
l3 = []

for i in l1:
    if index1 % 2 != 0:
        l3.append(i)
    index1 += 1
        
        
for j in l2:
    # print(index2)
    if index2 % 2 == 0:
        l3.append(j)
    index2 += 1
        
for p in l3:
    print(p)





