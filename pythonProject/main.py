import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def check_winnings(columns, lines, bets, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bets
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbols, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbols)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for column in columns:
        x_count = 0
        for row in range(len(column)):
            if x_count != len(columns) - 1:
                print(column[row], end=" | ")

            else:
                print(column[row], end="")

            x_count += 1

        print()


def deposit():
    while True:
        amount = input("what would u like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("please enter a number")

    return amount


def get_number_of_lines():
    while True:
        lines = input("enter the number of lines you would like to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("please enter a number")

    return lines


def get_bet():
    while True:
        amount = input("what would u like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a number")

    return amount


def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"you do not have enough balance to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on :", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer =input("press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"you left with ${balance}")


main()
