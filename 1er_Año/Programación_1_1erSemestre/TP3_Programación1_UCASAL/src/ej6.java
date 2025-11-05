import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ej6 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Ingrese nombre de usuario:");
        String usuario = br.readLine();
        System.out.println("Ingrese contraseña:");
        String clave = br.readLine();

        if (usuario.equals("Franco") && clave.equals("2022")) {
            System.out.println("Bienvenido Franco! Inicio de sesión válido!");
        } else if (!usuario.equals("Franco")) {
            System.out.println("Nombre de usuario incorrecto, no se puede iniciar sesión!");
        } else if (!clave.equals("2022")) {
            System.out.println("Contraseña incorrecta, no se puede iniciar sesión!");
        } else {
            System.out.println("Usuario totalmente desconocido! Fuera hacker!!");
        }
    }
}