// api_service.java
// Basic Java API to serve triage predictions using a pre-trained model exposed through a REST-like interface.
// This is a mock representation. Actual integration would use Spring Boot for production.

import java.util.Scanner;

public class api_service {

    // Simulate a model's decision logic (normally you would call Python model or use ONNX Java runtime)
    public static String predictTriage(int age, int bp, int hr, int symptomCode) {
        // Dummy logic for simulation: urgent if heart rate > 120 or bp < 90
        if (hr > 120 || bp < 90) {
            return "1 - Immediate";
        } else if (symptomCode >= 4) {
            return "2 - Urgent";
        } else {
            return "3 - Low Priority";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("=== MediTriage Java API ===");

        // Input simulation
        System.out.print("Enter Age: ");
        int age = scanner.nextInt();

        System.out.print("Enter Blood Pressure (BP): ");
        int bp = scanner.nextInt();

        System.out.print("Enter Heart Rate (HR): ");
        int hr = scanner.nextInt();

        System.out.print("Enter Symptom Code (0-10): ");
        int symptomCode = scanner.nextInt();

        String result = predictTriage(age, bp, hr, symptomCode);
        System.out.println("Predicted Triage Priority: " + result);
    }
}
