import tkinter as tk

janela = tk.Tk()
janela.title("Busca de Equipamentos")
janela.geometry("800x600") # Define o tamanho da janela (800x600) e a posição (300, 100)
janela.resizable(False, False)
janela.configure(bg="#1e1e1e")
janela.grid_columnconfigure(0, weight=1)  # Permite que a coluna 0 se expanda para preencher o espaço disponível

# Criar o título
titulo = tk.Label(
    janela, 
    text="Busca de Equipamentos", 
    font=("Arial", 24, "bold"), 
    fg="white", 
    bg="#1e1e1e"
)
titulo.grid(row=0, column=0, padx=20, pady=20)


# Criar o campo de entrada
entrada = tk.Entry(janela, width=20, font=("Arial", 14))
entrada.grid(row=1, column=0, padx=20, pady=20)

# Criar o botão de busca
def clicar():
    entrada.get()
    buscar = entrada.get().strip()
    print(buscar)
    entrada.delete(0, tk.END)
    
botao = tk.Button(
    janela, 
    text="Buscar",
    width=20,
    height=2,
    bg="blue",
    fg="white",
    command=clicar,
)

botao.grid(row=2, column=0, padx=20, pady=20)

# Criar o campo de resultado
resultado = tk.Text(janela, width=50, height=10, font=("Arial", 12))
resultado.grid(row=3, column=0, padx=20, pady=20)

janela.mainloop()



