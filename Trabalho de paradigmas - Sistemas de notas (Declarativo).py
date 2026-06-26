# ============================================================
#  SISTEMA DE NOTAS — PARADIGMA DECLARATIVO / FUNCIONAL
#  Uso de funções puras, map, filter, lambda, reduce
# ============================================================

from functools import reduce

# - Função puras (sem efeitod colaterais) -----------

media       = lambda notas: reduce(lambda acc, n: acc + n, notas) / len(notas)
situacao    = lambda m: "Aprovado" if m >= 6 else "Reprovado"
enriquecer  = lambda aluno: {**aluno,
                             "media":   media(aluno["notas"]),
                             "situacao": situacao(media(aluno["notas"]))}
ordenar     = lambda alunos: sorted(alunos, key=lambda a: a["media"], reverse=True)

todas_notas = lambda alunos: [n for a in alunos for n in a ["notas"]]
media_geral = lambda alunos: media(list(map(lambda a: a["media"], alunos)))
maior_nota  = lambda alunos: reduce(lambda acc, n: n if n > acc else acc, todas_notas(alunos))
menor_nota  = lambda alunos: reduce(lambda acc, n: n if n < acc else acc, todas_notas(alunos))

# ----- Entrada de dados -----------------------------------------

def ler_nota(j):
    while True:
        try:
            n = float(input(f" Nota {j} (0-10): "))
            if 0 <= n <= 10:
                return n
            print(" Nota deve estar entre 0 a 10.")
        except ValueError:
            print(" Digite um número válido.")



def ler_aluno(i):
    print(f"\n--- Aluno {i} ---")
    return {
        "nome": input("Nome: ").strip(),
        "notas": list(map(ler_nota, range(1, 4)))  # map aplica ler_nota para [1, 2, 3]
    }


def ler_quantidade():
    while True:
        try:
            n = int(input("\nQuantos alunos deseja cadastrar? "))
            if n > 0:
                 return n
            print("Digite um número maior que zero.")
        except ValueError:
             print("Valor inválido.")



# --- Saída de dados (único lugar com efeitodd colaterais) ------

def exibir_listagem(alunos):
    print("\n" + "=" * 60)
    print(f"{'ALUNO':<25} {'MÈDIA':>6} {'SITUAÇÂO'}")
    print("=" * 60)
    list(map(
        lambda a: print(f"{a['nome']:<25} {a['media']:>6.2f} {a['situacao']}"),alunos

    ))
    print("=" * 60)


def exibir_estatisticas(alunos):
    print("\n ESTATÌSTICAS DA TURMA")
    print(f" Média geral : {media_geral(alunos):.2f}")
    print(f" Maior nota  : {maior_nota(alunos):.2f}")
    print(f" Menor nota  : {menor_nota(alunos):.2f}")
    print("=" * 40)

# ------ Pipeline principal -----------------------------------

def main():
    print("="*40)
    print("SISTEMAS DE NOTAS - ALUNOS")
    print("="*40)

    n = ler_quantidade()

    # Pipeline declarativo: leitura -> enriquecimento -> ordenação
    alunos = ordenar(
        list(map(enriquecer,
                 map(ler_aluno, range(1, n + 1))))
    )

    exibir_listagem(alunos)
    exibir_estatisticas(alunos)


if __name__ == "__main__":
    main()
