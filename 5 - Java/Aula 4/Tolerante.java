public class Tolerante extends Individuo {
        Tolerante(String name){
            super(name);
        }
    private Integer enganado = 0;

@Override
protected void jogar(Boolean jogadaAdversario) {
    if (enganado == 3) {

            trapacear();
            
        }
        else{
        if (jogadaAdversario == false) {
            enganado++;
        }
        colaborar();
    }
    
}

public void setEnganado(Integer enganado) {
    this.enganado = enganado;
}



}

    
    
