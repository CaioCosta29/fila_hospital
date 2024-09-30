import os
from apresentacao.utils import *

from dominio.paciente_service import PacienteService
from dominio.value_object.paciente import Paciente

def exibir_menu_principal():
    while True:
        os.system("cls")
        print("*** Sistema de Controle de Pacientes")
        print("")

        print('''-------- Menu Principal --------
Digite '1' para inserir um paciente na fila
Digite '2' para exibir o proximo paciente
Digite '3' para exibir o tamanho da fila
Digite '4' para exibir sua posição na fila
Digite '5' para atender o paciente
Digite '0' para encerrar o programa''')
        
        try:
            while True:
                char = get_single_char()
                if char.isdigit():
                    escolha_menu = int(char)
                    break

        except ValueError:
            continue
        
        print('')
        match escolha_menu:
            case 1:
                codigo = input("Digite o codigo do paciente: ")
                nome = input("Digite o nome do paciente: ")

                paciente_VO = Paciente(codigo, nome)

                try:
                    paciente_service = PacienteService()
                    paciente_service.inserir_paciente(paciente_VO)

                    print('Cadastrado com sucesso\n')

                except ValueError as erro:
                    print(erro)
                except Exception as erro:
                    print(erro)

                pausar()

            case 2:
                try:
                    paciente_service = PacienteService()
                    proximo_paciente = paciente_service.exibir_proximo_paciente()

                    print(f"O proximo paciente é o/a {proximo_paciente.nome.title()} com o codigo {proximo_paciente.codigo}")

                except ValueError as erro:
                    print(erro)
                except Exception as erro:
                    print(erro)

                pausar()


            case 3:
                try:
                    paciente_service = PacienteService()
                    tamanho_fila = paciente_service.exibir_tamanho_fila()

                    print(f"Tem {tamanho_fila} pessoa{'s' if tamanho_fila != 1 else ''} na fila")

                except ValueError as erro:
                    print(erro)
                except Exception as erro:
                    print(erro)

                pausar()

            case 4:
                try:
                    codigo = input("Digite o codigo do paciente: ")

                    paciente_VO = Paciente(codigo)

                    paciente_service = PacienteService()
                    posicao = paciente_service.exibir_posicao_paciente(paciente_VO)

                    print(f"A posição é {posicao}")

                except ValueError as erro:
                    print(erro)
                except Exception as erro:
                    print(erro)

                pausar()

                

            case 5:
                try:

                    paciente_service = PacienteService()
                    paciente_service.atender_paciente()

                    print("Paciente indo para a consulta")

                except ValueError as erro:
                    print(erro)
                except Exception as erro:
                    print(erro)

                pausar()

            case 0:
                break
        