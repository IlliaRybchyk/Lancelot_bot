ru = {

    #-------------------------------------------------------------------------- 
    # RU: Общие команды
    # EN: General commands
    # PL: Ogólne polecenia

    "start": "Привет привет! Выбери действие!",
    "help": "Вот комманды которые я поддерживаю:",

    #-------------------------------------------------------------------------- 
    # RU: Работа с меню
    # EN: Menu management
    # PL: Zarządzanie menu

    "open_balance_menu": "Меню работы с балансом:",
    "open_expense_menu": "Меню работы с расходами:",
    "open_main_menu": "Главное меню:",
    "open_top_up_menu": "Работа с пополнениями:",
    "open_plan_menu": "Работа с планированеим:",

    #-------------------------------------------------------------------------- 
    # RU: Ожидание значений
    # EN: Waiting for values
    # PL: Czekanie na wartości

    "waiting_for_expense_amount": "Напиши мне сколько ты потратил",
    "waiting_for_new_balance_amount": "Напиши мне сколько у тебя сейчас есть денег(Например 1000.1):",
    "waiting_for_expense_category": "Выбери категорию расходов:",
    "waiting_for_expense_commentary": "Впиши комментарий к расходам",
    "waiting_for_show_expense_category": "Выбери категорию которую ты хочешь увидеть",
    "waiting_for_plan_amount": "Напиши сумму которую ты хочешь спланировать(Например твоя месячная зарплата):",
    "waiting_for_plan_category": "Выбери категории расходов которые ты хочешь спланировать(Минимум 1):",
    "waiting_for_plan_category_amount": "Сколько ты хочешь выделить на категорию {translated_category}?",
    "chose_another_category": "Хочешь добавить еще категорию?",
    "waiting_for_plan_new_category": "Выбери еще категории расходов которые ты хочешь спланировать:",
    "waiting_for_show_top_up_category": "Выбери категорию пополнений которую хочешь увидеть",
    "waiting_for_top_up_amount": "Напиши мне сколько ты хочешь добавить к своему балансу",
    "waiting_for_show_top_ups_type": "Как вам отобразить пополнения?",
    "waiting_for_top_up_category": "Выбери категорию пополнений:",
    "waiting_for_top_up_comment": "Впиши комментарий к пополнениям:",

    #-------------------------------------------------------------------------- 
    # RU: Отсутствие запросов
    # EN: No requests
    # PL: Brak zapytań

    "not_balance": "У тебя пока нет баланса!",
    "not_expenses": "У тебя пока нет расходов!",
    "not_top_up": "У тебя пока нет пополнений!",
    "not_plan": "У вас нет плана!",

    #-------------------------------------------------------------------------- 
    # RU: Отображение запросов
    # EN: Displaying requests
    # PL: Wyświetlanie zapytań

    "show_balance": "Твой баланс: {balance}",
    "saved_balance": "Сохранил! У тебя есть {amount}",
    "how_to_show_expenses": "Как тебе показать расходы?",
    "expense_saved": (
        "Сохранил расход:\n\n"
        "Сумма: {amount}\n"
        "Категория: {category}\n"
        "Комментарий: {commentary}\n"
        "Оставшийся бюджет на категорию: {remaining_budget}"
    ),
    "expense_details": (
        "\n\nСумма: {amount},\n"
        "Категория: {category},\n"
        "Дата: {date},\n"
        "Комментарий: {comment}\n"
    ),
    "show_expense": "Твои расходы:{expenses_text_result}\n\nОбщая сумма:{all_amount}",
    "plan_category_show": (
        "Название планируемой категории:{category_name}\n\n"
        "Выделенная сумма на категорию:{category_amount}\n"
        "Оставшаяся сумма на категорию:{remaining_category_amount}\n\n"
    ),
    "save_plan": (
        "Общая планируемая сумма:{budget_amount}\n\n"
        "Планируемые категории:\n{category_text}"
        "Остаток:{remaining_amount}"
    ),
    "show_chosen_categories": "Вот твои актуальные категории:\n",
    "confirm_plan": (
        "Вот итоги:\n"
        "Планируемая сумма: {plane_amount}\n\n"
        "Спланированные категории расходов:\n\n"
        "{summary}\n\n"
        "Сумма спланированных расходов: {total}\n"
        "Остаток: {remaining_amount}"
    ),
    "show_all_top_up": (
        'Сумма: {amount},\n'
        'Категория:{category_name},\n'
        'Дата: {date},\n'
        'Комментарий: {comment}\n\n'
    ),
    "show_top_ups": "Твои пополнения:\n\n{top_ups_text}Общая сумма:{all_amount}",
    "confirm_top_up": (
        "Сохранил пополнение:\n\n"
        "Сумма: {amount}\n"
        "Категория:{category}\n"
        "Комментарий: {commentary}"
    ),

    #-------------------------------------------------------------------------- 
    # RU: Очистка историй
    # EN: Clearing histories
    # PL: Czyszczenie historii

    "balance_deleted": "Баланс удален",
    "clear_expenses_list": "Список расходов очищен!",
    "clear_top_ups_list": "История расходов очищена",

    #-------------------------------------------------------------------------- 
    # RU: Ошибки
    # EN: Errors
    # PL: Błędy

    "amount_greater": "Число не должно быть меньше или равно нулю!",
    "expense_greater": "Число не должно быть меньше или равно нулю!",
    "incorrect_amount": "Ты похоже ввел что-то не так!",
    "category_chosen": "Эта категория уже выбрана. Выбери другую",
}

