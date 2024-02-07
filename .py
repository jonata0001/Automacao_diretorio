import os
from tkinter.filedialog import askdirectory

pasta_origem =askdirectory(title="pasta origem")
print(pasta_origem)
pasta_destino =askdirectory(title="pasta detino")

regras_arquivos ={
    "jan":"janeiro",
    "fev":"fevereiro",
    "mar":"março",

}

lista_arquivos=os.listdir(pasta_origem)

for nome_arquivo in lista_arquivos:
    for chave in regras_arquivos.keys():
      if chave in nome_arquivo:
         nova_pasta = regras_arquivos[chave]
         nome_completo =os.path.join(pasta_origem,nome_arquivo)
         nome_final=os.path.join(pasta_destino,nova_pasta,nome_arquivo)

         caminho_nova_pasta = os.path.join(pasta_destino,nova_pasta)
         if not os.path.exists(caminho_nova_pasta):
          os.mkdir(caminho_nova_pasta)
         os.rename(nome_completo,nome_final)
         
