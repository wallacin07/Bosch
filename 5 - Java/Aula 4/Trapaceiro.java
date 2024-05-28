public class Trapaceiro  extends Individuo{
    Trapaceiro(String name){
        super(name);
    }

@Override
protected void jogar(Boolean jogadaAdversario) {
    trapacear();
}

}


