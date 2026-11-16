# Experiment 10: Integration of Selenium with JUnit

## Objective
Integrate Selenium WebDriver with JUnit, automate a valid login, and verify the result using assertions.

## Prerequisites
- JDK 17+
- Maven
- Firefox browser
- IntelliJ IDEA or Eclipse (optional)

## Project layout
Place `AppTest.java` under `src/test/java` in a Maven project and use the supplied `pom.xml`.

## Run from PowerShell
Open a terminal in the folder containing `pom.xml`:

```powershell
mvn test
```

The test opens the login page, enters valid credentials, clicks Login, checks the success heading, and verifies the URL.

## Expected output
```text
Login heading matched. Test Passed.
URL validation passed. Test Passed.
```

Maven should report 1 test, 0 failures, and 0 errors.

## Notes
The lab-sheet program uses JUnit 4 imports and annotations (`@Before`, `@Test`, `@After`, `Assert`). This repository implements the shown JUnit version, not TestNG. Selenium Manager can manage the browser driver automatically.
