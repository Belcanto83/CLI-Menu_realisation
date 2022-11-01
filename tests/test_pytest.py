import pytest
from copy import deepcopy
from main import print_all_documents_to_stdout, add_document, summa


FIXTURE_SUMMA = [
    (2, 3, 5),
    (-2, 3, 1),
    (44, 48, 92),
]

FIXTURE_CLI_MENU_DOCUMENTS = (
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "101", "name": "Михаил Светлов"}
)

FIXTURE_CLI_MENU_DIRECTORIES = (
    ('1', ['2207 876234', '11-2', '101']),
    ('2', ['10006', '55']),
    ('3', []),
)

FIXTURE_CLI_MENU_DOCS_TO_ADD = iter((
    ('passport, 3208-1111, Иван Иванов', '2'),
    ('invoice, 5678-123, Стас Седов', '5'),
))


@pytest.fixture()
def data_for_test_add_document():
    result_documents = iter([
        [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
            {"type": "insurance", "number": "101", "name": "Михаил Светлов"},
            {"type": "passport", "number": "3208-1111", "name": "Иван Иванов"}
        ],
        [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
            {"type": "insurance", "number": "101", "name": "Михаил Светлов"},
        ]
    ])
    result_directories = iter([
        {
            '1': ['2207 876234', '11-2', '101'],
            '2': ['10006', '55', '3208-1111'],
            '3': []
        },
        {
            '1': ['2207 876234', '11-2', '101'],
            '2': ['10006', '55'],
            '3': []
        },
    ])
    data = (
        (next(result_documents), next(result_directories)),
        (next(result_documents), next(result_directories)),
    )
    return data


@pytest.mark.parametrize('a, b, exp_res', FIXTURE_SUMMA)
def test_summa(a, b, exp_res):
    res = summa(a, b)
    assert exp_res == res


def test_print_all_documents_to_stdout(monkeypatch, input_data=FIXTURE_CLI_MENU_DOCUMENTS):
    """
    Проверяем, что вывод тестируемой функции правильно отсортирован
    по параметру "type" (тип документа) в порядке возрастания
    """

    expected_result = [
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "insurance", "number": "101", "name": "Михаил Светлов"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    ]

    # monkeypatch.setattr('builtins.input', lambda _: "type")
    inputs = iter(('type', 'up'))
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = print_all_documents_to_stdout(input_data)

    assert result == expected_result


def test_add_document(monkeypatch, data_for_test_add_document, documents=FIXTURE_CLI_MENU_DOCUMENTS,
                      directories=FIXTURE_CLI_MENU_DIRECTORIES, docs_to_add=FIXTURE_CLI_MENU_DOCS_TO_ADD):
    """
    Проверяем, что функция добавила в каталог и на полку первый документ и не добавила второй
    """

    # results = data_for_test_add_document

    for itm in data_for_test_add_document:
        inputs = iter(next(docs_to_add))
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        result = add_document(deepcopy(list(documents)), deepcopy(dict(directories)))
        assert itm == result
