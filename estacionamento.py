class Estacionamento:
    def __init__(self, valor_fixo, valor_extra, linhas, colunas):
        self.valor_fixo = valor_fixo
        self.valor_extra = valor_extra
        self.linhas = linhas
        self.colunas = colunas
        # A matriz pode ser simulada por uma list simples de linhas x colunas espaços
        self.estacionamento = ["       "] * (linhas * colunas)
        self.horarios_chegada = {}

    def mostrarEstacionamento(self):
        print()
        
        # Itera por cada carro e sua posição
        for posicao, carro in enumerate(self.estacionamento):
            # Se o resto da posição pela quantidade e colunas for 0, a linha acabou, entao pula pra próxima, mas isso
            # ocorre apenas após a posição 0
            if posicao % self.colunas == 0 and posicao != 0:
                print('\n-------------------------------------------------')

            # Divisão estética, para deixar mais visíveis as vagas livres
            print(carro, end=" | ")
            
            

    def adicionarCarro(self, linha, coluna, placa):
        if self.estacionamento[coluna + linha * self.colunas] == '       ':
            self.estacionamento[coluna + linha * self.colunas] = placa
            hora_chegada = input("Hora de chegada (HH:MM): ")
            hora_chegada = list(map(int, hora_chegada.split(":")))
            self.horarios_chegada[placa] = hora_chegada
            print(f"\nCarro com placa {placa} adicionado ao estacionamento na posição ({linha}, {coluna})")
        else:
            print("\nVaga já ocupada!")

    def removerCarro(self, placa):
        if placa in self.estacionamento:
            posicao = self.estacionamento.index(placa)
            self.estacionamento[posicao] = '       '
            hora_saida = input("Hora de saída (HH:MM): ")
            hora_saida = list(map(int, hora_saida.split(":")))
            hora_chegada = self.horarios_chegada.pop(placa)
            self.pagarEstacionamento(hora_chegada, hora_saida, placa)
            print(f"\nCarro com placa {placa} removido do estacionamento na posição ({posicao % self.colunas}, {int(posicao / self.colunas)}) e o valor do estacionamento foi pago")
            from placa import identificarEstado
            identificarEstado(placa)
        else:
            print(f"\nCarro com placa {placa} não se encontra no estacionamento")

    def funcaoTeto(self, horas, minutos):
        
        tempo_extra = horas
        if (minutos != 0):
            tempo_extra += 1
        return tempo_extra

    def pagarEstacionamento(self, hora_chegada, hora_saida, placa):
        # Conversão do tempo
        tempo_chegada_em_minutos = hora_chegada[0] * 60 + hora_chegada[1]
        tempo_saida_em_minutos = hora_saida[0] * 60 + hora_saida[1]
        
        diferenca_tempo_em_minutos = tempo_saida_em_minutos - tempo_chegada_em_minutos
        horas = diferenca_tempo_em_minutos // 60
        minutos = diferenca_tempo_em_minutos % 60

        # Cálculo do estacionamento
        if (diferenca_tempo_em_minutos > 15):
            if (horas <= 3):
                total_estacionamento = self.valor_fixo
            else:               
                total_estacionamento = self.valor_fixo + (self.funcaoTeto(horas - 3, minutos) * self.valor_extra)
        else:
            total_estacionamento = 0

        print(f"\nO tempo total no estacionamento: {horas:02d}:{minutos:02d}\nO valor do estacionamento para o carro com placa {placa} ficou R$ {total_estacionamento:.2f}")

    def executar(self):
        while True:
            self.mostrarEstacionamento()
            acao = input("\n\nDigite 'adicionar' para adicionar um carro, 'remover' para remover um carro, ou 'sair' para sair: ")
            if acao == 'adicionar':
                linha = int(input("\nDigite a linha: "))
                coluna = int(input("Digite a coluna: "))
                placa = input("Digite a placa: ")
                self.adicionarCarro(linha, coluna, placa)
            elif acao == 'remover':
                placa = input("\nDigite a placa: ")
                self.removerCarro(placa)
                
            elif acao == 'sair':
                break
            else:
                print("Ação inválida. Tente novamente!")

# Crie um estacionamento com valor fixo de 5 reais, valor extra por hora/fração após 3h de 2 reais e
# com 5 linhas e 5 colunas
estacionamento = Estacionamento(5, 2, 5, 5)
estacionamento.executar()