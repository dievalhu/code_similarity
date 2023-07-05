from flask import Flask, render_template, request,redirect, url_for, send_from_directory, flash, session, send_file, escape
from os import remove
import math
from flaskext.mysql import MySQL
import funciones 
#importar para encriptar
import bcrypt

from shutil import rmtree
import pandas as pd
import numpy as np

import funciones2

#parte del archivo
import os
UPLOAD_FOLDER = os.path.abspath("../uploads/")


app = Flask(__name__)
#donde se quiere que se suban los archivos
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Settings
app.secret_key = 'mysecretkey'

#configuracion conexion BD
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='tesis'
mysql.init_app(app)

MENUS = {
        'administrador':[['Registrar Personal','Gestion empleados'],['registrar.html','gestionEmpleados.html']],
        'enfermero':[['op1','op2','op3'],['op1.html','op2.html','op3.html']]
        }

#Semilla para encriptamiento
semilla = bcrypt.gensalt()


@app.route('/')
def index():
    #nombre uno de los datos de la sesion
    #si nombre esta en la lista de sesiones
    if 'nombre' in session:
        #si esta logiado carga inicio
        return redirect(url_for('upload'))
    else:
        #si no esta logiado carga ingresar  
        resultado = request.args.get('resultado')     
        return render_template('inicio.html', resultado=resultado)
   


@app.route('/f')
def formulario():
    return render_template('textarea.html')

@app.route('/procesar_codigos', methods=['POST'])
def procesar_codigos():

    comentarios = request.form['cod1']
    lineas1 = comentarios.split('\r\n')
    comentarios2 = request.form['cod2']
    lineas2 = comentarios2.split('\r\n')
    r=funciones2.obtenerSimilitudDosTextos(lineas1,lineas2)

    # Escapar el valor de r para evitar problemas con caracteres especiales en la URL
    #r_escaped = escape(r)

    # Redireccionar a la URL actual con el ancla para la sección de resultado y el parámetro r
    return redirect(url_for('resultado', resultado=r) + '#we_Do')

    # Aquí puedes procesar los datos recibidos del formulario  
    #return render_template('inicio.html', _anchor='we_Do', resultado=r)
    

####################################

@app.route('/resultado')
def resultado():
    resultado = request.args.get('resultado')
    return render_template('inicio.html', resultado=resultado)


####################################

#ruta de inicio
@app.route('/home')
def home():   
       #verificar que hay sesion 
    if 'nombre' in session:
        #Carga template main.html
        return redirect(url_for('upload'))
    else:
        #carga template ingresar
        return render_template('ingresar.html')
    
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

#Define la ruta de registro 
@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    #Si se envia el metodo registrar por GET
    #Si ya esta logiado mandarle al inicio.html
    if(request.method=="GET"):
        #verificar que hay sesion
        if 'nombre' in session:
            #carga template main
            return render_template('home.html')
        else:
            #Acceso no concedido
            return render_template("ingresar.html")
    else:
        #si no realiza con el metodo GET 
        #lo realiza con el metodo POST

        #obtiene los datos 
        nombre=request.form['nmNombreRegistro']
        correo=request.form['nmCorreoRegistro']
        password=request.form['nmPasswordRegistro']
        password_encode=password.encode("utf-8")
        password_encriptado=bcrypt.hashpw(password_encode, semilla)
        print("insertado")

        #preparar el query para inserccion 
        sql = "INSERT INTO usuario (correo,clave_usuario,nombre) VALUES (%s,%s,%s);"
        
        #crear cursor para ejecucion
        conn= mysql.connect()
        cursor= conn.cursor()
        #ejecuta la sentencia
        cursor.execute(sql,(correo,password_encriptado,nombre))
        #ejecuta el commit
        conn.commit()
        conn.close()

        #Registra la sesion
        #Se guardan los parametros que se quieran 
        #nombre del if que se usa por ejemplo
        session['nombre'] = nombre
        session['correo'] = correo

        #crear directorio con su correo
        if os.path.exists(app.config["UPLOAD_FOLDER"]+'/'+ correo) == False: 
            os.mkdir(path=app.config["UPLOAD_FOLDER"] +'/'+correo)
        
        #crear directorio con su correo para
        if os.path.exists(app.config["UPLOAD_FOLDER"]+ '/resultados/'+ correo ) == False: 
            os.mkdir(path=app.config["UPLOAD_FOLDER"] +'/resultados/'+ correo)
            
        #redirige al index
        #url_for(nombre del metodo al que se vaya)
        return redirect(url_for('home'))


