'''
Due Monday
Input user name and phone
Todays movies : Terminator,Star Wars, The Matrix
Morning 7 Afternoon Full Evening 15
For loop, info > yes > end
Info > no > loop
15 seats total
'''
print('Welcome to the Vertedor Cinema!')
def booking():
    phone_number = ''
    Name= input('Please enter your name to reserve a seat for any of the above movies: ')
    while not phone_number.isnumeric():
        phone_number = input(f'Hello {Name}, please enter your phone number: ')
        if not phone_number.isnumeric():
            print ('Please enter 8 decimal numeral characters that correspond to the chain of numbers that people use to contact you over long distances through the small computer that most people own.')
    Movies = ('Terminator','Star_Wars','The_Matrix')
    print ("Choose one of the following movies: ")
    for number, movie in enumerate(Movies):
            print (f"{number+1}. {movie}")
 
    movie_ch = None
    while movie_ch not in range(1,4):
        try:
               movie_ch = int (input ("Which movie would you like to watch? "))
        except:
            print ("Error 404: Number not found")
 
    Sessions = ('Morning','Afteroon','Evening')
    print ("Choose one of the following sessions: ")
    for number, session in enumerate(Sessions):
        print (f"{number+1}. {session}")
 
    session_ch = None
    while session_ch not in range(1,4):
        try:
            session_ch = int (input ("Which session would you like to book? "))
        except:
            print ("Error 404: Number not found")
   
    #Display the seats
    booked_seats = [[[],[14],[]],[[],[],[12,15]],[[],[],[1]]]
    print(f'Seats for movie {movie_ch} during session {session_ch}')
    seats_txt = ''
    for seat_number in range(1,21):
        if seat_number in booked_seats[movie_ch-1][session_ch-1]:
            seats_txt = seats_txt + ' X'
        else:
            seats_txt = seats_txt + f" {seat_number}"
    print (seats_txt)
   
    booked_seats[movie_ch-1][session_ch-1].append(16)
   
 
#Main app    
info = 0
while info==0:  
    booking()
    inf = None
    while inf not in ('yes','no'):
        inf = input('Have you entered all your information correctly? ')
   
    match inf:
        case 'yes':
            info = 1
            print ("Adios")
        case 'no':
            infor = None
            while infor not in ('yes','no'):
                infor = input('Again? ')
            if infor=='no':
                info = 1
                print('Bye')
            else:
                info = 0
 


