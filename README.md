# mle-razrabotka-v-ide

Шаблон репозитория для самостоятельного задания спринта 6 курса Инженер Машинного Обучения Яндекс Практикума

## Какую проблему решает проект

Класс `DataFrameReporter` из [src/reporter.py](src/reporter.py) для первоначального знакомства с датафреймом: собирает стартовые
проверки в один отчёт и печатает его одной командой — `show_report(df)` —
вместо набора разрозненных вызовов `pandas`.

Отчёт включает:
- количество столбцов и строк;
- количество и долю дубликатов;
- базовые статистики (`df.describe()`);
- количество и долю пропущенных значений.

## Установка окружения

Проект использует виртуальное окружение `venv` и зависимости из
[requirements.txt](requirements.txt).

1. Создайте виртуальное окружение (если его ещё нет):

   ```powershell
   python -m venv venv
   ```

2. Активируйте окружение:

   - PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - cmd.exe:
     ```cmd
     venv\Scripts\activate.bat
     ```
   - Git Bash / Linux / macOS:
     ```bash
     source venv/Scripts/activate  # Windows
     source venv/bin/activate      # Linux/macOS
     ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

## Запуск

Отчёт по датафрейму `data/payments.csv` запускается командой:

```bash
python main.py
```