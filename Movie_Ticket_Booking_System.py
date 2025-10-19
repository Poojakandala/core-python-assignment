def seat_booking(book_seat):
    booked_seats.append(book_seat)

def cancellation(cancel_seat):
    if cancel_seat in booked_seats:
        booked_seats.remove(cancel_seat)

total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5

seat_booking(book_seat)
available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
print("Available seats:", available_seats)
cancellation(cancel_seat)
