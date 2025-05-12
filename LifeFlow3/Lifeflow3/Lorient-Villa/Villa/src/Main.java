import java.util.Scanner;

public class Main {
    // Menu de sabores pré-definidos
    private static final Pizza[] CARDAPIO = {
        new Pizza("Margherita", 45.0),
        new Pizza("Calabresa", 50.0),
        new Pizza("Portuguesa", 55.0),
        new Pizza("Frango com Catupiry", 60.0),
        new Pizza("Quatro Queijos", 65.0),
        new Pizza("Pepperoni", 60.0)
    };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Pizzaria pizzaria = new Pizzaria();

        while (true) {
            System.out.println("\n--- MENU PIZZARIA ---");
            System.out.println("1. Fazer novo pedido");
            System.out.println("2. Listar pedidos");
            System.out.println("3. Sair");
            System.out.print("Escolha uma opção: ");
            int opcao = scanner.nextInt();
            scanner.nextLine(); // limpa buffer

            switch (opcao) {
                case 1:
                    System.out.print("Nome do cliente: ");
                    String nome = scanner.nextLine();
                    System.out.print("Telefone: ");
                    String telefone = scanner.nextLine();
                    System.out.print("Endereço: ");
                    String endereco = scanner.nextLine();

                    Cliente cliente = new Cliente(nome, telefone, endereco);

                    System.out.println("Formas de pagamento: 1 - Dinheiro | 2 - Cartão | 3 - Pix");
                    int pg = scanner.nextInt();
                    scanner.nextLine();
                    FormaPagamento forma = FormaPagamento.values()[pg - 1];

                    Pedido pedido = new Pedido(cliente, forma);

                    while (true) {
                        System.out.println("\n--- CARDÁPIO ---");
                        for (int i = 0; i < CARDAPIO.length; i++) {
                            System.out.printf("%d. %s\n", i+1, CARDAPIO[i]);
                        }
                        System.out.println("0. Finalizar pedido");
                        System.out.print("Escolha uma pizza: ");
                        int escolha = scanner.nextInt();
                        scanner.nextLine();
                        
                        if (escolha == 0) {
                            break;
                        }
                        if (escolha < 0 || escolha > CARDAPIO.length) {
                            System.out.println("Opção inválida!");
                            continue;
                        }
                        
                        Pizza pizzaEscolhida = CARDAPIO[escolha - 1];
                        pedido.adicionarPizza(pizzaEscolhida);
                        System.out.printf("✅ %s adicionada ao pedido!\n", pizzaEscolhida.getSabor());
                    }

                    pizzaria.fazerPedido(pedido);
                    System.out.println("✅ Pedido realizado com sucesso!");
                    break;

                case 2:
                    pizzaria.listarPedidos();
                    break;

                case 3:
                    System.out.println("Saindo da pizzaria... 🍕");
                    scanner.close();
                    return;

                default:
                    System.out.println("Opção inválida.");
            }
        }
    }
}