class Estacionamento:
    def __init__(self, valor_fixo, valor_extra, linhas, colunas):
        self.valor_fixo = valor_fixo
        self.valor_extra = valor_extra
        self.linhas = linhas
        self.colunas = colunas
        # uma matriz pode ser simulada por uma list simples de linhas x colunas espaços
        self.estacionamento = ["       "] * (linhas * colunas)
        # as placas tem que ser armazenadas no estacionamento, pois nao necessariamente saberemos o local em que 
        # o carro estava estacionado, apenas sua placa, pensa como um leitor de placa na entrada e saída, e é a 
        # única informação que teremos, além do horario de chegada e saida, óbvio que para fins práticos nós vamos 
        # escolher onde o carro estaciona, mas em uma aplicação real isso nao ocorreria
        # self.placas = {}
        # nome mais descritivo, já que armazena apenas a hora de chegada. tempo_estacionamento da a entender que 
        # armazenaria o tempo que o carro ficou, o que não é possível já que o horário de saída só é fornecido na 
        # saída, quando o horário de chegada é poppado (então não da nem pra armazenar o valor e também não faria
        # sentido)
        self.horarios_chegada = {}

    def mostrarEstacionamento(self):
        print()
        
        # itera por cada carro e sua posição
        for posicao, carro in enumerate(self.estacionamento):
            # se o resto da posição pela quantidade e colunas for 0, a linha acabou, entao pula pra próxima, mas isso
            # ocorre apenas após a posição 0
            if posicao % self.colunas == 0 and posicao != 0:
                print('\n-------------------------------------------------')

            # a divisão é só estética, tambem deixa mais visível as vagas livres
            print(carro, end=" | ")
            
            

    def adicionarCarro(self, linha, coluna, placa):
        if self.estacionamento[coluna + linha * self.colunas] == '       ':
            self.estacionamento[coluna + linha * self.colunas] = placa
            # self.placas[(linha, coluna)] = placa
            hora_chegada = input("Hora de chegada (HH:MM): ")
            hora_chegada = list(map(int, hora_chegada.split(":")))
            self.horarios_chegada[placa] = hora_chegada
            print(f"\nCarro com placa {placa} adicionado ao estacionamento na posição ({linha}, {coluna})")
        else:
            print("\nVaga já ocupada!")

    def removerCarro(self, placa):
        if placa in self.estacionamento:
            # placa = self.placas.pop((linha, coluna))
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
        # tempo_extra = (horas - 3)
        tempo_extra = horas
        if (minutos != 0):
            tempo_extra += 1
        return tempo_extra

    def pagarEstacionamento(self, hora_chegada, hora_saida, placa):
        # Conversão do tempo
        tempo_chegada_em_minutos = hora_chegada[0] * 60 + hora_chegada[1]
        tempo_saida_em_minutos = hora_saida[0] * 60 + hora_saida[1]

        # o caso que temos é um shopping, não teria nenhum carro que passaria a noite no estacionamento. além
        # disso, para dar 24h o carro teria que chegar e sair na mesma hora (ex: de 23h para 1h do dia seguinte
        # se passam apenas 2h, muito menos que 24, mas o código adicionaria 24h independentemente). considerando
        # até mesmo uma aplicação real não faria sentido e deixaria o resultado errado. to deixando a explicação
        # pra não chegar e só remover sem deixar explícito o motivo 
        # Caso a saída foi no dia seguinte
        # if tempo_saida_em_minutos < tempo_chegada_em_minutos:
        #     tempo_saida_em_minutos += 24 * 60

        diferenca_tempo_em_minutos = tempo_saida_em_minutos - tempo_chegada_em_minutos
        horas = diferenca_tempo_em_minutos // 60
        minutos = diferenca_tempo_em_minutos % 60

        # Cálculo do estacionamento
        if (diferenca_tempo_em_minutos > 15):
            if (horas <= 3):
                total_estacionamento = self.valor_fixo
            else:
                # normalmente, nesse caso, se passa o valor já pronto pra função teto, porque se ela for quem 
                # subtrai 3 das horas, ela não é apenas uma função teto, ela faz mais do que o nome descreve 
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
                # linha = int(input("Digite a linha: "))
                # coluna = int(input("Digite a coluna: "))
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