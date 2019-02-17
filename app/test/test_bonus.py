from app.bonus import bonus


def test_bonus_less_min_sum():
    result = bonus(500, [199, 599, 1699])

    assert 0 == result


def test_bonus_blue_card():
    result = bonus(1399, [399, 899, 8499])

    assert 50 == result


def test_bouns_silver_card():
    result = bonus(2599, [9000, 8990, 15499])

    assert 140 == result


def test_bonus_gold_card():
    result = bonus(3200, [25000, 100000, 25000, 25000])

    assert 300 == result

