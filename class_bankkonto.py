class Account:
    def __init__(self, owner, account_name, account_type, account_number) -> None:
        self.owner = owner
        self.account_name = account_name
        self.account_type = account_type
        self.account_number = account_number

    def __str__(self) -> str:
        return f"Owner: {self.owner}, account name: {self.account_name}, account type: {self.account_type}, account number: {self.account_number}"

    def __repr__(self)-> str:
        return f"\nOwner: {self.owner}, account name: {self.account_name}, account type: {self.account_type}, account number: {self.account_number}"
