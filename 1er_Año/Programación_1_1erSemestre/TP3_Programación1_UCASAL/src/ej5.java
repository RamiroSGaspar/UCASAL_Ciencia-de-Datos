import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ej5 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Ingrese la nota del examen:");
        int nota = Integer.parseInt(br.readLine());
        if (nota >= 7 && nota <= 10) {
            System.out.println("Promocionado");
        } else if (nota >= 4 && nota <= 6) {
            System.out.println("Regular");
        } else if (nota >= 0 && nota <= 3) {
            System.out.println("Libre");
        } else {
            System.out.println("Nota inválida");
        }
    }
}