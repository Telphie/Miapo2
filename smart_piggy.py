VERSION = "1.0"

class SmartPiggyBank:
    def __init__(self):
    def add_savings(self, amount: float) -> str:
    if amount <= 0:
        raise ValueError("Сумма должна быть положительной")
    self.balance += amount
    return f"✅ Внесено {amount}₽. Баланс: {self.balance}₽"
        self.balance = 0.0
        self.goal = 0.0

    def get_status(self):
        return {"balance": self.balance, "goal": self.goal}