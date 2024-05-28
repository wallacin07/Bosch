public class Rabugento extends Individuo{
        
    Rabugento(String name){
        super(name);
    }

    private boolean enganado = false;


    @Override
    protected void jogar(Boolean jogadaAdversario) {
        if (enganado == true) {
            trapacear();
        }
        else
        enganado = !jogadaAdversario;
        colaborar();
        
    }

}