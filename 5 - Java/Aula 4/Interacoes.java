public class Interacoes {
    public void rodada(Individuo um, Individuo dois)
    {

        if (um.colaborar() && dois.colaborar()) {
            um.adicionarMoeda(2);
            dois.adicionarMoeda(2);
        }
        else if(um.colaborar() && dois.trapacear())
        {
            um.adicionarMoeda(-1);
            dois.adicionarMoeda(+3);
        }
        else if(um.trapacear() && dois.colaborar())
        {
            um.adicionarMoeda(+3);
            dois.adicionarMoeda(-1);
        }
        else if(um.trapacear()&& dois.trapacear())
        {
            um.adicionarMoeda(0);
            dois.adicionarMoeda(0);            
        }
    }

    public void finalRodada(Individuo um, Individuo dois)
    {
        um.adicionarMoeda(-1);
        dois.adicionarMoeda(-1);
    }
}
