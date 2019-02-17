def bonus(current_purchase, previous_purchases):
    blue_card_bonus = 50 # бонусов за каждые полные 1000 руб по синей карте
    silver_card_bonus = 70 # бонусов за каждые полные 1000 руб по серебряной карте
    gold_card_bonus = 100 # бонусов за каждые полные 1000 руб по золотой карте
    total_sum = 0 # сумма всех предыдущих покупок
    bonus_count = 0 # кол-во бонусов с текущей покупки
    min_purchase_sum = 1000 # минимальная сумма, на которую начисляются бонусы

    for purchase in previous_purchases:
        total_sum += purchase

    if current_purchase < min_purchase_sum:
        return 0

    if 1 <= total_sum <= 15000:
        bonus_count = current_purchase // min_purchase_sum * blue_card_bonus

    if 15000 < total_sum <= 150000:
        bonus_count = current_purchase // min_purchase_sum * silver_card_bonus

    if total_sum > 150000:
        bonus_count = current_purchase // min_purchase_sum * gold_card_bonus

    return bonus_count

