import os
import tkinter as tk

os.system('clear')


class PasswordManagerGUI:
    """
    Global User Interface Class that structures the Password Manager Application
    """

    def __init__(self):
        self._root = tk.Tk()  # starts tkinter window
        self._root.title('Password Manager')  # sets title of application
        self._root.geometry('800x600')  # sets window size of the application

        # User information
        self._email = tk.StringVar()
        self._username = tk.StringVar()
        self._password = tk.StringVar()
        self._password_rentry = tk.StringVar()

        # Log In
        self._login_username = tk.StringVar()
        self._login_password = tk.StringVar()

        self._data = [{'website': 'Facebook',
                       'username': 'treyboo',
                       'password': '1234'}]  # list of dictionary objects to store website, username and password

        # Used for adding and editing accounts
        self._temporary_website = tk.StringVar()
        self._temporary_username = tk.StringVar()
        self._temporary_password = tk.StringVar()
        self._temporary_renter_password = tk.StringVar()
        self._row_counter = 1

        # Used for search bar
        self._search = tk.StringVar()

        # Editing and deleting accounts
        self._marked_account = None  # Logic state for editing and deleting actions
        self._marked_account_index = None  # Logic state for editing and deleting actions

        self.start_window()  # run the first window


    def get_email(self):
        """
        Get email of user.
        :return:
        """
        return self._email

    def set_email(self, new_email):
        """
        Set the email of a user.
        :param new_email:
        :return:
        """
        self._email = new_email

    def get_username(self):
        """
        Get username of user.
        """
        return self._username

    def set_username(self, new_username):
        """
        Sets new username
        :param new_username:
        :return:
        """
        self._username = new_username

    def get_password(self):
        """
        Get password of user
        """
        return self._password

    def set_password(self, new_password):
        """
        :param new_password:
        :return:
        """
        self._password = new_password

    def get_password_rentry(self):
        """
        Get password of user
        """
        return self._password_rentry

    def set_password_rentry(self, new_password):
        """
        :param new_password:
        :return:
        """
        self._password_rentry = new_password

    def get_user_data(self):
        """Returns user data"""
        return self._data

    def add_data(self, data):
        """Adds dictionary object to list"""
        self._data.append(data)

    def clear_window(self):
        """Clear window command"""
        for widget in self._root.winfo_children():
            widget.destroy()

    def close_window(self):
        """Closes window"""
        self._root.destroy()

    def help_window(self):
        """Help window pop-up that explains the software to the user"""
        window = tk.Tk()
        window.geometry('400x200')
        window.title('Help & Information')

        help_label = tk.Label(window, text='Password Manager is an application that allows the storing and \n '
                                           'management of multiple accounts and their associated passwords.\n'
                                           'Please create an account and log in to access the application.\n')
        help_label.pack(padx=10, pady=10)

        return_button = tk.Button(window, text='Return', command=lambda: [window.destroy()])
        return_button.pack(padx=10, pady=10)

        window.mainloop()

    def start_window(self):
        """Function to create the start window of the password manager application"""

        self.clear_window()

        # Create a frame object to store welcome message and buttons
        frame = tk.Frame(master=self._root, relief=tk.SUNKEN, borderwidth=5)
        frame.pack(padx=150, pady=150)

        # Welcome to Title
        welcome_message = tk.Label(frame, text='Welcome to Password Manager',
                                   font=('Times New Roman', 23))  # creates a text entry
        welcome_message.pack(padx=50, pady=50)

        # Instructions
        instruction_message = tk.Label(frame, text='Please sign-up or login.',
                                       font=('Times New Roman', 12))  # creates a text entry
        instruction_message.pack(padx=10, pady=10)

        # Sign Up Button
        signup_button = tk.Button(frame, text='Sign Up', command=self.sign_up)
        signup_button.pack(padx=5, pady=5)

        # Log In Button
        login_button = tk.Button(frame, text='Already have an account? Login Here', command=self.log_in)
        login_button.pack(padx=5, pady=5)

        # Help Button
        help_button = tk.Button(self._root, text='Help', command=self.help_window)
        help_button.pack(side='bottom')

        self._root.mainloop()

    def sign_up(self):
        """
        Changes window to a sign-up window.
        """
        self.clear_window()
        self._root.title('Sign Up')  # sets title of application

        # Create a frame object to store welcome message and buttons
        frame = tk.LabelFrame(master=self._root, relief=tk.SUNKEN, borderwidth=5, text='Sign Up')
        frame.pack(padx=100, pady=100)

        # Sign Up Frame
        # Email Entry
        email_entry = tk.Entry(frame,
                               font=('Times New Roman', 12), textvariable=self._email, width=30)  # creates a text entry
        email_entry.grid(row=0, column=1, padx=10, pady=10)
        # Email Label
        email_label = tk.Label(frame, text='Email:')
        email_label.grid(row=0, column=0, padx=10, pady=10)

        # Username Entry
        username_entry = tk.Entry(frame,
                                  font=('Times New Roman', 12), textvariable=self._username,
                                  width=30)  # creates a text entry
        username_entry.grid(row=1, column=1, padx=10, pady=10)
        # Username Label
        username_label = tk.Label(frame, text='Username:')
        username_label.grid(row=1, column=0, padx=10, pady=10)

        # Password Entry
        password_entry = tk.Entry(frame,
                                  font=('Times New Roman', 12), textvariable=self._password,
                                  width=30, show='*')  # creates a text entry
        password_entry.grid(row=2, column=1, padx=10, pady=10)
        # Password Label
        password_label = tk.Label(frame, text='Password:')
        password_label.grid(row=2, column=0, padx=10, pady=10)

        # Password Rentry
        password_rentry = tk.Entry(frame,
                                   font=('Times New Roman', 12), textvariable=self._password_rentry,
                                   width=30, show='*')  # creates a text entry
        password_rentry.grid(row=3, column=1, padx=10, pady=10)
        # Password Rentry Label
        password_rentry_label = tk.Label(frame, text='Retype Password:')
        password_rentry_label.grid(row=3, column=0, padx=10, pady=10)

        # Return Button
        return_button = tk.Button(frame, text='Cancel', command=self.start_window)
        return_button.grid(row=4, column=0)

        # Confirm Sign Up Button
        signup_button = tk.Button(frame, text='Sign Up', command=self.confirm_signup)
        signup_button.grid(row=4, column=1)

        # Help Button
        help_button = tk.Button(self._root, text='Help', command=self.help_window)
        help_button.pack(side='bottom')

        self._root.mainloop()

    def missing_signup_parameters(self):
        """
        Checking the entry parameters if they are missing
        :return:
        """
        user_data = [self._email, self._username, self._password, self._password_rentry]
        for data in user_data:
            if len(data.get()) <= 1:
                return True

    def password_check(self):
        """If both passwords do not match"""
        if self._password.get() != self._password_rentry.get():
            return True

    def error_window(self):
        """
        Pop-up window to display error and return to sign up page.
        """
        window = tk.Tk()
        window.geometry('300x100')
        window.title('Error!')

        password_label = tk.Label(window, text='Error: Something went wrong, please try again.')
        password_label.pack(padx=10, pady=10)

        retry_button = tk.Button(window, text='Return to Sign Up',
                                 command=lambda: [window.destroy(), self.sign_up()])
        retry_button.pack(padx=10, pady=10)

    def confirm_signup(self):
        """Confirms user input information is correct"""
        if self.missing_signup_parameters():
            self.error_window()
        elif self.password_check():
            self.error_window()
        else:
            window = tk.Tk()
            window.geometry('300x100')
            window.title('Success!')

            password_label = tk.Label(window, text='Account created successfully. Proceed to login.')
            password_label.pack(padx=10, pady=10)

            continue_button = tk.Button(window, text='Log In', command=lambda: [window.destroy(), self.log_in()])
            continue_button.pack(padx=10, pady=10)

    def log_in(self):
        self.clear_window()
        self._root.title('Login')  # gives window a title

        # Create a frame object to store welcome message and buttons
        frame = tk.LabelFrame(master=self._root, relief=tk.SUNKEN, borderwidth=5, text='Log In')
        frame.pack(padx=100, pady=100)

        # Username Entry
        username_entry = tk.Entry(frame,
                                  font=('Times New Roman', 12), textvariable=self._login_username,
                                  width=30)  # creates a text entry
        username_entry.grid(row=1, column=1, padx=10, pady=10)
        # Username Label
        username_label = tk.Label(frame, text='Username:')
        username_label.grid(row=1, column=0, padx=10, pady=10)

        # Password Entry
        password_entry = tk.Entry(frame,
                                  font=('Times New Roman', 12), textvariable=self._login_password, width=30,
                                  show='*')  # creates a text entry
        password_entry.grid(row=2, column=1, padx=10, pady=10)

        # Password Label
        password_label = tk.Label(frame, text='Password:')
        password_label.grid(row=2, column=0, padx=10, pady=10)

        # Return Button
        return_button = tk.Button(frame, text='Cancel', command=self.start_window)
        return_button.grid(row=4, column=0)

        # Confirm Log In Button
        login_button = tk.Button(frame, text='Log In', command=self.verify_login)
        login_button.grid(row=4, column=1)

        # Help Button
        help_button = tk.Button(self._root, text='Help', command=self.help_window)
        help_button.pack(side='bottom')

        self._root.mainloop()

    def missing_login_parameters(self):
        """
        Checking the entry parameters if they are missing
        :return:
        """
        user_data = [self._login_username, self._login_password]
        for data in user_data:
            if len(data.get()) <= 1:
                return True

    def incorrect_login(self):
        correct_user = self._username.get()
        correct_password = self._password.get()
        login_user = self._login_username.get()
        login_password = self._login_password.get()

        if correct_user != login_user:
            if correct_password != login_password:
                return True

    def verify_login(self):
        """
        Ensure that the login information matches the sign-up information
        """
        correct_user = self._username.get()
        correct_password = self._password.get()
        login_user = self._login_username.get()
        login_password = self._login_password.get()

        if self.missing_login_parameters() or self.incorrect_login():
            window = tk.Tk()
            window.geometry('300x100')
            window.title('Error!')

            password_label = tk.Label(window, text='Incorrect login information. Please try again.')
            password_label.pack(padx=10, pady=10)

            continue_button = tk.Button(window, text='Log In', command=lambda: [window.destroy(), self.log_in()])
            continue_button.pack(padx=10, pady=10)

        elif correct_user == login_user:
            if correct_password == login_password:
                window = tk.Tk()
                window.geometry('300x100')
                window.title('Success!')

                password_label = tk.Label(window, text='Login Successful!')
                password_label.pack(padx=10, pady=10)

                continue_button = tk.Button(window, text='Continue',
                                            command=lambda: [window.destroy(), self.home_page()])
                continue_button.pack(padx=10, pady=10)

    def search(self):
        """Used as search bar"""
        found_accounts = []

        for account in self.get_user_data():
            if account['website'] == self._search.get():
                found_accounts.append(account)

        if len(found_accounts) == 0:
            self.error_window()
        else:
            self.search_results_window(found_accounts)

    def search_results_window(self, accounts):
        """Results window"""
        window = tk.Tk()
        window.title('Accounts Found!')

        account_frame = tk.Frame(window, relief=tk.SOLID, borderwidth=3)
        account_frame.grid(row=0, column=0)

        website_label = tk.Label(master=account_frame, text='Website', relief=tk.SUNKEN, borderwidth=2, height=3,
                                 width=15)
        website_label.grid(row=0, column=0)

        username_label = tk.Label(master=account_frame, text='Username', relief=tk.SUNKEN, borderwidth=2, height=3,
                                  width=15)
        username_label.grid(row=0, column=1)

        password_label = tk.Label(master=account_frame, text='Password', relief=tk.SUNKEN, borderwidth=2, height=3,
                                  width=15)
        password_label.grid(row=0, column=2)

        for account in accounts:
            website_name = account['website']
            website_data_label = tk.Label(master=account_frame, text=website_name, relief=tk.RAISED, borderwidth=1,
                                          height=1, width=15)
            website_data_label.grid(row=self._row_counter, column=0)
            user_name = account['username']
            user_name_data_label = tk.Label(master=account_frame, text=user_name, relief=tk.RAISED, borderwidth=1,
                                            height=1, width=15)
            user_name_data_label.grid(row=self._row_counter, column=1)
            password = account['password']
            password_data_label = tk.Label(master=account_frame, text=password, relief=tk.RAISED, borderwidth=1,
                                           height=1, width=15)
            password_data_label.grid(row=self._row_counter, column=2)

    def home_page(self):
        """Brings user to the home page of the password manager"""
        self.clear_window()

        self._root.geometry('850x500')  # sets window size of the application
        self._root.title('Password Manager')

        home_button = tk.Button(self._root, text='Home', command=self.home_page)
        home_button.grid(row=0, column=0)

        add_button = tk.Button(self._root, text='Add Account', command=self.add_account)
        add_button.grid(row=0, column=1)

        search_button = tk.Button(self._root, text='Search:', command=self.search)
        search_button.grid(row=1, column=1)
        search_entry = tk.Entry(self._root, textvariable=self._search)
        search_entry.grid(row=1, column=2)

        advanced_options_button = tk.Button(self._root, text='Advanced Options', command=self.advanced_options)
        advanced_options_button.grid(row=0, column=2)

        password_frame = tk.Frame(master=self._root, relief=tk.SOLID, borderwidth=3)
        password_frame.grid(row=2, column=0, padx=15, pady= 15)

        website_label = tk.Label(master=password_frame, text='Website', relief=tk.SUNKEN, borderwidth=2, height=3,
                                 width=15)
        website_label.grid(row=0, column=0)

        username_label = tk.Label(master=password_frame, text='Username', relief=tk.SUNKEN, borderwidth=2, height=3,
                                  width=15)
        username_label.grid(row=0, column=1)

        password_label = tk.Label(master=password_frame, text='Password', relief=tk.SUNKEN, borderwidth=2, height=3,
                                  width=15)
        password_label.grid(row=0, column=2)

        edit_label = tk.Label(master=password_frame, text='Edit Button', relief=tk.SUNKEN, borderwidth=2, height=3,
                              width=15)
        edit_label.grid(row=0, column=3)

        delete_label = tk.Label(master=password_frame, text='Delete Button', relief=tk.SUNKEN, borderwidth=2, height=3,
                                width=15)
        delete_label.grid(row=0, column=4)

        self._row_counter = 1
        for data in self.get_user_data():
            website_name = data['website']
            website_data_label = tk.Label(master=password_frame, text=website_name, relief=tk.RAISED, borderwidth=1,
                                          height=1, width=15)
            website_data_label.grid(row=self._row_counter, column=0)
            user_name = data['username']
            user_name_data_label = tk.Label(master=password_frame, text=user_name, relief=tk.RAISED, borderwidth=1,
                                            height=1, width=15)
            user_name_data_label.grid(row=self._row_counter, column=1)
            password = data['password']
            password_data_label = tk.Label(master=password_frame, text=password, relief=tk.RAISED, borderwidth=1,
                                           height=1, width=15)
            password_data_label.grid(row=self._row_counter, column=2)
            edit_button = tk.Button(master=password_frame, text='Edit',
                                    command=lambda: [self.mark_account(edit_button.grid_info()), self.edit_account()],
                                    height=1,
                                    width=15)
            edit_button.grid(row=self._row_counter, column=3)
            delete_button = tk.Button(master=password_frame, text='Delete',
                                      command=lambda: [self.mark_account(delete_button.grid_info()),
                                                       self.delete_account(), self.home_page()], height=1,
                                      width=15)
            delete_button.grid(row=self._row_counter, column=4)
            self._row_counter += 1

        # Help Button
        help_button = tk.Button(self._root, text='Help', command=self.help_window)
        help_button.grid(row=0, column=3)

        self._root.mainloop()

    def add_account(self):
        """Brings user to the add account page."""
        self.clear_window()

        home_button = tk.Button(self._root, text='Home', command=self.home_page)
        home_button.grid(row=0, column=0)

        add_button = tk.Button(self._root, text='Add Account', command=self.add_account)
        add_button.grid(row=0, column=1)

        help_button = tk.Button(self._root, text='Help', command=self.help_window)
        help_button.grid(row=0, column=3)

        add_account_frame = tk.Frame(master=self._root, relief=tk.SOLID, borderwidth=3)
        add_account_frame.grid(row=2, column=0)

        # Labeling
        website_label = tk.Label(master=add_account_frame, text='Website: ')
        website_label.grid(row=0, column=0)

        user_name_label = tk.Label(master=add_account_frame, text='Username: ')
        user_name_label.grid(row=1, column=0)

        password_label = tk.Label(master=add_account_frame, text='Password: ')
        password_label.grid(row=2, column=0)

        renter_password_label = tk.Label(master=add_account_frame, text='Re-enter Password: ')
        renter_password_label.grid(row=3, column=0)

        # Entries
        website_entry = tk.Entry(master=add_account_frame, textvariable=self._temporary_website, width=30)
        website_entry.grid(row=0, column=1)

        user_name_entry = tk.Entry(master=add_account_frame, textvariable=self._temporary_username, width=30)
        user_name_entry.grid(row=1, column=1)

        password_entry = tk.Entry(master=add_account_frame, textvariable=self._temporary_password, width=30, show='*')
        password_entry.grid(row=2, column=1)

        renter_password_entry = tk.Entry(master=add_account_frame, textvariable=self._temporary_renter_password,
                                         width=30, show='*')
        renter_password_entry.grid(row=3, column=1)

        # Buttons
        cancel_button = tk.Button(master=add_account_frame, text='Cancel', command=self.home_page)
        cancel_button.grid(row=4, column=0)

        add_button = tk.Button(master=add_account_frame, text='Add', command=self.verify_add_account)
        add_button.grid(row=4, column=1)

        self._root.mainloop()

    def verify_add_account(self):
        """Verifies the added account has all parameters filled and passwords match"""
        cache = [self._temporary_website, self._temporary_username, self._temporary_password,
                 self._temporary_renter_password]

        for data in cache:
            if len(data.get()) <= 1:
                self.verification_error()

        if self._temporary_password.get() != self._temporary_renter_password.get():
            self.verification_error()

        else:
            self.add_data({'website': self._temporary_website.get(), 'username': self._temporary_username.get(),
                           'password': self._temporary_password.get()})  # add data to init data storage
            window = tk.Tk()
            window.geometry('300x100')
            window.title('Success!')

            password_label = tk.Label(window, text='Account added successfully.')
            password_label.pack(padx=10, pady=10)

            retry_button = tk.Button(window, text='Return to Home',
                                     command=lambda: [window.destroy(), self.home_page()])
            retry_button.pack(padx=10, pady=10)

    def verification_error(self):
        """If verification error, pop up this window."""
        window = tk.Tk()
        window.geometry('300x100')
        window.title('Error!')

        password_label = tk.Label(window, text='Error: Something went wrong, please try again.')
        password_label.pack(padx=10, pady=10)

        retry_button = tk.Button(window, text='Return to Add Account',
                                 command=lambda: [window.destroy(), self.add_account])
        retry_button.pack(padx=10, pady=10)

    def mark_account(self, info):
        """Mark the specific account for editing or deleting"""
        row_number = info['row']
        account = self.get_user_data()[row_number - 1]
        self._marked_account = account
        self._marked_account_index = row_number - 1

    def edit_account(self):
        """Edit account window"""
        self.clear_window()

        home_button = tk.Button(self._root, text='Home', command=self.home_page)
        home_button.grid(row=0, column=0)

        add_button = tk.Button(self._root, text='Add Account', command=self.add_account)
        add_button.grid(row=0, column=1)

        edit_account_frame = tk.Frame(master=self._root, relief=tk.SOLID, borderwidth=3)
        edit_account_frame.grid(row=2, column=0)

        # Labeling
        website_label = tk.Label(master=edit_account_frame, text='Website: ')
        website_label.grid(row=0, column=0)

        user_name_label = tk.Label(master=edit_account_frame, text='Username:')
        user_name_label.grid(row=1, column=0)

        password_label = tk.Label(master=edit_account_frame, text='Password: ')
        password_label.grid(row=2, column=0)

        renter_password_label = tk.Label(master=edit_account_frame, text='Re-enter Password: ')
        renter_password_label.grid(row=3, column=0)

        # Entries
        website_entry = tk.Entry(master=edit_account_frame, textvariable=self._temporary_website, width=30)
        website_entry.insert(0, self._marked_account['website'])
        website_entry.grid(row=0, column=1)

        user_name_entry = tk.Entry(master=edit_account_frame, textvariable=self._temporary_username, width=30)
        user_name_entry.insert(0, self._marked_account['username'])
        user_name_entry.grid(row=1, column=1)

        password_entry = tk.Entry(master=edit_account_frame, textvariable=self._temporary_password, width=30, show='*')
        password_entry.insert(0, self._marked_account['password'])
        password_entry.grid(row=2, column=1)

        renter_password_entry = tk.Entry(master=edit_account_frame, textvariable=self._temporary_renter_password,
                                         width=30, show='*')
        renter_password_entry.insert(0, self._marked_account['password'])
        renter_password_entry.grid(row=3, column=1)

        cancel_button = tk.Button(master=edit_account_frame, text='Cancel', command=self.home_page)
        cancel_button.grid(row=4, column=0)

        edit_button = tk.Button(master=edit_account_frame, text='Confirm Edit',
                                command=lambda: [self.edit_data(), self.home_page()])
        edit_button.grid(row=4, column=1)

        self._root.mainloop()

    def edit_data(self):
        self._data[self._marked_account_index]['website'] = self._temporary_website.get()
        self._data[self._marked_account_index]['username'] = self._temporary_username.get()
        self._data[self._marked_account_index]['password'] = self._temporary_password.get()
        return

    def delete_account(self):
        del self._data[self._marked_account_index]
        return

    def advanced_options(self):
        pass


if __name__ == "__main__":
    PasswordManagerGUI()
