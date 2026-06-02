branch_names = [
    "Highlands Nha Tho",
    "Highlands Ba Trieu",
    "Highlands Nguyen Du",
    "Highlands Landmark 81",
    "Highlands Tran Hung Dao"
]

daily_revenues = [
    15500000,
    28000000,
    9200000,
    45000000,
    11000000
]

target_achieved = [
    True,
    True,
    False,
    True,
    False
]

while True:

    print("\n===== HE THONG QUAN LY DOANH THU HIGHLANDS =====")
    print("1. Hien thi bao cao doanh thu tong hop")
    print("2. Thong ke chi nhanh cao nhat / thap nhat")
    print("3. Loc danh sach co so kem")
    print("4. Thoat chuong trinh")
    print("================================================")

    choice = input("Nhap lua chon cua ban (1-4): ")

    if choice == "1":

        print("\nBAO CAO DOANH THU")

        for i in range(len(branch_names)):

            if target_achieved[i]:
                status = "Dat"
            else:
                status = "Khong Dat"

            print(
                branch_names[i],
                "-",
                daily_revenues[i],
                "VND -",
                status
            )

        print("Tong doanh thu:", sum(daily_revenues), "VND")

    elif choice == "2":

        max_revenue = max(daily_revenues)
        min_revenue = min(daily_revenues)

        max_index = daily_revenues.index(max_revenue)
        min_index = daily_revenues.index(min_revenue)

        print("\nChi nhanh doanh thu cao nhat:")
        print(branch_names[max_index], "-", max_revenue, "VND")

        print("\nChi nhanh doanh thu thap nhat:")
        print(branch_names[min_index], "-", min_revenue, "VND")

    elif choice == "3":

        failed_branches = []

        for i in range(len(branch_names)):

            if target_achieved[i] == False:
                failed_branches.append(branch_names[i])

        print("\nDanh sach co so khong dat chi tieu:")
        print(failed_branches)

    elif choice == "4":

        print("He thong ghi nhan du lieu hoan tat. Tam biet!")
        break

    else:

        print("[Loi] Lua chon khong hop le, vui long nhap lai so tu 1 den 4!")