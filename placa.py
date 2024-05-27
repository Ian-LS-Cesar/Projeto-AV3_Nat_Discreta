def identificarEstado(placa): 
    # intervalos e estado correspondente na forma (incio, fim, estado)
    intervaloEstado =[('HOL', 'HQE', 'Maranhão'), ('HTX', 'HZA', 'Ceará'), ('LVF', 'LWQ', 'Piauí'), ('NHA', 'NHT', 'Maranhão'), 
         ('NHU', 'NIX', 'Piauí'), ('NMP', 'NNI', 'Maranhão'), ('NQL', 'NRE', 'Ceará'), ('NUM', 'NVF', 'Ceará'), 
         ('NWS', 'NXQ', 'Maranhão'), ('OCB', 'OCU', 'Ceará'), ('ODU', 'OEI', 'Piauí'), ('OHX', 'OIQ', 'Ceará'), 
         ('OIR', 'OJQ', 'Maranhão'), ('ORN', 'OSV', 'Ceará'), ('OUA', 'OUE', 'Piauí'), ('OVW', 'OVY', 'Piauí'), 
         ('OXQ', 'OXZ', 'Maranhão'), ('OZA', 'OZA', 'Ceará'), ('PIA', 'PIZ', 'Piauí'), ('PMA', 'POZ', 'Ceará'), 
         ('PSA', 'PTZ', 'Maranhão'), ('QRN', 'QRZ', 'Piauí'), ('RIA', 'RIN', 'Ceará'), ('ROA', 'ROZ', 'Maranhão'), 
         ('RSG', 'RST', 'Piauí'), ('SAN', 'SBV', 'Ceará')]
    
    primeiras3Letras = placa[:3]

    for possibilidade in intervaloEstado:
        # comparação lexicográfica entre as 3 primeiras letras da placa e o intervalo, feita para cada um dos intervalos
        # possíveis para os três estados definidos
        if primeiras3Letras >= possibilidade[0] and primeiras3Letras <= possibilidade[1]:
            print(f'O estado de origem da placa {placa} é {possibilidade[2]}')
            return
        
    print(f'O estado de origem da placa não foi identificado')
        
    

    
            