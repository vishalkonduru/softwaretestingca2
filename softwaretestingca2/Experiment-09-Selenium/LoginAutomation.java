import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class LoginAutomation {
    public static void main(String[] args) {
        // Selenium 4.6+ can manage the matching ChromeDriver automatically.
        WebDriver driver = new ChromeDriver();

        try {
            driver.get("https://practicetestautomation.com/practice-test-login/");
            driver.manage().window().maximize();

            driver.findElement(By.id("username")).sendKeys("student");
            driver.findElement(By.id("password")).sendKeys("Password123");
            driver.findElement(By.id("submit")).click();

            String heading = driver.findElement(By.tagName("h1")).getText();

            if (heading.equals("Logged In Successfully")) {
                System.out.println("Test Passed: Login Successful");
            } else {
                System.out.println("Test Failed: Login Not Successful");
            }
        } finally {
            driver.quit();
        }
    }
}
