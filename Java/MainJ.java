package Java;
import java.util.Scanner;

public class MainJ {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        System.out.println("Your age is: " + age);
        scanner.close();
    }
}