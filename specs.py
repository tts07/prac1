N = 57
Qx = 71.0
W = 59.0
M_MIN_THRESHOLD = 11.5

OIL_DENSITY: float = 850.0

def read_valid_param(prompt: str, min_val: float, max_val: float) -> float:
    """Запрашивает у пользователя число в цикле до попадания в диапазон."""
    while True:
        try:
            # Заменяем запятую на точку для правильного ввода
            user_input = input(prompt).replace(',', '.')
            val = float(user_input)
            if min_val <= val <= max_val:
                return val
            else:
                print(f"Ошибка: значение должно быть в диапазоне от {min_val} до {max_val}")
        except ValueError:
            print("Ошибка: введите корректное число.")

def calc_oil_volume(q_liq: float, w_pct: float) -> float:
    """Вычисляет суточный объёмный дебит чистой нефти."""
    # Формула: Q_н = Q_ж * (1 - W / 100)
    return q_liq * (1 - w_pct / 100.0)

def calc_oil_mass(q_oil: float, density: float = OIL_DENSITY) -> float:
    """Переводит объёмный дебит нефти (м³/сут) в массовый дебит (т/сут)."""
    # Формула: M_н = Q_н * density / 1000
    return q_oil * density / 1000.0

def evaluate_profitability(m_oil: float, m_min: float = M_MIN_THRESHOLD) -> str:
    """Определяет категорию рентабельности скважины по массовому дебиту нефти."""
    if m_oil < m_min:
        return "Убыточная (стоп)"
    elif m_oil < 3 * m_min:
        return "Рентабельная (база)"
    else:
        return "Высокодебитная (приоритет)"

# Блок для проверки (запускается только если запустить этот файл напрямую)
if __name__ == "__main__":
    print("ПРОВЕРКА СПЕЦИФИКАЦИЙ МОДУЛЯ (Вариант А)")
    print("-" * 45)
    print(evaluate_profitability.__doc__)
    print("-" * 45)
    
    # Тестируем функцию на ваших расчетных данных
    test_mass = 24.7435
    status = evaluate_profitability(test_mass)
    print(f"При Mн = {test_mass:.2f} т/сут (порог {M_MIN_THRESHOLD}): -> {status}")