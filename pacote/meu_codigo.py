from pacote.moduloA.script_A import var_test_A
from pacote.moduloB.script_B import var_test_B
from pacote.moduloC.script_C import var_test_C


def funcao_concat():
    print(var_test_A + var_test_B + var_test_C)


if __name__ == "__main__":
    print(var_test_A)
    print(var_test_B)
    print(var_test_C)
