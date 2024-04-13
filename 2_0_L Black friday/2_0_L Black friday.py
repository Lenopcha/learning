
queue = list(map(int, input("Enter number how many consoles each customer want, separated by space: ").split()))
available_consoles = int(input("Enter the number of available consoles: "))

customers_served = 0
last_person_consoles = 0

for consoles in queue:
    if consoles <= available_consoles:
        customers_served += 1
        available_consoles -= consoles
        last_person_consoles = consoles
    else:
        customers_served += 1
        last_person_consoles = available_consoles
        break


print("How many people in line:", len(queue))
print("Number of customers served:", customers_served)

print("Number of consoles received by the last person served:", last_person_consoles)

