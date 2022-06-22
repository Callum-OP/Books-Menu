# import matplotlib and use plt as an alias
import matplotlib.pyplot as plt


# main function code
def main():

    book_list = []
    read_file(book_list)

    # print the list of options to choose from
    print('**************************_Books_Menu_**************************')
    print('1 - List of each book and its details with a summary')
    print('2 - Average price of all books in stock')
    print('3 - Number of books per genre')
    print('4 - Add a new book to the list of books')
    print('5 - Change the stock of a chosen title')
    print('6 - View books ordered by title or genre')
    print('7 - Books per genre bar chart')
    print('8 - Exit the program\n')

    while True:
        # ask user to enter one of the 8 numbers
        selection = input('Please select a number from the menu above: ')

        # if user entered 1 call get_summary function
        if selection == '1':
            print('\n')
            get_summary(book_list)

        # if user entered 2 call get_average function
        elif selection == '2':
            print('\n')
            get_average(book_list)

        # if user entered 3 call get_genre function
        elif selection == '3':
            print('\n')
            get_genre(book_list, selection)

        # if user entered 4 call add_book function
        elif selection == '4':
            print('\n')
            add_book(book_list)

        # if user entered 5 call change_stock function
        elif selection == '5':
            print('\n')
            change_stock(book_list)

        # if user entered 6 call order_book function
        elif selection == '6':
            print('\n')
            order_book(book_list)

        # if user entered 7 call genre_chart function
        elif selection == '7':
            print('\n')
            get_genre(book_list, selection)

        # if user entered 8 exit the program
        elif selection == '8':
            print('\n')
            print('Thanks for using, bye')
            break
        # print error if they selected anything else
        else:
            print('Error, please select another option')


# function to fill book_list with book details
def read_file(book_list):

    # open the text file
    infile = open('book_data_file.txt')
    for row in infile:
        start = 0
        string_builder = []
        # if the row isn't a comment append and strip each word in the row to a list
        if not row.startswith('#'):
            for index in range(len(row)):
                if row[index] == ',' or index == len(row) - 1:
                    string_builder.append(row[start:index].strip())
                    start = index + 1
            book_list.append(string_builder)
    # close the text file
    infile.close()


# function to list all book details and summary
def get_summary(book_list):

    total_titles = 0
    total_value = 0

    print('*************************************_Books_List_*************************************')
    print('Author,     Title,     Format,     Publisher,     Cost,     Stock,     Genre')

    for each_book in book_list:
        print(each_book)
        total_titles = total_titles + 1
        # if current book is in stock
        if each_book[5] != 0:
            # calculate total value by price * stock
            total_value += float(each_book[4])*float(each_book[5])

    print('\n')
    print('**************************_Books_Summary_**************************')
    print('Total number of book titles =', total_titles)
    print('Total value of books in stock = ', format(total_value, ',.2f'), sep='£')
    print('\n')


# function to calculate the average price of books that are in stock
def get_average(book_list):

    title_value = 0
    count = 0

    for each_book in book_list:
        # if stock of book is not 0
        if each_book[5] != 0:
            # add price to title_value
            title_value += float(each_book[4])
            count = count + 1
    average = title_value / count

    print('**************************_Average_Price_**************************')
    print('Average price of books that are in stock = ', format(average, ',.2f'), sep='£')
    print('\n')


# function to count the number of books for each genre
# depending on selection this can print the genre count or display it in a bar chart
def get_genre(book_list, selection):

    genre_list = []
    duplicate_genre_list = []
    genre_count_dict = {}
    count = 0
    index = 0

    # add genre of each book to both genre lists and remove duplicates from genre_list
    for each_book in book_list:
        genre_list += [each_book[6]]
        duplicate_genre_list += [each_book[6]]
        genre_list = list(dict.fromkeys(genre_list))

    # find current genre and then count how many times that genre appears in duplicate_genre_list
    # then update the each genre and each count to a dictionary
    for _ in genre_list:
        genre = genre_list[index]
        for each_genre in duplicate_genre_list:
            if each_genre == genre_list[index]:
                count = count + 1
        index = index + 1
        genre_count_dict.update({genre: count})
        count = 0

    # if user selected to see the number of books per genre, print genre_count_dictionary
    if selection == '3':
        print('**************************_Books_Per_Genre_**************************')
        print('Number of books in stock for each genre')
        print(genre_count_dict)
    # if user selected bar chart, build the bar chart, from page 415 Starting out with Python, Tony Gaddis
    elif selection == '7':
        bar_label = genre_count_dict.keys()
        bar_count = genre_count_dict.values()
        bar_width = 0.5
        plt.bar(bar_label, bar_count, bar_width)
        plt.show()
    print('\n')


