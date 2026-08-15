print(f'''
            {"="*40}
            {"Loja Python SA":^40}
            {"Rua dos códigos":^40}
            {"="*40}

            Cliente: {input("Nome do Cliente: ")}
            CPF: {input("CPF do Cliente: ")}
            {"-"*40}
            {"ITEM":<20} {"QTD.":<5} {"PREÇO":<15}
            {input("Produto 1: "):.<20} {input("Quantidade: "):<5} R$ {input("Preço: "):<12}
            {"-"*40}
            SUBTOTAL: {"R$":>19} {input("Total: ")}
            IMPOSTO (10%): {"R$ A calcular":>25}
            {"="*40}
            {"OBRIGADO PELA PREFERÊNCIA":^40}
            {"="*40}
      ''')