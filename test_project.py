from project import Person, secretsantas, purchase, christmasday


def test_secretsantas():
    assert secretsantas(['james', 'peter', 'john', 'andrew']) != ['james', 'peter', 'john', 'andrew']

def test_purchase():
    gifter = Person('karkuen', 'santa')
    gifters = []
    gifters.append(gifter)
    purchase(gifters, 'karkuen', 'cookies')
    assert gifter.gift == 'cookies'

def test_christmasday():
    assert christmasday(['karkuen']) == None