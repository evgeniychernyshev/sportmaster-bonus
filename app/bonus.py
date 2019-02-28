def bonus(current_purchase, previous_purchases):
    blue_card_bonus = 50  # бонусов за каждые полные 1000 руб по синей карте
    silver_card_bonus = 70  # бонусов за каждые полные 1000 руб по серебряной карте
    gold_card_bonus = 100  # бонусов за каждые полные 1000 руб по золотой карте
    total_sum = 0  # сумма всех предыдущих покупок
    bonus_count = 0  # кол-во бонусов с текущей покупки
    min_purchase_sum = 1_000  # минимальная сумма покупки, на которую начисляются бонусы

    # количество полных тысяч в сумме текущей покупки
    full_thousand_count = current_purchase // min_purchase_sum

    for purchase in previous_purchases:
        total_sum += purchase

    if current_purchase < min_purchase_sum:
        return 0

    if 1 <= total_sum <= 15_000:
        bonus_count = full_thousand_count * blue_card_bonus

    if 15_000 < total_sum <= 150_000:
        bonus_count = full_thousand_count * silver_card_bonus

    if total_sum > 150_000:
        bonus_count = full_thousand_count * gold_card_bonus

    return bonus_count

