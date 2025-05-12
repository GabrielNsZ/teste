public class Pizza {
    private String sabor;
    private double preco;

    public Pizza(String sabor, double preco) {
        this.sabor = sabor;
        this.preco = preco;
    }

    public String getSabor() {
        return sabor;
    }

    public double getPreco() {
        return preco;
    }

    @Override
    public String toString() {
        return sabor + " - R$" + String.format("%.2f", preco);
    }
}