<h1 align=center>Mail-it</h1>

A module written using python to send a mail template to 'n' number of email addresses. 

## Set Up

1. Clone this repository <br />
2. Populate the [data.csv](data.csv) file with the users data <br /> 
   - [data.csv](data.csv) must have 'id' and 'email' columns <br />

<table>
<tr>     
<th>id</th>
<th>email</th>
</tr>
<tr>     
<td>1</td>
<td>xyz@abc.com</td>
</tr>
</table>

4. Include the from email address and password in [mail_manager.py](mail_manager.py) <br />


## Edit Template

Insert your mail message by editing the files in [templates](templates/) folder <br />

**Example:** <br />
<br />
[email_message.txt](templates/email_message.txt)<br />
```
Hey {name}! your monthly bill is {amount}
```
[email_message.html](templates/email_message.html)<br />
```
<html>
     <head></head>
     <body>
          <p>Hey {name}!</p></br>
          <p>Yout monthly bill is {amount}</p> </br>
     </body>
</html>
```
> The variables name and amount get rendered with user's data from the data.csv file <br />


## Execute <br />

Run the module using command line arguments <br />

##### To view a particular user <br />
```
python Mail-it View -id <idno>
```
or
```
python Mail-it View -email <email>
```
##### To message a particular user <br />
```
python Mail-it Message -id <idno>
```
or
```
python Mail-it Message -email <email>
```
##### To view all users <br />
```
python Mail-it ViewAll
```
##### To message all users <br />
```
python Mail-it MessageAll
```
**Enter the subject and _the job is done!_**
