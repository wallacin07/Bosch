public class Individuo {
    protected Integer moeda = 10;
    protected String nome;

    Individuo(String nameString){
        this.nome = nameString;
    };

    protected String nome(String nome)
    {
        this.nome = nome;
        return this.nome;
    }

    protected Boolean colaborar() {
        return true;
    }

    protected Boolean trapacear()
    {
        return false;
    }

    protected void jogar(Boolean jogadaAdversario)
    {}

    void adicionarMoeda(Integer moeda)
    {
        this.moeda += moeda;
    }
}
