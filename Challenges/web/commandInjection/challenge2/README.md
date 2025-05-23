# Command Injection Challenge

![Command Injection Challenge](media/landingPage.png)

# Starting the Application (using Docker)
## Create Docker Image
```bash
sudo docker build -t commandinjectionlab2 .
```

## Starting the Application
```bash
sudo docker run --rm -it -p 8081:5000 -v ./.env:/commandInjectionLab2/.env --name commandinjectionlab2-container commandinjectionlab2
```
-> The application is noew available at `http://localhost:8081/`

# Challenge
Try to escalate the command injection vulnerabilities and read `flag.txt` at the source folder. Please don't break stuff. Thank you!
In this challenge some filtering is an place, so it might be a little bit more challenging.
