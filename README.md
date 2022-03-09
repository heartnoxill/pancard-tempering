2022-03-09T08:27:17.447991+00:00 heroku[web.1]: State changed from crashed to starting

2022-03-09T08:27:29.600133+00:00 heroku[web.1]: Starting process with command `gunicorn`

2022-03-09T08:27:31.112292+00:00 app[web.1]:

2022-03-09T08:27:31.112324+00:00 app[web.1]: Error: No application module specified.

2022-03-09T08:27:31.295166+00:00 heroku[web.1]: Process exited with status 1

2022-03-09T08:27:31.407974+00:00 heroku[web.1]: State changed from starting to crashed

2022-03-09T08:27:44.000000+00:00 app[api]: Build succeeded

2022-03-09T08:29:32.585002+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" 

I am stuck with these and cannot proceed further, can anyone help me 😂😭

Step to run application:

Step 1:	Create the copy of the project.

Step 2: Open command prompt and change your current path to folder where you can find 'app.py' file.

Step 3: Create environment by command given - conda create -name <environment name>

Step 4: Activate environment by command as follows- conda activate <environment name>

Step 5: Use command below to install required dependencies- python -m pip install -r requirements.txt

Step 6: Run application by command; python app.py You will get url copy it and paste in browser.

Step 7: You have sample_data folder where you can get images to test.
