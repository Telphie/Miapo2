VERSION = "1.1-Goal"

class SmartPiggyBank:
    def __init__(self):
    def add_savings(self, amount: float) -> str:
    if amount <= 0:
        raise ValueError("Сумма должна быть положительной")
    self.balance += amount
    return f" Внесено {amount}₽. Баланс: {self.balance}₽"
        self.balance = 0.0
        self.goal = 0.0

    def get_status(self):
        return {"balance": self.balance, "goal": self.goal}

class SmartPiggyBank:
    def __init__(self):
        self.balance = 0.0
        self.goal = 0.0
        self.currency = "RUB"

    def set_goal(self, target: float) -> str:
        if target <= 0:
            raise ValueError("Цель должна быть положительной")
        self.goal = target
        return f" Новая цель: {target}₽"
    