#Definir ruta para ingresar 
@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    if (request.method=="GET"):
        if 'nombre' in session:
            #Carga template main.html
            return redirect(url_for('upload'))
        else:
            #Acceso no concebido
            return render_template("ingresar.html")
    else:
        #Obtiene los datos
        correo=request.form['nmCorreoLogin']
        password=request.form['nmPasswordLogin']
        #print(correo)
        #print(password)
        password_encode=password.encode("utf-8")

        #preparar el query para inserccion 
        sql = "SELECT correo,clave_usuario,nombre FROM usuario WHERE correo=%s;"
        
        #crear cursor para ejecucion
        conn= mysql.connect()
        cursor= conn.cursor()
        #ejecuta la sentencia
        cursor.execute(sql,(correo))
        #Obtengo el dato 
        usuario = cursor.fetchone()
        #print(usuario)
        #ejecuta el commit
        conn.commit()
        conn.close()

        #Verificar si la consulta a la BD se obtuvo
        #Ver si usuario es distinto de None
        if (usuario != None):
            #Obtiene el password encriptado encode
            password_encriptado_encode = usuario[1].encode()

            #verifica el password
            if(bcrypt.checkpw(password_encode,password_encriptado_encode)):

                #registra la sesion
                session['nombre']=usuario[2]
                session['correo']=correo
                #print(session['nombre'])
                #print(escape(session['correo']))
                #Redirige al metodo inicio

                if (os.path.exists(app.config["UPLOAD_FOLDER"]+'/'+session['correo']) == False): 
                    os.mkdir(path=app.config["UPLOAD_FOLDER"] +'/'+session['correo'])
                #crear directorio con su correo para
                if os.path.exists(app.config["UPLOAD_FOLDER"]+ '/resultados/'+ correo ) == False: 
                    os.mkdir(path=app.config["UPLOAD_FOLDER"] +'/resultados/'+ correo)

                return redirect(url_for('home'))
            else:
                #Mensaje Flash
                flash("El password no es correcto","alert-warning")

                #Redirige a Ingresar
                return render_template('ingresar.html')
        
        else:
            print('El usuario no existe')
            #Mensaje Flash
            flash("El correo no existe","alert-warning")

            #Redirige a ingresar 
            return render_template('ingresar.html')

#Definir la ruta salir
#Se utiliza para cerrar sesion
# Se limpia la sesion  
@app.route('/salir')
def salir():
    #limpia un argumento de la sesion 
    #Se pone session.pop('nombreVariable',None)
    #None, es para que si no encuentra el nombreVariable
    #no de error 
    session.pop('nombre',None)
    #limpia la sesion 
    session.clear()

    #Manda a ingresar
    return redirect(url_for('inicio'))


###################################



@app.route('/jair')
def jair():
    return '<h1>jair</h1>'



rutas = ['base.py']
i=0
filas = []
nombreMatriz = ''



@app.route("/similitud")
def Similitud():
    global filas 
    global rutas
    global nombreMatriz
    #filas = funciones.calcularMatrizSimlitud(rutas,'../uploads/',3)
    fila1 = funciones.crearEncabezadoMatriz(filas)
    fila2 = fila1[1:]
     
    
    return render_template('similitud.html', matriz = filas, encabezado = fila1, nombre = nombreMatriz, nombresArchivos = rutas[:], encabezado2 = fila2)

