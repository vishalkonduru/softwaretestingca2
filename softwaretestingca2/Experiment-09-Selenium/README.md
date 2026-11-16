# Experiment 9: Cross-Browser Testing using Selenium

## Objective
Automate a valid login on the Practice Test Automation login page using Selenium WebDriver.

## Test data
- URL: https://practicetestautomation.com/practice-test-login/
- Username: `student`
- Password: `Password123`
- Expected heading: `Logged In Successfully`

## Prerequisites
- JDK 17 or later
- Maven or an IDE such as IntelliJ IDEA/Eclipse
- Google Chrome
- Internet access

## Setup
Create a Maven Java project and add this dependency to `pom.xml`:

```xml
<dependency>
    <groupId>org.seleniumhq.selenium</groupId>
    <artifactId>selenium-java</artifactId>
    <version>4.25.0</version>
</dependency>
```

Place `LoginAutomation.java` in the project's source folder. Selenium 4.6+ includes Selenium Manager, which can manage a compatible browser driver automatically. A manually hard-coded `chromedriver.exe` path is normally unnecessary.

## Run
From the project directory:

```powershell
mvn compile
```

Run `LoginAutomation` from your IDE, or configure the Maven Exec plugin and run:

```powershell
mvn exec:java -Dexec.mainClass="LoginAutomation"
```

## Expected console output
```text
Test Passed: Login Successful
```

## Lab-sheet note
The lab-sheet title says Selenium Grid, but the supplied program creates a local `ChromeDriver`. Actual Grid execution requires a Selenium Grid server and `RemoteWebDriver`; this implementation follows the supplied local Chrome program.
