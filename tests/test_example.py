from hexlet_pytest.example import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'

def test_revers_for_empty_string():
    assert reverse('') == ''