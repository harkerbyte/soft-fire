# Soft - Fire 
![Static Badge](https://img.shields.io/badge/Author-Shade-green?style=for-the-badge&logo=github)
![GitHub issues](https://img.shields.io/github/issues/harkerbyte/safe-fire?style=for-the-badge&logo=git)

![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/harkerbyte/safe-fire?style=for-the-badge&logo=git&color=blue)
![GitHub watchers](https://img.shields.io/github/watchers/harkerbyte/safe-fire?style=for-the-badge&logo=git&logoColor=green)

### Extensions and Licence

![GitHub Repo stars](https://img.shields.io/github/stars/harkerbyte/soft-fire?style=for-the-badge&logo=github)
![node-current](https://img.shields.io/node/v/package?style=for-the-badge&logo=node&logoColor=blue)
![GitHub License](https://img.shields.io/github/license/harkerbyte/soft-fire?style=for-the-badge&logo=github&color=green)


### App description
An innovative web app, seamlessly integrates **Python and JS** to create a dynamic game canvas, delivering an immersive gaming experience. Soft Fire stands out by allowing users to upload and showcase their games within its integrated store. Moreover, it streamlines development with a unique feature, leveraging Node.js and Webpack to convert TypeScript (.ts) and SCSS (.scss) to JavaScript and CSS, making Soft Fire a comprehensive and solution-oriented tool for game creation and management.



# ChangeLog

| Version |  Publicized  |   Changes 
----------|--------------|---------          
|1.0.0    | 2024-01-19   | Initial release 
|2.3.0    | 2024-02-20   | New Ui and feel, Template to upload game properties. File conversion & Download (Ts to Js & .scss to .css)|


**Soft Fire** is designed for continuous improvement, with ongoing **Minor** patches delivering new features and enhanced security. Its dynamic nature ensures that development remains active, guaranteeing a cutting-edge experience for users as the software evolves over time.</br>
With that being said, feel free to report any issue, and if you have any ideas to improve the software, You should submit a pull request. I'll gladly review the code and merge if necessary.

![GitHub Release](https://img.shields.io/github/v/release/harkerbyte/soft-fire?display_name=release&style=for-the-badge&logo=ethereum&color=blue)

## Installation 
  
* Open the terminal in Visual Studio Code. You can use shortcut <kbd>Ctrl</kbd>+<kbd>`</kbd>

* Use the **cd** command to navigate to the directory where you would like to clone the repository.
  
* Install VirtualEnv if not already installed `pip install virtualenv`
* Create a virtual environment  `virtualenv 'environment-name'`
* Activate the environment **Windows** - `.\enviroonment-name\Scripts\activate.bat` **macOS/Linux** - `source environment-name/bin/activate`
   
* Use  `git clone https://github.com/harkerbyte/soft-fire` to have the repository cloned.
* Navigate to the project directory **cd** C:\<directory-path>

* Install the software's Dependencies. Run `pip install -r requirements.txt` 
* Run Migrations `py manage.py migrate`
  
* To start the project. Run `py manage.py runserver` Now open `127.0.0.1:8000` on your browser.

  
* Login to the admin dashboard `127.0.0.1:8000/admin`
```
Username : Admin-1
Password : adminuser239
```

## Notice
* For any **html** file to be uploaded. . .It content must be similar to this:
  
```html
<div id="container">
  <div id="game"></div>
  <div id="score">0</div>
  <div id="instructions">Click (or press the spacebar) to place the block</div>
  <div class="game-over">
    <h2>Game Over</h2>
    <p>You did great, you're the best.</p>
    <p>Click or spacebar to start again</p>
  </div>
  <div class="game-ready">
    <div id="start-button">Start</div>
    <div></div>
  </div>
</div>
```

* It only need the raw HTML code since it will be incorporated using the **{{html_content|safe}}** variable tag, eliminating the necessity for a complete HTML structure with headers and bodies. This approach ensures flexibility in inserting HTML content directly into the templates. 
 A work - around could be available later on as the software's development progresses.

![Amazon-aws](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Visual-studio-code](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)

* If you intend to commit to this **project**, I'd advise you leave the debug setting default. If you turn off debug, the software would assume you're intending to deploy to production, which would require creating an S3 bucket. While configuring s3 bucket can be quite strenuous, do not worry as i have already done 80% of the job. You can just go ahead, create, and configure the server side.
```
   'static'
   'media'
```
![S3-Bucket-Objects](.images/soft-fire.png)
Fill in the correct information in an ".env" file located in the project's root directory.

* However, The API doesn't come with a command to collectmedia file for upload unto the s3 bucket. A workaround command would be available soon as the software's development proceeds.