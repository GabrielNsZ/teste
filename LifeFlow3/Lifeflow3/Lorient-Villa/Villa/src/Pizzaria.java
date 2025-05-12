import java.util.ArrayList;
import java.util.List;

public class Pizzaria {
    private List<Pedido> pedidos;

    public Pizzaria() {
        pedidos = new ArrayList<>();
    }

    public void fazerPedido(Pedido pedido) {
        pedidos.add(pedido);
    }

    public void listarPedidos() {
        if (pedidos.isEmpty()) {
            System.out.println("Nenhum pedido feito ainda.");
        } else {
            for (Pedido p : pedidos) {
                System.out.println(p);
            }
        }
    }
}
