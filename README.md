# DISCLAIMER: This is a side project for fun.<br>Do not use this code for hacking purposes (including White Hacking).
Realistically most applications should be able to prevent scripts of this nature from working so please don't try. 

# What is Password Cracking With Response Times? 
Password cracking refers to... well... figuring out a passcode.<br>
So what does Response Time have to do with this? <br>
Well, when you pass in a password candidate into an application, 
that application needs to process the input and check if it matches the correct password or not.<br> 
This process takes time, and it takes different amounts of time depending on how correct/incorrect your guess is.<br> 
This application exploits this implementation detail to "crack" hypothetical passwords.

# How to run 
Simply run main and enjoy the show!<br> 
If you would like to attempt a different password to be broken, insert your hypothetical username and password in
the ImplementationDetails.py -> password_database<br>
Afterwords, pass in the username in PasswrdCracking.py -> main(user)

### This project is a nice reminder and motivation to take extra care when validating passwords and not rely on default/bare minimum implementations.