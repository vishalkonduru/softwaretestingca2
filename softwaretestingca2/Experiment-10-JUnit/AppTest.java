import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class AppTest {
    private WebDriver driver;

    @Before
    public void setUp() {
        driver = new FirefoxDriver();
        driver.manage().window().maximize();
        driver.get("https://practicetestautomation.com/practice-test-login/");
    }

    @Test
    public void testValidLogin() {
        driver.findElement(By.id("username")).sendKeys("student");
        driver.findElement(By.id("password")).sendKeys("Password123");
        driver.findElement(By.id("submit")).click();

        String heading = driver.findElement(By.tagName("h1")).getText();
        Assert.assertEquals("Logged In Successfully", heading);

        String currentUrl = driver.getCurrentUrl();
        Assert.assertTrue(currentUrl.contains("logged-in-successfully"));

        System.out.println("Login heading matched. Test Passed.");
        System.out.println("URL validation passed. Test Passed.");
    }

    @After
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
