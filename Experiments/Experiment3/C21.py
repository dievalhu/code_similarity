#ML_T001_HASH_BARRIONUEVO_SANCHEZ_LOACHAMIN_CAMPOVERDE_JIMENEZ_GRANDA

import numpy as np

B = 11
v = [23,14,9,6,30,12,18]  
mod = []
thash = [None] * 11

print('   ****** UNIVERSIDAD POLITECNICA SALESIANA ******\n****** DEBER 01 - MACHINE LEARNING ******')
print('                    Tablas Hash\n')
print('Tabla Hash a ser Llenada \n')
print(thash)
for i in range(len(v)):  ## 0  - 6
    ## 23 MOD 7
    calc = np.mod(v[i], B)  ## Esto calcula las Modas posicion por posicion

    if i == 0:  ## si estamos en el primer elemento simplemente se encola
        mod.append(calc)
        print('esta es la primera moda:' + str(mod))

    else:  ## caso contrario

        print('esta es la ' + str(i + 1) + ' iteracion:')
        print('ESTE ES EL VALOR NUMERICO:' + str(v[i]))

        for j in range(len(mod)):
            print('calc ahora es:' + str(calc))
            print('mod[j] ahora es:' + str(mod[j]))
            if calc == mod[j]:
                print('encontre una colision')
                while (calc == mod[j]):
                    ## APLICAMOS REHASHING
                    print('Calculamos K(x)\n')
                    kx = int((np.mod(v[i], (B - 1))) + 1)
                    print('kx = ' + str(kx) + '\n')
                    print('Calculamos Hi(x)\n')
                    anterior = calc
                    hn = int(np.mod((anterior + kx), B))
                    print('hn = ' + str(hn))
                    calc = hn

                if calc != mod[j]:

                    ## debemos evaluar una vez más
                    #####################################
                    for k in range(len(mod)):
                        print('calc ahora es:' + str(calc))
                        print('mod[j] ahora es:' + str(mod[k]))
                        if calc == mod[k]:
                            print('encontre una colision')
                            while (calc == mod[k]):
                                print('Calculamos K(x)\n')
                                kx = int((np.mod(v[i], (B - 1))) + 1)
                                print('kx = ' + str(kx) + '\n')
                                print('Calculamos Hi(x)\n')

                                if (k == 0):
                                    anterior = calc
                                else:
                                    anterior = hn

                                hn = int(np.mod((anterior + kx), B))
                                print('hn = ' + str(hn))
                                calc = hn

                    ####################################
                    mod.append(calc)
                    print('El vector de moda queda con rehash: ')
                    print(mod)
                    print('Salimos')
                    break
        else:
            mod.append(calc)
            print('El vector de moda queda: ')
            print(mod)

for r in range(len(v)):
    thash[mod[r]] = v[r]
    print(thash)
