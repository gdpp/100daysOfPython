def get_active_employees(employees):
    return list(filter(lambda employee: employee["active"], employees))


def sort_by_salary(employees):
    return sorted(employees, key=lambda employee: employee["salary"], reverse=True)


def apply_bonus(employees, percent):
    perc_bonus = percent / 100
    return list(
        map(
            lambda employee: {
                **employee,
                "salary": employee["salary"] + (employee["salary"] * perc_bonus),
            },
            employees,
        )
    )


def average_salary(*salaries):
    if len(salaries) == 0:
        return 0

    return sum(salaries) / len(salaries)
