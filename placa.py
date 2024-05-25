# 9/26

# ceara:    HTX - HZA ok
#           NQL - NRE ok 
#           NUM - NVF ok 
#           OCB - OCU
#           OHX - OIQ
#           ORN - OSV
#           OZA
#           PMA - POZ
#           RIA - RIN
#           SAN - SBV

# maranhao: HOL - HQE ok
#           NHA - NHT ok 
#           NMP - NNI ok 
#           NWS - NXQ ok
#           OIR - OJQ
#           OXQ - OXZ
#           PSA - PTZ
#           ROA - ROZ

# piaui:    LVF - LWQ ok
#           NHU - NIX ok
#           ODU - OEI
#           OUA - OUE
#           OVW - OVY
#           PIA - PIZ
#           QRN - QRZ
#           RSG - RST

# a b c d e f g h i j k l m n o p q r s t u v w x y z

def identificarEstado(placa): 
    # trasnformando a string da placa em uma lista de chars
    letrasPlaca = list(placa)

    segundaLetra = letrasPlaca[1]
    terceiraLetra = letrasPlaca[2]
    estado = "Não identificado"
    CE = "Ceará"
    MA = "Maranhão"
    PI = "Piauí"

    match letrasPlaca[0]: 
        case 'H': 
            #                   HT X, Y, Z                                  HU, HV, HW, HX, HY                                    HZA
            if (segundaLetra == 'T' and terceiraLetra >= 'X') or (segundaLetra > 'T' and segundaLetra < 'Z') or (segundaLetra == 'Z' and terceiraLetra == 'A'):
                estado = CE
            #                HO L, M, ..., Y, Z                              HP                            HQ A, B, C, D, E
            elif (segundaLetra == 'O' and terceiraLetra >= 'L') or (segundaLetra == 'P') or (segundaLetra == 'Q' and terceiraLetra <= 'E'):
                estado = MA
        
        case 'L': 
            #               LV F, G, ..., Y, Z                                LW A, B, ..., P, Q    
            if (segundaLetra == 'V' and terceiraLetra >= 'F') or (segundaLetra == 'W' and terceiraLetra <= 'Q'): 
                estado = PI

        case 'N':
            #            NQ L, M, ..., Y, Z                                     NR A, B, C, D, E                            NU M, N, ..., Y, Z                                   NV A, B, C, D, E, F
            if (segundaLetra == 'Q' and terceiraLetra >= 'L') or (segundaLetra == 'R' and terceiraLetra <= 'E') or (segundaLetra == 'U' and terceiraLetra >= 'M') or (segundaLetra == 'V' and terceiraLetra <= 'F'):
                estado = CE
            #                           NH A, B, ..., S, T                                              NM P, Q, ..., Y, Z                              NN A, B, ..., H, I                                   NW S, T, ..., Y, Z                                 NX A, B, ..., P, Q
            elif (segundaLetra == 'H' and terceiraLetra <= 'A' and terceiraLetra <= 'T') or (segundaLetra == 'M' and terceiraLetra >= 'P') or (segundaLetra == 'N' and terceiraLetra <= 'I') or (segundaLetra == 'W' and terceiraLetra >= 'S') or (segundaLetra == 'X' and terceiraLetra <= 'Q'):
                estado = MA
            #               NH U, V, W, X, Y, Z                                NI A, B, ..., W, X
            elif (segundaLetra == 'H' and terceiraLetra >= 'U') or (segundaLetra == 'I' and terceiraLetra <= 'X'): 
                estado = PI
        case 'O': 
            pass
            