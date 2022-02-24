from cereal_complex_pipeline import diamond, find_highest_calorie_cereal


def test_find_highest_calorie_cereal():
    cereals = [
        {"name": "high-calorie cereal", "calories": 400},
        {"name": "low-calorie cereal", "calories": 50},
    ]
    result = find_highest_calorie_cereal(cereals)
    assert result == "high-calorie cereal"


def test_diamond():
    res = diamond.execute_in_process()
    assert res.success
    assert res.output_for_node("find_highest_protein_cereal") == "Special K"
