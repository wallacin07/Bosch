
import java.time.LocalDate;
import java.time.LocalTime;

public class Ponto {
    

    private LocalDate today; // Declara a variável de instância
    private LocalTime now;
    private int hora;
    private int minuto;
    private int dia;
    private int mes;
    private int ano;
    private String cpfEmpregado;



    // Metodo Construtor
    public Ponto(String cpf) {
        today = LocalDate.now(); // Inicializa a variável de instância
        now = LocalTime.now();


        hora = now.getHour();
        minuto = now.getMinute();
        dia = today.getDayOfMonth();
        mes = today.getMonthValue();
        ano = today.getYear();
        this.cpfEmpregado = cpf;
    }

    public int getHora() {
        return hora;
    }

    public void setHora(int hora) {
        this.hora = hora;
    }

    public int getMinuto() {
        return minuto;
    }

    public void setMinuto(int minuto) {
        this.minuto = minuto;
    }

    public int getDia() {
        return dia;
    }

    public void setDia(int dia) {
        this.dia = dia;
    }

    public int getMes() {
        return mes;
    }

    public void setMes(int mes) {
        this.mes = mes;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }
}

