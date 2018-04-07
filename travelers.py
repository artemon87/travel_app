class Member():
    def __init__(self, name = None, expenses = None):
        self.name = name
        self.expenses = expenses
        self.total = None
        """
        Calculate total as soon as an instance is created
        """
        self.calculate_total()


    def __repr__(self):
        return "%s's total expenses are %d" %(self.name, self.total)

    def calculate_total(self):
        try:
            return sum(self.expenses)
        except TypeError:
            """
            In case if string or unicode char was passed
            """
            return sum(int(exp) for exp in self.expenses)

    