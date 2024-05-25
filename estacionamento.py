
def funcaoTeto(horas, minutos):
    tempo_extra = (horas - 3)
    if (minutos != 0):
        tempo_extra += 1
    return tempo_extra

def Estacionamento():
    
    valor_fixo, valor_extra, total_estacionamento = 5, 3, 0
    
    
    hora_chegada, minuto_chegada = map(int, input("Hora de chegada: ").split(":"))
    hora_saida, minuto_saida = map(int, input("\nHora de saída: ").split(":"))
    
    if (hora_chegada < 0 or hora_saida < 0 or hora_chegada > 23 or hora_saida > 23 or minuto_chegada < 0 or minuto_saida < 0 or minuto_chegada > 59 or minuto_saida > 59):
        print("Hora inválida digitada, tente novamente:\n")
        Estacionamento()
    
    # Conversão do tempo
    tempo_chegada_em_minutos = hora_chegada * 60 + minuto_chegada
    tempo_saida_em_minutos = hora_saida * 60 + minuto_saida
    
    #Caso a saída foi no dia seguinte
    if tempo_saida_em_minutos < tempo_chegada_em_minutos:
        tempo_saida_em_minutos += 24 * 60
    
    diferenca_tempo_em_minutos = tempo_saida_em_minutos - tempo_chegada_em_minutos
    horas = diferenca_tempo_em_minutos // 60
    minutos = diferenca_tempo_em_minutos % 60
    
    print(f"Tempo total no estacionamento: {horas:02d}:{minutos:02d}")
    
    #Cálculo do estacionamento
    
    if(diferenca_tempo_em_minutos > 15):
        if (horas <= 3):
            total_estacionamento = valor_fixo
        else:
            total_estacionamento = valor_fixo + (funcaoTeto(horas,minutos) * valor_extra)
            
    return print(f"\nO valor do estacionamento ficou R${total_estacionamento:.2f}")


        
Estacionamento()