@app.route('/calcular', methods=['POST'])
def calcular():
    if request.method == 'POST':
        tipo = request.form['options']  
        tipo = int(tipo)
        

        global rutas
        global filas
        global nombreMatriz
        nombreMatriz = funciones.nombreMatriz(tipo)
        filas = funciones.calcularMatrizSimlitud(rutas,'../uploads/',tipo)       
        return redirect(url_for('Similitud'))
    
#calcular similitud metodo Coseno NUEVO 
@app.route('/calcularSimilitud', methods=['POST'])
def calcularSimilitud():
    if request.method == 'POST':
        tipo = 1
        ruta=request.form['ruta']
        dir=request.form['dir']
        url=ruta+'/'+dir
        print(url)
        global rutas
        global filas
        global nombreMatriz
        rutas = os.listdir(url)
       
        print(rutas)
        nombreMatriz = funciones.nombreMatriz(tipo)
        url_guardar_resultado=app.config["UPLOAD_FOLDER"] +'/resultados/'+ session['correo'] + '/'+dir
        filas = funciones.calcularMatrizSimlitud(rutas,url+'/',tipo,url_guardar_resultado)  
        session['ruta']=app.config["UPLOAD_FOLDER"] +'/resultados/'+ session['correo']
        session['ar']=dir+'calculo.csv'    
        return redirect(url_for('verResultadoDataFrame'))


#ruta para mostrar formulario de subir imagen
@app.route("/upload", methods=["GET","POST"])
def upload():
    if request.method == "POST":
        f = request.files["ourfile"] #ourfile es el name del formulario
        filename = f.filename #se escoge el nombre del archivo
        #print(filename)
        global rutas
        filename = funciones.agregarArchivoLista(rutas,filename)
        rutas.append(filename)
        print(rutas)
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename)) 
        #return "Your file has been uploaded " + filename
        flash('El código se subio correctamente')
        #return redirect(url_for("get_file", filename=filename))
        

    
    directorios = os.listdir(app.config["UPLOAD_FOLDER"] +'/'+session['correo'])
    return render_template('formularioArchivo.html',directorios=directorios,ruta=app.config["UPLOAD_FOLDER"] +'/'+session['correo'])

#metodo para ver archivos teniendo la ruta y directorio
@app.route("/archivos/<dir>")
def archivos(dir):
    try:
        ruta=app.config["UPLOAD_FOLDER"] +'/'+session['correo']
        url=ruta+'/'+dir
        archivos=os.listdir(url)
        return render_template('verArchivos.html',dir=dir,archivos=archivos)
    except Exception as e:
        flash('Se ha producido un error inténtelo de nuevo')
        return redirect(url_for('index'))

#metodo para ver archivos teniendo la ruta y directorio
@app.route("/resultados")
def resultados():
    try:
        ruta=app.config["UPLOAD_FOLDER"] +'/resultados/'+session['correo']
        archivos=os.listdir(ruta)
        return render_template('verResultados.html',ruta=ruta,archivos=archivos)
    except Exception as e:
        flash('Se ha producido un error inténtelo de nuevo')
        return redirect(url_for('index'))

#metodo para eliminar archivo de proyecto
@app.route("/eliminarArchivoResultado", methods=['POST'])
def eliminarArchivoResultado():
    try:
        if(request.method=="POST"):
            ruta=request.form['dir']
            ar=request.form['ar']
            url=ruta+'/'+ar
            os.remove(url)
            return redirect('/resultados')
    except Exception as e:
        flash('Se ha producido un error inténtelo de nuevo')
        return redirect(url_for('index'))
    
#descargar archivo de resultado
@app.route('/download',methods=['POST'])
def download():
    try:
        if(request.method=="POST"):
            ruta=request.form['dir']
            ar=request.form['ar']
            url=ruta+'/'+ar
            print(url)
            return send_file(url,as_attachment=True)
    except Exception as e:
        flash('Se ha producido un error inténtelo de nuevo')
        return redirect(url_for('index'))

