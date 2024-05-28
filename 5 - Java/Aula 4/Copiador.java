public class Copiador extends Individuo {
    Copiador(String name){
        super(name);
    }
    private Boolean jogadaAntigaAdversario = true;

    @Override
    protected void jogar(Boolean jogadaAdversario) {
        if (jogadaAntigaAdversario == true) {
            jogadaAntigaAdversario = jogadaAdversario;
            colaborar();
        }
        else
        trapacear();
        
    }

    

    

}