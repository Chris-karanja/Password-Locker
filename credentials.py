class Credentials:

    """Class Generates new instances of Users"""


    Accounts = []
    platform = ''
    platform_username = ''
    platform_password = ''
    def __init__(self, platform, username, password):
        self.platform = platform
        self.platform_username = username
        self.platform_password = password
                
    def add_credentials(self):
        """ save new credentials to Accounts List """
        Credentials.Accounts.append(self)    


@classmethod
def find_credentials(cls, Network):
        """
        Method that takes in a network and returns a credential that matches that network.
         Args:
            network: platform to search for
        Returns :
            details of platform that matches network.
        """
        for saved_credentials in cls.Accounts:
            if saved_credentials.platform == Network:
                return saved_credentials