# function to allow a user to add a new book to the books list
def add_book(book_list):

    total_value = 0
    new_total_titles = 0
    new_total_value = 0
    count = 0
    new_count = 0
    average = 0

    for each_book in book_list:
        # if stock of book is not 0
        if float(each_book[5]) != 0:
            # add price to total_value
            total_value += float(each_book[4])
            count = count + 1
            average = total_value / count

    while True:
        new_book = []
        # ask user if they want to add a new book and then ask them to enter each of the details
        begin = input('Do you want to add a new book? (y for yes | n for no): ')
        # if user says yes
        if begin == 'y' or begin == 'Y':
            author = input('Enter the author of the book: ')
            new_book.append(author)
            title = input('Enter the title of the book: ')
            new_book.append(title)
            book_format = input('Enter the format of the book: ')
            new_book.append(book_format)
            publisher = input('Enter the publisher of the book: ')
            new_book.append(publisher)
            cost = input('Enter the cost (in decimal) of the book: ')
            new_book.append(cost)
            stock = input('Enter the number of books that are available: ')
            new_book.append(stock)
            genre = input('Enter the genre of the book: ')
            new_book.append(genre)

            print('\n')
            print('These are the details of the new book you have entered')
            print(new_book, sep='\n')
            print('\n')

            # check if user is happy with the details they entered
            append = input('Is this the book you want to add to books list? (y for yes | n for no): ')
            # if user said yes append new_book to book_list
            if append == 'y' or append == 'Y':
                book_list.append(new_book)
                print('New book has been added to books list')
                new_total_titles = new_total_titles + 1

                print('\n')
                print('**************************_New_Books_Summary_**************************')

                # calculate the new average
                for each_book in book_list:
                    # if book is in stock
                    if float(each_book[5]) != 0:
                        # add price to new_total_value
                        new_total_value += float(each_book[4])
                        new_count = new_count + 1
                new_average = new_total_value / new_count
                difference = new_average - average

                print('Total number of titles has increased by', new_total_titles)
                print('The original average = ', format(average, ',.2f'), sep='£')
                print('The new average = ', format(new_average, ',.2f'), sep='£')

                if new_average >= average:
                    print('The average price per book has increased by ', format(difference, ',.2f'), sep='£')
                elif new_average < average:
                    print('The average price per book has decreased by -', format(-difference, ',.2f'), sep='£')
            print('\n')
        # if user said no
        else:
            print('Returning to main menu')
            break
    print('\n')


# function to allow user to increase or decrease stock of chosen book title
def change_stock(book_list):

    title_stock = {}
    book_count = 0
    change = ''

    # gather each title with the stock it has and put it into a dictionary
    for each_book in book_list:
        book_count = book_count + 1
        title = each_book[1]
        stock = each_book[5]
        # add title as key and stock as value
        title_stock.update({title: stock})
        if book_count == len(book_list):
            break

    print('**************************_Change_Stock_**************************')
    # ask user if they want to change the stock of a title
    begin = input('Do you want to change the stock of a title? (y for yes | n for no): ')
    # if user said yes ask them to enter the title and whether stock has increased or decreased
    if begin == 'y' or begin == 'Y':
        stock_title = input('Select a title to change the stock it has: ')
        stock = title_stock.get(stock_title, 'Title not found')
        # show the current stock, if title isn't found restart function
        print('Number of', stock_title, 'books in stock =', stock)
        if stock == 'Title not found':
            print('\n')
            change_stock(book_list)
        else:
            change = input('Has the stock increased or decreased? Type anything else to exit: ')

        # if user said increased ask user how much the stock has increased by
        if change == 'increased' or change == 'Increased':
            increase = int(input('How much has the stock increased?: '))
            new_stock = int(stock) + increase
            # show the new stock and replace the old stock in book_list
            print('New number of', stock_title, 'books in stock =', new_stock)
            for each_book in book_list:
                if each_book[1] == stock_title:
                    each_book[5] = new_stock
        # if user said decreased ask user how much the stock has decreased by
        elif change == 'decreased' or change == 'Decreased':
            decrease = int(input('How much has the stock decreased?: '))
            new_stock = int(stock) - decrease
            # if the book is out of stock alert the user
            if new_stock <= 0:
                print(stock_title, 'books are now out of stock')
                new_stock = 0
            # if the book is still in stock show the new stock
            else:
                print('New number of', stock_title, 'books in stock =', new_stock)
            # replace the old stock in book_list
            for each_book in book_list:
                if each_book[1] == stock_title:
                    each_book[5] = str(new_stock)
        # if user didn't choose increased or decreased
        else:
            print('Returning to main menu')
    # if user said no
    else:
        print('Returning to main menu')
    print('\n')


# function to allow user to order book list by title or genre in alphabetical order
def order_book(book_list):

    title_book_list = book_list
    genre_book_list = book_list

    print('1 - Order by title')
    print('2 - Order by genre')
    print('Enter any other key to go back to main menu')
    print('\n')
    # ask user what they want to order by
    choice = input('Please choose a number from above: ')
    # if user selected 1 print each book ordered by title
    if choice == '1':
        # from page 380 Starting out with Python, Tony Gaddis
        # title_book_list equal to book_list sorted by key=title
        title_book_list.sort(key=lambda x: x[1])
        print('Ordered by title')
        for each_book in title_book_list:
            print(each_book)
    # if user selected 2 print each book ordered by genre
    elif choice == '2':
        # from page 380 Starting out with Python, Tony Gaddis
        # genre_book_list equal to book_list sorted by key=genre
        genre_book_list.sort(key=lambda x: x[6])
        print('Ordered by genre')
        for each_book in genre_book_list:
            print(each_book)
    # if user selected anything else
    else:
        print('Returning to main menu')
    print('\n')


main()
