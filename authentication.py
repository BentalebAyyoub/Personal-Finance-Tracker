import hashlib

class UserManager:
    """
    A class to manage user registration and authentication.

    Attributes:
        credentials_file (str): The file path to store user credentials.
    """

    def __init__(self, credentials_file='data/user_credentials.txt'):
        """
        Initializes the UserManager with the specified credentials file.

        Args:
            credentials_file (str, optional): The file path to store user credentials.
                Defaults to 'user_credentials.txt'.
        """
        self.credentials_file = credentials_file

    def register_user(self, username, password):
        """
        Registers a new user with the given username and password.

        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.
        """
        hashed_password = self._hash_password(password)
        if not self._username_exists(username):
            with open(self.credentials_file, 'a') as file:
                file.write(f"{username}:{hashed_password}\n")
            print("User registered successfully.")
        else:
            print("Username already exists. Please choose a different one.")

    def login_user(self, username, password):
        """
        Authenticates a user with the given username and password.

        Args:
            username (str): The username of the user to authenticate.
            password (str): The password of the user to authenticate.
        """
        hashed_password = self._hash_password(password)
        if self._is_authenticated(username, hashed_password):
            print("Login successful. Welcome, " + username + "!")
        else:
            print("Invalid username or password. Please try again.")

    def _hash_password(self, password):
        """
        Hashes the given password using SHA-256.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def _username_exists(self, username):
        """
        Checks if the given username already exists in the credentials file.

        Args:
            username (str): The username to check.

        Returns:
            bool: True if the username exists, False otherwise.
        """
        with open(self.credentials_file, 'r') as file:
            for line in file:
                stored_username, _ = line.strip().split(':')
                if stored_username == username:
                    return True
        return False

    def _is_authenticated(self, username, hashed_password):
        """
        Checks if the given username and hashed password match any stored credentials.

        Args:
            username (str): The username to authenticate.
            hashed_password (str): The hashed password to authenticate.

        Returns:
            bool: True if the username and hashed password match, False otherwise.
        """
        with open(self.credentials_file, 'r') as file:
            for line in file:
                stored_username, stored_hashed_password = line.strip().split(':')
                if stored_username == username and stored_hashed_password == hashed_password:
                    return True
        return False

# Example usage:
#user_manager = UserManager()

#user_manager.register_user("john_doe", "password123")
#user_manager.login_user("john_doe", "password123")
