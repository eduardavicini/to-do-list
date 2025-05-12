import json
import os
from datetime import datetime

ARQUIVO = "tarefas_diarias1.json"

# Carregar tarefas salvas
def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Salvar tarefas
def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

# Adicionar tarefa
def adicionar_tarefa(tarefas):
    print("\n✨ Nova tarefa chegando!")
    descricao = input("📝 O que você quer fazer? ").strip()
    categoria = input("📌 Categoria (ex: Estudo, Lazer, Vida pessoal): ").strip()
    data = datetime.now().strftime("%d/%m/%Y")

    tarefas.append({
        "descricao": descricao,
        "categoria": categoria,
        "concluida": False,
        "data": data
    })
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada com sucesso!")

# Mostrar tarefas de hoje
def listar_tarefas(tarefas):
    hoje = datetime.now().strftime("%d/%m/%Y")
    tarefas_hoje = [t for t in tarefas if t["data"] == hoje]

    print(f"\n📅 Sua lista para hoje ({hoje}):")

    if not tarefas_hoje:
        print("🚀 Nada por aqui. Aproveite seu dia!")
        return

    for i, t in enumerate(tarefas_hoje):
        status = "✅" if t["concluida"] else "⬜"
        print(f"{i+1}. {status} {t['descricao']} [{t['categoria']}]")

# Marcar tarefa como concluída
def concluir_tarefa(tarefas):
    hoje = datetime.now().strftime("%d/%m/%Y")
    tarefas_hoje = [t for t in tarefas if t["data"] == hoje]
    listar_tarefas(tarefas)

    try:
        idx = int(input("🎯 Número da tarefa que você concluiu: ")) - 1
        if 0 <= idx < len(tarefas_hoje):
            tarefa_idx = tarefas.index(tarefas_hoje[idx])
            tarefas[tarefa_idx]["concluida"] = True
            salvar_tarefas(tarefas)
            print("🎉 Boa! Tarefa concluída!")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("❌ Ops! Digite um número.")

# Remover tarefa
def remover_tarefa(tarefas):
    hoje = datetime.now().strftime("%d/%m/%Y")
    tarefas_hoje = [t for t in tarefas if t["data"] == hoje]
    listar_tarefas(tarefas)

    try:
        idx = int(input("🗑️ Qual tarefa deseja deletar? (número): ")) - 1
        if 0 <= idx < len(tarefas_hoje):
            tarefa_idx = tarefas.index(tarefas_hoje[idx])
            removida = tarefas.pop(tarefa_idx)
            salvar_tarefas(tarefas)
            print(f"🧹 Tarefa removida: {removida['descricao']}")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("❌ Isso não é um número.")

# Menu interativo
def exibir_menu():
    print("\n🌟 ORGANIZE SEU DIA 🌟")
    print("1️⃣ Adicionar tarefa")
    print("2️⃣ Ver tarefas de hoje")
    print("3️⃣ Marcar como concluída")
    print("4️⃣ Remover tarefa")
    print("5️⃣ Sair 🚪")

# Início do programa
def boas_vindas():
    nome = os.getenv("USERNAME") or os.getenv("USER") or "você"
    print("\n==============================")
    print(f"✨ Bem-vindo(a), {nome}! ✨")
    print("Pronta pra organizar seu dia com estilo? 😍")
    print("==============================")

def main():
    tarefas = carregar_tarefas()
    boas_vindas()

    while True:
        exibir_menu()
        escolha = input("\n👉 Escolha uma opção: ").strip()

        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            concluir_tarefa(tarefas)
        elif escolha == "4":
            remover_tarefa(tarefas)
        elif escolha == "5":
            print("\n🚀 Até logo! Que seu dia seja produtivo 💡")
            break
        else:
            print("🤔 Opção inválida. Tenta de novo!")

if __name__ == "__main__":
    main()



