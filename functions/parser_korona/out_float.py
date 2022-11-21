from check_number import is_number

# to_pay_in_html = '1,465.00 RUB'
def out_float(to_pay_in_html):
    words_list = to_pay_in_html.split()
    print(words_list)
    for num in words_list:
        number = num.replace(",", "")
        if is_number(number):
            to_pay = float(number)
            print(f'to_pay: {to_pay}')
    return to_pay
