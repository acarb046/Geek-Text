# the myViews.py file


def star_rating(rating):
    stars = '★' * rating #will print the stars the per rating
    return stars

def main():
    while True: #while this code is true, do whats in it
        try: #try catch in case someone inputs things that shouldn't
            user_input = int(input("Thanks for reading! Please rate the book from 1 to 5: "))
            if 1 <= user_input < 6: #if someone follows the rules, stop the loop and print
                break
            else:
                print("Oops, not quite.")
        except ValueError:
            print("Only numbers are allowed, thanks!")

    visual_aide = star_rating(user_input) #a variable that displays the stars holding the user input
    print("Geek Text Rating:", visual_aide) #print the rating

if __name__ == "__main__":
    main()
