#تابع میانگین n عدد ورودی از یک لیست
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

# استفاده از تابع
input_numbers = [10, 20, 30, 40, 50]
result = calculate_average(input_numbers)
print("میانگین اعداد ورودی: ", result)
