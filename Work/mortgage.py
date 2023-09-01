"""
Exercise 1.7.

mortgage.py
"""
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = payment + 1000
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
count = 1
while principal > 0:
    if(principal < payment):
        principal = principal * (1+rate/12) - (principal)
        total_paid = total_paid + (payment-principal)
    else:
        if(count >= extra_payment_start_month and count <= extra_payment_end_month):
            principal = principal * (1+rate/12) - extra_payment
            total_paid = total_paid + extra_payment
        else:
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment
    count += 1

    print(f'{count} {round(total_paid,2)} {round(principal,2)}')

print('Total paid', total_paid)

print('Months needed', count)
