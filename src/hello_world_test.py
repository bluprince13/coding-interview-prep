import pytest
from dataclasses import dataclass

def say_hello(name: str) -> str:
    return f"Hello {name}"

# ------------------------------------------------------------------------------
# TESTS
# ------------------------------------------------------------------------------

@dataclass
class TestData:
    id: str
    input: tuple
    expected: any
    __test__ = False


class TestClass:
    testdata = [
        TestData(id="boy name", input=("Vipin",), expected="Hello Vipin"),
        TestData(id="girl name", input=("Geethu",), expected="Hello Geethu"),
    ]

    @pytest.mark.parametrize(
        "input,expected",
        map(lambda x: (x.input, x.expected), testdata),
        ids=map(lambda x: x.id, testdata),
    )
    def test(self, input, expected):
        actual = say_hello(*input)
        assert actual == expected


if __name__ == "__main__":
    pytest.main()
