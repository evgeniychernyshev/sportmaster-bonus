from app.bonus import bonus


def test_bonus_less_min_sum(current_purchase, previous_purchases):
    result = bonus(500, [199, 599, 1699])

    assert 0 == result