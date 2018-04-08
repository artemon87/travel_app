class Member():
    def __init__(self, name = None, expenses = None):
        self.name = name
        self.expenses = expenses
        self.total = None
        self.owns_to = {}
        """
        Calculate total as soon as an instance is created
        """
        self.calculate_total()
        """
        Create wallet for all instances
        """
        self.create_wallet()


    def __repr__(self):
        return "%s's total expenses are %d" %(self.name, self.total)

    def calculate_total(self):
        try:
            self.total = sum(self.expenses)
        except TypeError:
            """
            In case if string or unicode char was passed
            """
            self.total = sum(int(exp) for exp in self.expenses)

    def create_wallet(self):
        self.owns_to['owns to'] = {}

    def set_own_to(self, name = None, amount = None):
        """
        This will sent an amount this person needs to pay to,
        and the amount
        """
        if amount:
            self.owns_to['owns to'][name] = amount
        return True

    