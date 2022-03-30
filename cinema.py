'''
Due Monday
Input user name and phone
Todays movies : Terminator,Star Wars, The Matrix
Morning 7 Afternoon Full Evening 15
For loop, info > yes > end
Info > no > loop
15 seats total
'''
Movies = ('Terminator','Star_Wars','The_Matrix')
Movie1_seats = []
Movie1_seats.append([])
Movie1_seats.append([])
Movie1_seats.append([])
Movie2_seats = []
Movie2_seats.append([])
Movie2_seats.append([])
Movie2_seats.append([])
Movie3_seats = []
Movie3_seats.append([])
Movie3_seats.append([])
Movie3_seats.append([])

Movie1_seats[1].append(1)
Movie1_seats[1].append(12)
phone_number = ''
print(Movie1_seats)
print(Movie2_seats)
print(Movie3_seats)
print(Movies)
Name= input('Please enter your name to reserve a seat for any of the above movies: ')
while not phone_number.isnumeric():
    phone_number = input(f'Hello {Name}, please enter your phone number: ')
    if not phone_number.isnumeric():
        print ('Bad, bad...')


