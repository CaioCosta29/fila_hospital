from collections import deque

class PacientePersis:
    def __init__(self):
        self.queue = deque()

    def cadastrar_paciente(self, paciente_VO):
        self.queue.append(paciente_VO)

    def procurar_proximo_paciente(self):
        if self.queue:
            proximo_paciente = self.queue[0]

            return proximo_paciente
        
        raise ValueError("Não existe ninguem cadastrado")
    
    def medir_tamanho_fila(self):
        tamanho_fila = len(self.queue)
        
        return tamanho_fila
    
    def procurar_posicao_paciente(self, paciente_VO):
        for i in range(len(self.queue)):
            if self.queue[i].codigo == paciente_VO.codigo:
                return i + 1
        
    @staticmethod
    def obter_pacientes():
        
        return paciente_persis.queue
    
    def atender_paciente(self):
        if self.queue:
            self.queue.popleft()
        else:
            raise ValueError("Não existe ninguem na fila")
        
paciente_persis = PacientePersis()