from utils import apply_bonus, get_active_employees, sort_by_salary

employees = [
    {"name": "Ana", "salary": 3000, "active": True},
    {"name": "Luis", "salary": 4500, "active": False},
    {"name": "Maria", "salary": 5200, "active": True},
    {"name": "John", "salary": 2800, "active": True},
]


def main():
    active_employees = get_active_employees(employees)
    print(active_employees)

    sorted_employees = sort_by_salary(employees)
    print(sorted_employees)

    bonus_employees = apply_bonus(employees, 20)
    print(bonus_employees)


if __name__ == "__main__":
    main()
