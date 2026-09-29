def read_number(prompt, as_int=True):
    while True:
        text = input(prompt).strip()
        try:
            return int(text) if as_int else float(text)
        except ValueError:
            kind = "whole number" if as_int else "number"
            print(f"  Invalid input. Please enter a valid {kind}.")


def validate_attendance(total, attended):
    if total <= 0:
        return "Total classes must be greater than zero."
    if attended < 0:
        return "Attended classes cannot be negative."
    if attended > total:
        return "Attended classes cannot be greater than total classes."
    return None


def validate_target(target):
    if target < 0 or target > 100:
        return "Target attendance must be between 0 and 100."
    return None


def validate_non_negative(value, label):
    if value < 0:
        return f"{label} cannot be negative."
    return None


def get_attendance():
    while True:
        total = read_number("Total classes: ")
        attended = read_number("Classes attended: ")
        error = validate_attendance(total, attended)
        if error:
            print(f"  Error: {error} Please try again.\n")
        else:
            return total, attended


def get_target():
    while True:
        target = read_number("Target percentage: ", as_int=False)
        error = validate_target(target)
        if error:
            print(f"  Error: {error}")
        else:
            return target


def get_count(label):
    while True:
        value = read_number(f"{label}: ")
        error = validate_non_negative(value, label)
        if error:
            print(f"  Error: {error}")
        else:
            return value


def current_percentage(attended, total):
    return (attended / total) * 100


def future_percentage(attended, total, future_attended, future_missed):
    new_total = total + future_attended + future_missed
    return ((attended + future_attended) / new_total) * 100


def classes_needed_for_target(attended, total, target):
    if current_percentage(attended, total) >= target:
        return 0
    if target >= 100:
        return None

    needed = 0
    while future_percentage(attended, total, needed, 0) < target:
        needed += 1
    return needed


def build_scenario(attended, total, future_attended, future_missed):
    return {
        "current": current_percentage(attended, total),
        "future_attended": future_attended,
        "future_missed": future_missed,
        "new_attended": attended + future_attended,
        "new_total": total + future_attended + future_missed,
        "new_percentage": future_percentage(
            attended, total, future_attended, future_missed
        ),
    }


def show_menu():
    print("\nATTENDANCE SCENARIO CALCULATOR")
    print("1. Calculate current attendance")
    print("2. Find classes needed for target")
    print("3. Predict future attendance")
    print("4. Exit")


def show_current(attended, total):
    print(f"\nCurrent attendance: {current_percentage(attended, total):.2f}%")


def show_target_result(attended, total, target):
    print(f"\nCurrent attendance: {current_percentage(attended, total):.2f}%")
    needed = classes_needed_for_target(attended, total, target)
    if needed is None:
        print(f"Target of {target:g}% cannot be reached.")
    elif needed == 0:
        print("You already meet the target. No extra classes required.")
    else:
        print(f"Classes required to reach target: {needed}")


def show_scenario(result):
    print(f"\nCurrent attendance: {result['current']:.2f}%")
    print(f"Upcoming attended: {result['future_attended']}")
    print(f"Upcoming missed:   {result['future_missed']}")
    print(f"New record: {result['new_attended']}/{result['new_total']}")
    print(f"Predicted attendance: {result['new_percentage']:.2f}%")


def main():
    print("Note: results are for planning only, not an official decision.")
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            total, attended = get_attendance()
            show_current(attended, total)

        elif choice == "2":
            total, attended = get_attendance()
            target = get_target()
            show_target_result(attended, total, target)

        elif choice == "3":
            total, attended = get_attendance()
            fa = get_count("Upcoming classes attended")
            fm = get_count("Upcoming classes missed")
            show_scenario(build_scenario(attended, total, fa, fm))

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
