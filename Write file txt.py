# دریافت نام و نام خانوادگی از کاربر
first_name = input("لطفا نام خود را وارد کنید: ")
last_name = input("لطفا نام خانوادگی خود را وارد کنید: ")

# ایجاد یک فایل txt و ذخیره نام و نام خانوادگی
file_name = "user_info.txt"
with open(file_name, 'w') as file:
    file.write(f"نام: {first_name}\n")
    file.write(f"نام خانوادگی: {last_name}\n")

print(f"اطلاعات شما در فایل {file_name} ذخیره شد.")
