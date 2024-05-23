    // Algorithm in JAVA
    
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class IoVSecuritySystem {

    // Method to simulate collecting vehicle network traffic data
    public List<Double> collectTrafficData() {
        // Simulating network traffic data (example)
        List<Double> trafficData = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < 100; i++) {
            // Generating random network traffic data (example)
            double trafficVolume = random.nextDouble() * 100; // Random value between 0 and 100
            trafficData.add(trafficVolume);
        }
        return trafficData;
    }

    // Method to apply homomorphic encryption to collected data
    public List<Double> encryptData(List<Double> rawData) {
        // Simulating homomorphic encryption: adding a small random value to the data
        List<Double> encryptedData = new ArrayList<>();
        Random random = new Random();
        for (double value : rawData) {
            double encryptedValue = value + random.nextDouble(); // Adding a small noise
            encryptedData.add(encryptedValue);
        }
        return encryptedData;
    }

    // Method for detecting anomalies in encrypted data
    public boolean detectAnomalies(List<Double> encryptedData) {
        // Simulation: identifying anomalies as values outside the range [0, 50]
        for (double value : encryptedData) {
            if (value < 0 || value > 50) {
                return true; // Anomaly detected
            }
        }
        return false; // No anomalies detected
    }

    // Method for homomorphic addition of encrypted data
    public List<Double> homomorphicAddition(List<Double> encryptedData1, List<Double> encryptedData2) {
        List<Double> result = new ArrayList<>();
        for (int i = 0; i < encryptedData1.size(); i++) {
            double sum = encryptedData1.get(i) + encryptedData2.get(i);
            result.add(sum);
        }
        return result;
    }

    // Main method
    public static void main(String[] args) {
        IoVSecuritySystem securitySystem = new IoVSecuritySystem();

        // Collect vehicle network traffic data
        List<Double> trafficData = securitySystem.collectTrafficData();

        // Apply homomorphic encryption to collected data
        List<Double> encryptedData = securitySystem.encryptData(trafficData);

        // Perform homomorphic addition
        List<Double> sumData = securitySystem.homomorphicAddition(encryptedData, encryptedData);

        // Detect anomalies in homomorphically added data
        boolean anomalyDetected = securitySystem.detectAnomalies(sumData);

        // If anomalies are detected, respond to the intrusion attempt
        if (anomalyDetected) {
            System.out.println("Alert: Anomaly detected! Possible intrusion attempt via botnet.");
        } else {
            System.out.println("No anomalies detected in the vehicle network traffic data.");
        }
    }
}
