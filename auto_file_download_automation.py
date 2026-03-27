#Automatização Baixa Arquivos
    
import time

# LOGIN 
print('REALIZANDO LOGIN')
with open("LoginMannesoftPrime.py") as login:
    exec(login.read())
    #time.sleep(0.2)

# ALUNOS
print('ATUALIZA ALUNOS MATRICULADOS')
with open("alunos_matriculados.py") as alunos:
    exec(alunos.read())
    #time.sleep(0.2)


### ### ### ### ### ### ### ### ### ### ### ### ### ### ### MATRICULA

# Matricula POR DOC
print('BAIXAS MATRICULA POR DOC')
with open("BaixasMatTodos.py") as mat_doc:
    exec(mat_doc.read())
    #time.sleep(0.2)

# Matricula Sintetico
print('BAIXAS MATRICULA SINTETICO')
with open("BaixasMatTodosSintetico.py") as mat_sintetico:
    exec(mat_sintetico.read())
    #time.sleep(0.2)

# Matricula TITULOS EMITIDOS
print('BAIXAS TITULOS EMITIDOS MATRICULA')
with open("BaixasMatTituEmit.py") as mat_titulos_emitidos:
    exec(mat_titulos_emitidos.read())
    #time.sleep(0.2)


### ### ### ### ### ### ### ### ### ### ### ### ### ### ### MENSALIDADE


# MENSALIDADE POR DOC
print('BAIXAS MENSALIDADE POR DOC')
with open("BaixasMensaTodos.py") as mensa_doc:
    exec(mensa_doc.read())
    #time.sleep(0.2)

# MENSALIDADE Sintetico
print('BAIXAS MENSALIDADE SINTETICO')
with open("BaixasMensaTodosSintetico.py") as mensa_sintetico:
    exec(mensa_sintetico.read())
    #time.sleep(0.2)

# MENSALIDADE TITULOS EMITIDOS
print('BAIXAS TITULOS EMITIDOS MENSALIDADE')
with open("BaixasMensaTituEmit.py") as mensa_titulos_emitidos:
    exec(mensa_titulos_emitidos.read())
    #time.sleep(0.2)
