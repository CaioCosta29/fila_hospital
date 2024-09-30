from persistencia.paciente_persis import paciente_persis

class PacienteService:
    def __init__(self):
        self.paciente_persis = paciente_persis

    def inserir_paciente(self, paciente_VO):
        self.validar_dados(paciente_VO)
        
        paciente_existe = self.verificar_se_paciente_esta_na_fila(paciente_VO)
        
        
        if paciente_existe == False: # mudar para false
            self.paciente_persis.cadastrar_paciente(paciente_VO)
        else:
            raise ValueError("Já existe uma paciente com esse codigo")


    def exibir_proximo_paciente(self):
        proximo_paciente = self.paciente_persis.procurar_proximo_paciente()
        
        
        return proximo_paciente

    def exibir_tamanho_fila(self):
        tamanho_fila = self.paciente_persis.medir_tamanho_fila()

        return tamanho_fila

    def exibir_posicao_paciente(self, paciente_VO):
        paciente_existe = self.verificar_se_paciente_esta_na_fila(paciente_VO)

        if paciente_existe == True:
            posicao = self.paciente_persis.procurar_posicao_paciente(paciente_VO)

            return posicao
        
        raise ValueError("Esse paciente não existe")
    
    def atender_paciente(self):
        self.paciente_persis.atender_paciente()

        

    def verificar_se_paciente_esta_na_fila(self, paciente_VO):
        pacientes = self.paciente_persis.obter_pacientes()

        for paciente in pacientes:
            if paciente.codigo == paciente_VO.codigo:
                return True
            
        return False

    def validar_dados(self, paciente_VO):
        if len(paciente_VO.codigo) != 6:
            raise ValueError("Codigo Invalido")
        if not paciente_VO.codigo.isdigit():
            raise ValueError("Codigo Invalido")

