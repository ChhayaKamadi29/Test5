#A list contains the denominations as follows : D = [2000, 500, 200, 100 , 50, 20, 10, 5] Accept an amount from user and calculate how many minimum number of notes will be needed for that amount.


def min_notes(amount):
    D = [2000, 500, 200, 100, 50, 20, 10, 5]
    notes_count = {}
    total_notes = 0

    for note in D:
        if amount >= note:
            count = amount // note
            notes_count[note] = count
            total_notes += count
            amount %= note

    return total_notes, notes_count

amount = int(input("Enter amount: "))
total, breakdown = min_notes(amount)
print(f"Minimum notes needed: {total}")
for note, count in breakdown.items():
    print(f"Rs {note} x {count}")