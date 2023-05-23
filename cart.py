


p_a_cost = 20
p_b_cost = 40
p_c_cost = 50

print("PRODUCT A COST 20$ ")
p_a_quantity = int(input("Enter quantity for product A: "))


print("PRODUCT B COST 40$ ")
p_b_quantity = int(input("Enter quantity for product B: "))


print("PRODUCT C COST 50$ ")
p_c_quantity = int(input("Enter quantity for product C: "))

print("--------------------------------------------------")

if p_a_quantity <= 0:
    p_a_quantity = 1

if p_b_quantity <= 0:
    p_b_quantity = 1

if p_c_quantity <= 0:
    p_c_quantity = 1
   

total_quantity = p_a_quantity + p_b_quantity + p_c_quantity

p_a_total_cost = p_a_cost * p_a_quantity
p_b_total_cost = p_b_cost * p_b_quantity
p_c_total_cost = p_c_cost * p_c_quantity

# rule 2
if p_a_quantity > 10:
    p_a_total_cost = p_a_total_cost - (p_a_total_cost * 5 / 100)
    

 # rule 4
if total_quantity > 30 and p_a_quantity > 15:
    p_a_total_cost = p_a_total_cost - (p_a_total_cost * 50 / 100)

if p_b_quantity > 10:
    p_b_total_cost = p_b_total_cost - (p_b_total_cost * 5 / 100)

# rule 4
if total_quantity > 30 and p_b_quantity > 15:
    p_b_total_cost = p_b_total_cost - (p_b_total_cost * 50 / 100)

if p_c_quantity > 10:
    p_c_total_cost = p_c_total_cost - (p_c_total_cost * 5 / 100)

 # rule 4
if total_quantity > 30 and p_c_total_cost > 15:
    p_c_total_cost = p_c_total_cost - (p_c_total_cost * 50 / 100)

total_cart_cost = p_a_total_cost + p_b_total_cost + p_c_total_cost

# rule 1
if total_cart_cost > 200:
    total_cart_cost = total_cart_cost - 10
    

# rule 3
if total_quantity > 20:
    total_cart_cost = total_cart_cost - (total_cart_cost * 10 / 100)
    
# shipping fee
if total_quantity > 10:
    ship_fee= 5
else:
    ship_fee=0

     
    
# gift wrap
gift_wrap=input("would you like to wrap your product?,(y/n)")
if gift_wrap=='y':
    gift_wrap_price= 1
elif gift_wrap=='n':
    gift_wrap_price= 0 
total= total_cart_cost + ship_fee + gift_wrap_price    


print(f"TOTAL QUANTITY IS: {total_quantity} ")
print(f"SHIPPING FEE: {ship_fee} $")
print(f"GIFT WRAP PRICE:{gift_wrap_price}$")
print(f"TOTAL COST IS: {total_cart_cost} $")
print(f"TOTAL PRICE TO PAY:{total} $")


