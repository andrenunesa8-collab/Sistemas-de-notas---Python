# =============================================================
# SISTEMAS DE NOTAS - PARADIGMA ESTRUTURADO
# Uso de funções, estruturas de controle e modularização
# =============================================================

def ler_alunos(n):
    """Lê nome e notas de n alunos e retorna uma lista de dicionario"""
    alunos  =[]
    for i in range(1, n + 1):
        print(f"\n--- Aluno {i} ---")
        nome = input("Nome: ").strip()
        notas = []
        for j in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Nota {j} (0-10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    print(" Nota deve estar entre 0 e 10.")
                except ValueError:
                    print(" Digite um número válido.")
        alunos.append({"nome": nome, "notas": notas})
    return alunos


def calcular_media(notas):
    """Retorna a média aritmética de uma lista de notas."""
    return sum(notas) / len(notas)


def determinar_situaçao(media):
    """Retorna 'Aprovado' se média >= 6, caso contrário 'Reprovado'. """
    return "Aprovado" if media >= 6 else "Reprovado"


def processar_alunos(alunos):
    """Adicionar média e situação a cada aluno."""
    for aluno in alunos:
        aluno["média"] = calcular_media(aluno["notas"])
        aluno["situaçao"] = determinar_situaçao(aluno["média"])
    return alunos


def ordenar_alunos(alunos):
    """Retorna lista ordernada por média (descrescente). """
    return sorted(alunos, key=lambda a: a["média"], reverse=True)


def exibir_listagem(alunos):
    """Exibe a tabela de resultados individuais."""
    print("\n" + "=" * 60)
    print(f"{'ALUNOS': <25} {'MÈDIA': >6} {'SITUAÇÂO'}")
    print("-" * 60)
    for aluno in alunos:
        print(f"{aluno['nome']:<25} {aluno['média']:>6.2f}  {aluno['situaçao']}")
        print("=" * 60)


def calcular_estatisticas(alunos):
    """Calcular e exibe média geral, maior e menor nota da turma."""
    todas_as_notas = [n for a in alunos for n in a["notas"]]
    media_geral    = sum(a["média"] for a in alunos) / len(alunos)
    maior_nota     = max(todas_as_notas)
    menor_nota     = min(todas_as_notas)

    print("\n ESTATISTICAS DA TURMA")
    print(f" Média geral : {media_geral:.2f}")
    print(f" Maior nota  : {maior_nota:.2f}")
    print(f" Menor nota  : {menor_nota:.2f}")
    print("=" * 60)


def main():
    print("=" * 40)
    print("SITESMAS DE NOTAS - ALUNOS")
    print("=" * 40)

    while True:
        try:
            n = int(input("\nQuantos alunos deseja cadastrar? "))
            if n > 0:
                break
            print(" DIgite um número maior que zero.")
        except ValueError:
            print("Valor inválido.")

    alunos     = ler_alunos(n)
    alunos     = processar_alunos(alunos)
    ordenados  = ordenar_alunos(alunos)

    exibir_listagem(ordenados)
    calcular_estatisticas(alunos)


if __name__ == "__main__":
    main()