eng = {

    #-------------------------------------------------------------------------- 
    # RU: Общие команды
    # EN: General commands
    # PL: Ogólne polecenia


    "start": "Hello hello! Choose an action!",
    "help": "Here are the commands I support:",

   #-------------------------------------------------------------------------- 
    # RU: Работа с меню
    # EN: Menu management
    # PL: Zarządzanie menu

    "open_balance_menu": "Balance management menu:",
    "open_expense_menu": " Expense management menu:",
    "open_main_menu": "Main menu:",
    "open_top_up_menu": "Manage deposits:",
    "open_plan_menu": "Manage planning:",

   #-------------------------------------------------------------------------- 
    # RU: Ожидание значений
    # EN: Waiting for values
    # PL: Czekanie na wartości

    "waiting_for_expense_amount": "Tell me how much you spent",
    "waiting_for_new_balance_amount": "Tell me how much money you have right now (for example: 1000.1):",
    "waiting_for_expense_category": "Choose an expense category:",
    "waiting_for_expense_commentary": "Enter a comment for the expenses",
    "waiting_for_show_expense_category": "Choose the category you want to view",
    "waiting_for_plan_amount": "Enter the amount you want to plan (for example, your monthly salary):",
    "waiting_for_plan_category": "Choose the expense categories you want to plan (at least 1):",
    "waiting_for_plan_category_amount": "How much do you want to allocate to the category {translated_category}?",
    "chose_another_category": "Do you want to add another category?",
    "waiting_for_plan_new_category": "Choose more expense categories you want to plan:",
    "waiting_for_show_top_up_category": "Choose a top-up category you want to view",
    "waiting_for_top_up_amount": "Tell me how much you want to add to your balance",
    "waiting_for_show_top_ups_type": "How would you like to view the top-ups?",
    "waiting_for_top_up_category": "Choose a top-up category:",
    "waiting_for_top_up_comment": "Enter a comment for the top-up:",

    #-------------------------------------------------------------------------- 
    # RU: Отсутствие запросов
    # EN: No requests
    # PL: Brak zapytań

    "not_balance": "You don't have a balance yet!",
    "not_expenses": "You don't have any expenses yet!",
    "not_top_up": "You don't have any top-ups yet!",
    "not_plan": "You have no plan!",

   #-------------------------------------------------------------------------- 
    # RU: Отображение запросов
    # EN: Displaying requests
    # PL: Wyświetlanie zapytań

    "show_balance": "Your balance is: {balance}",
    "saved_balance": "Saved! You have {amount}",
    "how_to_show_expenses": "How should I show you the expenses?",
    "expense_saved": (
        "Saved the expense:\n\n"
        "Amount: {amount}\n"
        "Category: {category}\n"
        "Comment: {commentary}\n"
        "Remaining budget for the category: {remaining_budget}"
    ),
    "expense_details": (
        "Amount: {amount},\n\n"
        "Category: {category},\n"
        "Date: {date},\n"
        "Comment: {comment}\n"
    ),
    "show_expense": "Your expenses:{expenses_text_result}\n\nTotal amount: {all_amount}",
    "plan_category_show": (
        "Planned category name: {category_name}"
        "Allocated amount for the category: {category_amount}"
        "Remaining amount for the category: {remaining_category_amount}"
    ),
    "save_plan": (
        "Total planned amount: {budget_amount}"
        "Planned categories:{category_text}"
        "Remaining: {remaining_amount}"
    ),
    "show_chosen_categories": "Here are your current categories:\n",
    "confirm_plan": (
        "Here are the results:\n"
        "Planned amount: {plane_amount}\n\n"
        "Planned expense categories:"
        "{summary}\n\n"
        "Total planned expenses: {total}\n"
        "Remaining: {remaining_amount}"
    ),
    "show_all_top_up": (
        "Amount: {amount},\n"
        "Category: {category_name},\n"
        "Date: {date},\n"
        "Comment: {comment}\n\n"
    ),
    "show_top_ups": "Your top-ups:\n{top_ups_text}Total amount: {all_amount}",
    "confirm_top_up": (
        "Top-up saved:\n\n"
        "Amount: {amount}\n"
        "Category: {category}\n"
        "Comment: {commentary}"
    ),

    #-------------------------------------------------------------------------- 
    # RU: Очистка историй
    # EN: Clearing histories
    # PL: Czyszczenie historii

    "clear_expenses_list": "The list of expenses has been cleared!",
    "balance_deleted": "Balance deleted",
    "clear_top_ups_list": "Expense history has been cleared",

    #-------------------------------------------------------------------------- 
    # RU: Ошибки
    # EN: Errors
    # PL: Błędy

    "amount_greater": "The amount must be greater than zero!",
    "expense_greater": "The amount must be greater than zero!",
    "incorrect_amount": "Looks like you entered something wrong!",
    "category_chosen": "This category has already been selected. Please choose another one."
}