#mostrar en dataframe
@app.route("/verResultadoDataFrame", methods=['POST','GET'])
def verResultadoDataFrame():
    try:
        if(request.method=="POST"):
            ruta=request.form['dir']
            session['ruta']=ruta
            ar=request.form['ar']
            session['ar']=ar
            url=ruta+'/'+ar
            df = pd.read_csv(url)   
            lista = df.values.tolist()
            funciones2.pasarResultadosC(lista)
            encabezado = list(df.columns)
            encabezado2 = funciones2.crearEncabezadoMatrizSimilitud(encabezado)

            porciento=70
            listaPor=funciones2.archivosFiltrados(df,porciento)
            return render_template('resultadosDF.html', porciento=porciento,listaPor=listaPor,matriz=lista, encabezado=encabezado, encabezado2=encabezado2)
        
        if(request.method=="GET"):
            ruta=session['ruta']
            ar=session['ar']
            url=ruta+'/'+ar
            df = pd.read_csv(url)   
            lista = df.values.tolist()
            funciones2.pasarResultadosC(lista)
            encabezado = list(df.columns)
            encabezado2 = funciones2.crearEncabezadoMatrizSimilitud(encabezado)
            porciento=70
            listaPor=funciones2.archivosFiltrados(df,porciento)
            return render_template('resultadosDF.html', porciento=porciento,listaPor=listaPor,matriz=lista, encabezado=encabezado, encabezado2=encabezado2)


    except Exception as e:
        flash('Se ha producido un error inténtelo de nuevo')
        return redirect(url_for('index'))

#mostrar en dataframe
@app.route("/filtroSimilitud", methods=['POST','GET'])
def filtroSimilitud():
    try:
        if(request.method=="POST"):
            ruta=session['ruta']
            ar=session['ar']
            url=ruta+'/'+ar
            df = pd.read_csv(url)   
            lista = df.values.tolist()
            funciones2.pasarResultadosC(lista)
            encabezado = list(df.columns)
            encabezado2 = funciones2.crearEncabezadoMatrizSimilitud(encabezado)
            porciento=int(request.form['por'])
            listaPor=funciones2.archivosFiltrados(df,porciento)
            print(listaPor)
            return render_template('resultadosDF.html', porciento=porciento,listaPor=listaPor,matriz=lista, encabezado=encabezado, encabezado2=encabezado2)
        
        if(request.method=="GET"):
            ruta=session['ruta']
            ar=session['ar']
            url=ruta+'/'+ar
            df = pd.read_csv(url)   
            lista = df.values.tolist()
            funciones2.pasarResultadosC(lista)
            encabezado = list(df.columns)
            encabezado2 = funciones2.crearEncabezadoMatrizSimilitud(encabezado)
            porciento=70
            listaPor=funciones2.archivosFiltrados(df,porciento)
            return render_template('resultadosDF.html', porciento=porciento,listaPor=listaPor,matriz=lista, encabezado=encabezado, encabezado2=encabezado2)


    except Exception as e:
        flash('Se ha producido un error inténtelo de nuevo')
        return redirect(url_for('index'))


#metodo para eliminar directorio
@app.route("/eliminarDirectorio", methods=['POST'])
def eliminarDirectorio():
    try:
        if(request.method=="POST"):
            ruta=request.form['ruta']
            dir=request.form['dir']
            rmtree(ruta+'/'+dir)
            return redirect(url_for('upload'))
    except Exception as e:
        flash('Se ha producido un error inténtelo de nuevo')
        return redirect(url_for('index'))
    
#metodo para eliminar archivo de proyecto
@app.route("/eliminarArchivo", methods=['POST'])
def eliminarArchivo():
    try:
        if(request.method=="POST"):
            dir=request.form['dir']
            ar=request.form['ar']
            ruta=app.config["UPLOAD_FOLDER"] +'/'+session['correo']
            url=ruta+'/'+dir
            os.remove(url+'/'+ar)
            return redirect('/archivos/'+dir)
    except Exception as e:
        flash('Se ha producido un error inténtelo de nuevo')
        return redirect(url_for('index'))

