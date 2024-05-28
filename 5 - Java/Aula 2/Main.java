import java.util.Scanner;
public class Main {
    
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String CPF;
        String Senha;
        Lista lista = new Lista();
        
        Empregados Admin = new Empregados("Admin", "123", "123", "03/05/2024", true);

        lista.add(Admin);


        System.out.println("Bem vindo ao sistema ponto.\nLogue com seu usuario no sistema digitando seu CPF e senha\n");
        System.out.println("CPF: ");
        CPF = scanner.nextLine();
        System.out.println("Senha: ");
        Senha = scanner.nextLine();
        if (CPF == Admin.getCpf() && Senha == Admin.getSenha() && Admin.getAdministrador() == true) 
        {
            System.out.println("bem vindo Administrador\nO que deseja fazer?\n[1] Adicionar um empregado ao sistema\n[2] Procurar um usuario no sistema\n[3] Verificar quantos usuarios existem nos sistemas");
        }


        scanner.close();
    }

    
}
