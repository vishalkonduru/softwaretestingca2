# Experiment 13: Performance Testing using Apache JMeter

## Objective
Measure homepage response time, throughput, concurrency, and error percentage.

## Prerequisites
- Apache JMeter 5.6.3 or a compatible newer release
- Java installed and available on PATH
- Internet connection

Check Java in PowerShell:

```powershell
java -version
```

Download the **binary ZIP** from the official Apache JMeter downloads page:
https://jmeter.apache.org/download_jmeter.cgi

Extract it and launch the GUI from its `bin` folder:

```powershell
cd C:\path\to\apache-jmeter\bin
.\jmeter.bat
```

## Open and run the supplied test plan
1. In JMeter, select **File → Open**.
2. Open `HomepageLoadTest.jmx`.
3. Confirm Thread Group: 10 threads, 10-second ramp-up, 2 loops.
4. Confirm HTTP Request: HTTPS, server `www.example.com`, path `/`, method GET.
5. Confirm the Summary Report and View Results Tree listeners are present.
6. Click the green Start button.

## Expected request count
10 users × 2 loops = **20 samples**.

Actual response times and throughput vary with network conditions and the target server. The sample values in the lab manual are illustrative, not guaranteed output.

## Command-line execution (optional)
From JMeter's `bin` directory:

```powershell
.\jmeter.bat -n -t "C:\path\to\HomepageLoadTest.jmx" -l "C:\path\to\result.jtl" -e -o "C:\path\to\html-report"
```

Open `html-report\index.html` in a browser.

## Important
Only run load tests against systems you own or have permission to test. JMeter 2.10 is very old and may have compatibility issues with modern Java; use a current JMeter 5.x release.
