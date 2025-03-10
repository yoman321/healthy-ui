#  Healthy UI

### Getting started 

### React via CRA
##### 1. get nvm 
`https://github.com/nvm-sh/nvm`

##### 2. install the right node / npm version with nvm   

`$ cd react-app && nvm use `

##### 3. install node modules  

`$ npm install`

##### 4. start the webpack dev server 

`$ npm run start`


### Python / Flask 

#### via venv 

#### 1. create the venv 
`$ python -m venv .venv`

#### 2. activate it 
`$ source .venv/bin/activate`

#### 3. install reqs via pip 
`pip install -r requirements.txt`

#### 4. If the library.dll file is not present in the flask_app directory
```
cd go
go build -o library.dll -buildmode=c-shared main.go library.go c_youtube.go c_newsapi.go c_factcheck.go
rm library.h
mv library.dll ../flask_app
```
#### via docker 


### EXTENSION

the extension needs to be loaded into chrome: 

extension workflow: 
`$ cd extension-react`  
`$ npm install`   
`$ npm run build`   
`$ npm watch`   

open chrome browser  
navigate to [chrome extensions page](chrome://extensions/)

select 'developer mode on' 
select 'load unpacked'
navigate to the extension-react folder 
choose the 'dist' directory 

## Credits
- Logo and Icon for the chrome extension are generate from the logo.com website

### ToDo
#### Winter 2025
- Finish implementing the videos fact-check articles
  - Fix the backend code to remove all inference errors [Done for now]
  - Fix frontend extension code so that it runs on local host 
    - Display fact checked websites using the extension [Done]
    - Potentially always add it as a pop up when clicking a new youtube video [Done -> users are free to click the extension for fack check articles]
    - Need to add caching at the frontend [Done]
    - Add logo to extension [Done]
    - Create .env file 
  - Create pipelines to host website
    - Create docker container
    - Host on remoter server (Heroku, Azure, ...)
  - Need to update fact-check algo and add anti-siloing algo
    - Update fact-check algo to better match words
    - Add anti-siloing algo

- If time permits, start implementing the carbon emission tracker
