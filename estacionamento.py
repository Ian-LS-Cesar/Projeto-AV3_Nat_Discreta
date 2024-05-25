class Estacionamento:
    def __init__(self, valor_fixo, valor_extra, linhas, colunas):
        self.valor_fixo = valor_fixo
        self.valor_extra = valor_extra
        self.linhas = linhas
        self.colunas = colunas
        self.estacionamento = [[' ' for _ in range(colunas)] for _ in range(linhas)]
        self.placas = {}
        self.tempo_estacionamento = {}

    def mostrarEstacionamento(self):
        for linha in self.estacionamento:
            print(' '.join(linha))
            print('---------')

    def adicionarCarro(self, linha, coluna, placa):
        if self.estacionamento[linha][coluna] == ' ':
            self.estacionamento[linha][coluna] = 'X'
            self.placas[(linha, coluna)] = placa
            hora_chegada = input("Hora de chegada (HH:MM): ")
            hora_chegada = list(map(int, hora_chegada.split(":")))
            self.tempo_estacionamento[(linha, coluna)] = hora_chegada
            print(f"Carro com placa {placa} adicionado ao estacionamento na posição ({linha}, {coluna})")
        else:
            print("Vaga já ocupada!")

    def removerCarro(self, linha, coluna):
        if self.estacionamento[linha][coluna] == 'X':
            placa = self.placas.pop((linha, coluna))
            hora_saida = input("Hora de saída (HH:MM): ")
            hora_saida = list(map(int, hora_saida.split(":")))
            hora_chegada = self.tempo_estacionamento.pop((linha, coluna))
            self.pagarEstacionamento(hora_chegada[0], hora_chegada[1], hora_saida[0], hora_saida[1], placa)
            self.estacionamento[linha][coluna] = ' '
            print(f"\nCarro com placa {placa} removido do estacionamento na posição ({linha}, {coluna}) e o valor do estacionamento foi pago")
        else:
            print("Vaga já vazia!")

    def funcaoTeto(self, horas, minutos):
        tempo_extra = (horas - 3)
        if (minutos!= 0):
            tempo_extra += 1
        return tempo_extra

    def pagarEstacionamento(self, hora_chegada, minuto_chegada, hora_saida, minuto_saida, placa):
        # Conversão do tempo
        tempo_chegada_em_minutos = hora_chegada * 60 + minuto_chegada
        tempo_saida_em_minutos = hora_saida * 60 + minuto_saida

        #Caso a saída foi no dia seguinte
        if tempo_saida_em_minutos < tempo_chegada_em_minutos:
            tempo_saida_em_minutos += 24 * 60

        diferenca_tempo_em_minutos = tempo_saida_em_minutos - tempo_chegada_em_minutos
        horas = diferenca_tempo_em_minutos // 60
        minutos = diferenca_tempo_em_minutos % 60

        #Cálculo do estacionamento
        if(diferenca_tempo_em_minutos > 15):
            if (horas <= 3):
                total_estacionamento = self.valor_fixo
            else:
                total_estacionamento = self.valor_fixo + (self.funcaoTeto(horas,minutos) * self.valor_extra)
        else:
            total_estacionamento = 0

        print(f"\nO tempo total no estacionamento: {horas:02d}:{minutos:02d}\nO valor do estacionamento para o carro com placa {placa} ficou R${total_estacionamento:.2f}")

    def executar(self):
        while True:
            self.mostrarEstacionamento()
            acao = input("Digite 'adicionar' para adicionar um carro, 'remover' para remover um carro, ou 'sair' para sair: ")
            if acao == 'adicionar':
                linha = int(input("Digite a linha: "))
                coluna = int(input("Digite a coluna: "))
                placa = input("Digite a placa: ")
                self.adicionarCarro(linha, coluna, placa)
            elif acao == 'remover':
                linha = int(input("Digite a linha: "))
                coluna = int(input("Digite a coluna: "))
                self.removerCarro(linha, coluna)
            elif acao == 'sair':
                break
            else:
                print("Ação inválida. Tente novamente!")

# Crie um estacionamento com 5 linhas e 5 colunas
estacionamento = Estacionamento(5, 2, 5, 5)
estacionamento.executar()