pl = {
    
    #-------------------------------------------------------------------------- 
    # RU: Общие команды
    # EN: General commands
    # PL: Ogólne polecenia


    "start":"Cześć cześć! Wybierz akcję!",
    "help":"Oto polecenia, które obsługuję:",

    #-------------------------------------------------------------------------- 
    # RU: Работа с меню
    # EN: Menu management
    # PL: Zarządzanie menu

    "open_balance_menu":"Menu zarządzania saldem:",
    "open_expense_menu":"Menu zarządzania wydatkami:",
    "open_main_menu":"Menu główne:",
    "open_top_up_menu":"Zarządzanie wpłatami:",
    "open_plan_menu":"Zarządzanie planowaniem:",

    #-------------------------------------------------------------------------- 
    # RU: Ожидание значений
    # EN: Waiting for values
    # PL: Czekanie na wartości

    "waiting_for_expense_amount":"Napisz mi, ile wydałeś",
    "waiting_for_new_balance_amount":"Napisz mi, ile masz teraz pieniędzy (na przykład: 1000.1):",
    "waiting_for_expense_category":"Wybierz kategorię wydatków:",
    "waiting_for_expense_commentary":"Wpisz komentarz do wydatków",
    "waiting_for_show_expense_category":"Wybierz kategorię, którą chcesz zobaczyć",
    "waiting_for_plan_amount":"Wpisz kwotę, którą chcesz zaplanować (na przykład swoją miesięczną pensję):",
    "waiting_for_plan_category":"Wybierz kategorie wydatków, które chcesz zaplanować (minimum 1):",
    "waiting_for_plan_category_amount":"Ile chcesz przeznaczyć na kategorię {translated_category}?",
    "chose_another_category":"Chcesz dodać kolejną kategorię?",
    "waiting_for_plan_new_category":"Wybierz kolejne kategorie wydatków, które chcesz zaplanować:",
    "waiting_for_show_top_up_category":"Wybierz kategorię doładowania, którą chcesz zobaczyć",
    "waiting_for_top_up_amount":"Napisz, ile chcesz dodać do swojego salda",
    "waiting_for_show_top_ups_type":"Jak chcesz wyświetlić doładowania?",
    "waiting_for_top_up_category":"Wybierz kategorię doładowań:",
    "waiting_for_top_up_comment":"Wpisz komentarz do doładowania:",

    #-------------------------------------------------------------------------- 
    # RU: Отсутствие запросов
    # EN: No requests
    # PL: Brak zapytań#Отсутствие запросов

    "not_balance":"Nie masz jeszcze salda!",
    "not_expenses":"Nie masz jeszcze żadnych wydatków!",
    "not_top_up":"Nie masz jeszcze żadnych doładowań!",
    "not_plan":"Nie masz planu!",

    #-------------------------------------------------------------------------- 
    # RU: Отображение запросов
    # EN: Displaying requests
    # PL: Wyświetlanie zapytań

    "show_balance":"Twój stan konta: {balance}",
    "saved_balance":"Zapisano! Masz {amount}",
    "how_to_show_expenses":"Jak mam Ci pokazać wydatki?",
    "expense_saved":(
        "Zapisano wydatek:\n\n"
        "Kwota: {amount}\n"
        "Kategoria: {category}\n"
        "Komentarz: {commentary}\n"
        "Pozostały budżet na kategorię: {remaining_budget}"
    ),
    "expense_details": (
        "Kwota: {amount},\n\n"
        "Kategoria: {category},\n"
        "Data: {date},\n"
        "Komentarz: {comment}\n"
    ),
    "show_expense":"Twoje wydatki:{expenses_text_result}\n\nŁączna kwota: {all_amount}",
    "plan_category_show":(
        "Nazwa zaplanowanej kategorii: {category_name}"
        "Przydzielona kwota na kategorię: {category_amount}"
        "Pozostała kwota na kategorię: {remaining_category_amount}"
    ),
    "save_plan":(
        "Całkowita zaplanowana kwota: {budget_amount}"
        "Zaplanowane kategorie:{category_text}"
        "Pozostało: {remaining_amount}"
    ),
    "show_chosen_categories":"Oto twoje aktualne kategorie:\n",
    "confirm_plan":(
        "Oto podsumowanie:\n"
        "Planowana kwota: {plane_amount}\n\n"
        "Zaplanowane kategorie wydatków:"
        "{summary}\n\n"
        "Łączna kwota zaplanowanych wydatków: {total}\n"
        "Pozostało: {remaining_amount}"
    ),
    "show_all_top_up":(
        "Kwota: {amount},\n"
        "Kategoria: {category_name},\n"
        "Data: {date},\n"
        "Komentarz: {comment}\n\n"
    ),
    "show_top_ups:":"Twoje doładowania:\n{top_ups_text}Łączna kwota: {all_amount}",
    "confirm_top_up":(
        "Doładowanie zapisane:\n\n"
        "Kwota: {amount}\n"
        "Kategoria: {category}\n"
        "Komentarz: {commentary}"
    ),

    #-------------------------------------------------------------------------- 
    # RU: Очистка историй
    # EN: Clearing histories
    # PL: Czyszczenie historii

    "balance_deleted":"Saldo usunięte",
    "clear_expenses_list":"Lista wydatków została wyczyszczona!",
    "clear_top_ups_list":"Historia wydatków została wyczyszczona",

    #-------------------------------------------------------------------------- 
    # RU: Ошибки
    # EN: Errors
    # PL: Błędy

    "amount_greater":"Kwota nie może być mniejsza lub równa zeru!",
    "expense_greater":"Kwota nie może być mniejsza lub równa zeru!",
    "incorrect_amount":"Wygląda na to, że wpisałeś coś nieprawidłowo!",
    "category_chosen":"Ta kategoria została już wybrana. Wybierz inną",
}