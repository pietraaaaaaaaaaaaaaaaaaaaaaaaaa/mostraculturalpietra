def analisar_vendas(vendas):
    """Função para processar e analisar os dados de vendas."""
    if not vendas:
        print("Nenhum dado de venda fornecido.")
        return

    total_faturado = sum(vendas.values())
    qtd_produtos = len(vendas)
    ticket_medio = total_faturado / qtd_produtos

    # Encontra o produto mais vendido e o menos vendido
    produto_top = max(vendas, key=vendas.get)
    produto_baixo = min(vendas, key=vendas.get)

    # Exibição dos resultados no terminal
    print("=" * 40)
    print("      RELATÓRIO DE DESEMPENHO      ")
    print("=" * 40)
    print(f"Quantidade de produtos: {qtd_produtos}")
    print(f"Faturamento Total:     R$ {total_faturado:,.2f}")
    print(f"Ticket Médio por item:  R$ {ticket_medio:,.2f}")
    print("-" * 40)
    print(f"🏆 Produto Destaque:   {produto_top} (R$ {vendas[produto_top]:,.2f})")
    print(f"📉 Pior Desempenho:    {produto_baixo} (R$ {vendas[produto_baixo]:,.2f})")
    print("=" * 40)


# Dicionário de dados simulando as vendas do mês
dados_vendas = {
    "Curso de Python": 15000.00,
    "Curso de Web Design": 8900.50,
    "E-book de Lógica": 2450.00,
    "Mentoria Tech": 22000.00,
    "Curso de Banco de Dados": 11200.00,
}

# Execução do script
if __name__ == "__main__":
    analisar_vendas(dados_vendas)
