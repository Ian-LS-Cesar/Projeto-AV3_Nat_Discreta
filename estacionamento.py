


def pagarEstacionamento():
    
    horaInicial, minutoInicial = map(int, input("Digite o horário de chegada: ").split(":"))
    horaFinal, minutoFinal = map(int, input("Digite o horário de saída: ").split(":"))
    
    valorEstacionamento == 0 
    
    totalMinutosIniciais = (horaInicial * 60) + minutoInicial
    totalMinutosFinais = (horaFinal * 60) + minutoFinal
    
    # Transformar o tempo total em minutos
    if (horaInicial > horaFinal):
        totalMinutosFinais+= 1440
    else:
        
        if (totalMinutosFinais > totalMinutosFinais):
            totalMinutos = totalMinutosFinais - totalMinutosIniciais
            
        elif (totalMinutosFinais < totalMinutosIniciais):
            totalMinutos = totalMinutosIniciais - totalMinutosFinais
            
        else:
            return valorEstacionamento
    
    #Ver qual o valor a ser pago
    if(totalMinutos > 15):
        pass
    else:
        return valorEstacionamento
    
    
        
    