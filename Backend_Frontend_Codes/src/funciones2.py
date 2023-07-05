import pandas as pd
import funciones as f

def guardarCSV(filas,nombresArchivos,url):
    df = pd.DataFrame(data=filas,columns=nombresArchivos)
    df.insert(0, 'Nombre Archivos', nombresArchivos)
    df.to_csv(url+'calculo.csv',index=False)

#metodo para pasar el encabezado a c1,c2,c3,...
def crearEncabezadoMatrizSimilitud(encabezado):
    lista=[]
    lista.append('')
    for i in range(1,len(encabezado)):
        cad='C'+str(i)
        lista.append(cad)
    return lista

#metodo para pasar de nombre a c1,c2,...
def pasarResultadosC(matriz):
    i=1
    for j in range(len(matriz)):
        cad='C'+str(i)
        matriz[j][0]=cad
        i=i+1
    
#metodo para filtrar archivos segun su procentaje de similitud
#entrada dataframe, poricentaje sobre 100
#salida lista [[nombre1,nombre2,porcentaje]]
def archivosFiltrados(df,porciento):
  tresh=porciento/100

  columns_names = df.columns.values
  #print(columns_names)

  lista=[]

  nFilas=df.shape[0]
  nCol=df.shape[1]
  for i in range(0,nFilas):
    for j in range(i+2,nCol):
      if(df.iloc[i,j]>=tresh):
        l1=[]
        l1.append(df.iloc[i,0])
        l1.append(columns_names[j])
        l1.append(round(df.iloc[i,j]*100,2))
        lista.append(l1)
  
  return lista



def obtenerSimilitudDosTextos(c1,c2):
  triangularVectorial = f.calcularDisimilitudVectorial2(c1,c2)
  filas = f.retornarFilasDisimilitudVectorial(triangularVectorial)
  f.redondearFilas(filas)
  return round(filas[0][1]*100,2)



def normalizacionCodigosTexto(c1,c2):
  listaTokensCod = []
  lineas = f.eliminarComentariosLineas(c1)
  lista = f.separarCaracteresLineas(c1)
  lista= f.eliminarNombreVariables(lista)
  listaT = f.concatenarTokensEnUnaLista(lista)
  
  listaTokensCod.append(listaT)

  lineas = f.eliminarComentariosLineas(c2)
  lista = f.separarCaracteresLineas(c2)
  lista=f.eliminarNombreVariables(lista)
  listaT = f.concatenarTokensEnUnaLista(lista)
  
  listaTokensCod.append(listaT)
  
  return listaTokensCod

