

public class Empregados {
    private String nome;
    private String cpf;
    private String senha;
    private String dataDeNascimento;
    private Boolean Administrador;
    
    public Empregados(String nome, String cpf, String senha, String dataDeString, boolean Administrador){
        this.nome = nome;
        this.cpf = cpf;
        this.senha = senha;
        this.dataDeNascimento = dataDeString;
        this.Administrador = Administrador;        
        
    }

    public String getNome() {
        return nome;
    }
    
    
    public void setNome(String nome) {
        this.nome = nome;
    }
    
    String getCpf()
    {
        return cpf;
    }
    
    public void setCpf(String cpf) {
        this.cpf = cpf;
    }


    public String getSenha() {
        return senha;
    }


    public void setSenha(String senha) {
        this.senha = senha;
    }


    public String getDataDeNascimento() {
        return dataDeNascimento;
    }


    public void setDataDeNascimento(String dataDeNascimento) {
        this.dataDeNascimento = dataDeNascimento;
    }


    public Boolean getAdministrador() {
        return Administrador;
    }


    public void setAdministrador(Boolean administrador) {
        Administrador = administrador;
    }
}

