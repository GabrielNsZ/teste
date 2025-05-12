import java.util.ArrayList;
import java.util.List;

public class Pedido {
    private Cliente cliente;
    private List<Pizza> pizzas;
    private PedidoStatus status;
    private FormaPagamento pagamento;

    public Pedido(Cliente cliente, FormaPagamento pagamento) {
        this.cliente = cliente;
        this.pizzas = new ArrayList<>();
        this.status = PedidoStatus.EM_PREPARO;
        this.pagamento = pagamento;
    }

    public void adicionarPizza(Pizza pizza) {
        pizzas.add(pizza);
    }

    public double calcularTotal() {
        double total = 0;
        for (Pizza p : pizzas) {
            total += p.getPreco();
        }
        return total;
    }

    public void atualizarStatus(PedidoStatus status) {
        this.status = status;
    }

    public PedidoStatus getStatus() {
        return status;
    }

    @Override
    public String toString() {
        return "Pedido de " + cliente + 
               "\nPizzas: " + pizzas + 
               "\nTotal: R$" + calcularTotal() +
               "\nPagamento: " + pagamento +
               "\nStatus: " + status + "\n";
    }
}