#SUBIR ARCHIVOS 
@app.route('/subirArchivos', methods=['POST'])
def subir():
    #crear cursor para ejecucion
    conn= mysql.connect()
    cursor= conn.cursor()
    try:
        
        if(request.method=="POST"):
            files = request.files.getlist("myfiles")
            nombreProyecto = request.form['nombreProyecto'];
            
            #preparar el query para inserccion 
            sql = ("SELECT DIRECTORIO.NOMBRE "
                   "FROM USUARIO, DIRECTORIO "
                   "WHERE USUARIO.id = DIRECTORIO.id "
                   "AND correo=%s AND DIRECTORIO.NOMBRE=%s;")
            print(sql)
            #ejecuta la sentencia
            cursor.execute(sql,(session['correo'],nombreProyecto))
            #Obtengo el dato 
            dir = cursor.fetchone()
            print(dir)

            sql = ("SELECT id FROM USUARIO WHERE correo=%s")
            cursor.execute(sql,(session['correo']))
            id = cursor.fetchone()
            print(id)
            
            #se agrega directorio a la base de datos 
            if(dir == None):
                #preparar el query para inserccion 
                sql = ("INSERT INTO DIRECTORIO (id,nombre) VALUES (" 
                       "%s,%s);")
                cursor.execute(sql,(id,nombreProyecto))
            
            #obtener id del directorio
            sql = "SELECT id_dir FROM DIRECTORIO WHERE id=%s AND nombre=%s"
            cursor.execute(sql,(id,nombreProyecto))
            id_dir = cursor.fetchone()


            for file in files: 
                print(file.filename) 
                sql = "INSERT INTO ARCHIVO(ID_DIR,NOMBRE_ARCHIVO) VALUES(%s,%s)"
                cursor.execute(sql,(id_dir,file.filename))          
                #si existe la carpeta no se crea la carpeta
                if (os.path.exists(app.config["UPLOAD_FOLDER"]+'/'+session['correo']+'/'+nombreProyecto) == False): 
                    os.mkdir(path=app.config["UPLOAD_FOLDER"] +'/'+session['correo']+'/'+nombreProyecto)
                    file.save(os.path.join(app.config["UPLOAD_FOLDER"],session['correo'],nombreProyecto,file.filename))
                else:
                     file.save(os.path.join(app.config["UPLOAD_FOLDER"],session['correo'],nombreProyecto,file.filename))
            
            #ejecuta el commit
            conn.commit()
            conn.close()

            

            return redirect(url_for('upload'))
    except Exception as e:
        #ejecuta el commit
        conn.commit()
        conn.close()
        return redirect(url_for('upload')) 

@app.route('/gestionArchivos')
def gestionArchivos():
    directorios = os.listdir(app.config["UPLOAD_FOLDER"] +'/'+session['correo'])
    print(directorios)
    #se envia informacion de empleados
    return render_template('archivos.html', directorios=directorios)


@app.route("/delete/<nombre_archivo>")
def delete(nombre_archivo):
  global rutas
  rutas.remove(nombre_archivo)
  remove("../uploads/"+nombre_archivo)
  flash('Documento Eliminado')
  return redirect(url_for('eliminar'))




@app.route("/eliminar")
def eliminar():
  global rutas

  return render_template('eliminar.html', ubicaciones = rutas[1:])




#parte de subir codigo
@app.route("/uploadCodigo",methods=['GET','POST'])
def uploadCodigo():
    if request.method == "POST":
        textCodigo = request.form["codigo"]
        #print(textCodigo)
        mns = escribirArchivo(textCodigo)   
        flash(mns)      
        return render_template('formularioCodigo.html')
        
       
    return render_template('formularioCodigo.html')


#metodo para escribir archivo
def escribirArchivo(texto):      
    global rutas
    ruta = "../uploads/"
    nombreA = 'archivo'+'.txt'
    nombreA = funciones.agregarArchivoLista(rutas,nombreA)
    nombreArchivo = ruta + nombreA     
    escritura = open(nombreArchivo,'w')
    escritura.write(texto)
    escritura.close()     
    rutas.append(nombreA)
    return "Archivo: "+str(nombreA)+" escrito"


if __name__ == '__main__':
    app.run(port = 5000, debug = True)