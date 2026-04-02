from typing import Dict, Union

VERSION = "1.2-Combined"


class SmartPiggyBank:
    def __init__(self, currency: str = "RUB", enable_notifications: bool = True):
        self.balance = 0.0
        self.goal = 0.0
        self.currency = currency
        self.notifications = enable_notifications

    # add_savings
    def add_savings(self, amount: float) -> str:
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount
        msg = f" Внесено {amount} {self.currency}. Баланс: {self.balance} {self.currency}"
        if self.notifications:
            print(f"[ Уведомление] {msg}")
        return msg

    # set_goal
    def set_goal(self, target: float) -> str:
        if target <= 0:
            raise ValueError("Цель должна быть положительной")
        self.goal = target
        return f" Новая цель: {target} {self.currency}"

    # calculate_interest
    def calculate_interest(self, annual_rate: float, months: int) -> float:
        if annual_rate < 0 or months < 1:
            raise ValueError("Ставка и срок должны быть положительными")
        future_value = self.balance * (1 + annual_rate / 100) ** (months / 12)
        return round(future_value, 2)

    # check_progress
    def check_progress(self) -> Dict[str, Union[float, str]]:
        if self.goal == 0:
            return {"status": "Цель не установлена"}
        percent = min((self.balance / self.goal) * 100, 100)
        remaining = max(self.goal - self.balance, 0)
        return {
            "progress_percent": round(percent, 2),
            "remaining_amount": remaining,
            "currency": self.currency
        }

    def get_status(self) -> Dict[str, Union[float, str, bool]]:
        return {
            "balance": self.balance,
            "goal": self.goal,
            "currency": self.currency,
            "notifications_enabled": self.notifications,
            "app_version": VERSION
        }


if __name__ == "__main__":
    print(f"Запуск Умной копилки v{VERSION}\n" + "="*40)

    piggy = SmartPiggyBank(currency="RUB", enable_notifications=True)

    print(piggy.set_goal(50_000))

    print(piggy.add_savings(15_000))
    print(piggy.add_savings(10_500))

    progress = piggy.check_progress()
    print(f"\nПрогресс: {progress['progress_percent']}%")
    print(f"Осталось накопить: {progress['remaining_amount']} {progress['currency']}")

    projected = piggy.calculate_interest(annual_rate=8.5, months=12)
    print(f"\nПрогноз через 12 мес (ставка 8.5%): {projected} {piggy.currency}")

    # Итог
    print("\n Полный статус:", piggy.get_status())