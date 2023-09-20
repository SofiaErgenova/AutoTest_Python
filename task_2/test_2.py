from main import login, post, get_post

def test_2(login):
    my_post = post(login)
    all_posts = get_post(login)
    lst = all_posts['data']
    lst_description = [el["description"] for el in lst]

    assert "Мое первое автотестирование" in lst_description, 'тест провален'