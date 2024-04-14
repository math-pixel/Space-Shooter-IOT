# Space Shooter IOT

```
npm install socket.io
```

# Error Code

## Logic
the logic of blink is :

- blink the number of the current process with an interval of 1 sec
- 5 blink with 0.5 sec of interval for validate the test
- 5 blink with 0.2 sec of interval for invalid process / connection
- 10 blink with 0.2 sec of interval for invalid user interaction

example :
step 1 = init phase 1 => one blink
step 2 = wifi testing => 5 blink of 0.5 interval => validate
step 3 = init phase 2 => 2 blink with 1 sec interval
step 4 = sensor testing => 5 blink with 0.2 interval => !! ERROR of the sensor !! 

## ESP 32

Order test :
1) Wifi Connection
2) Server Connection
3) Gyroscope Connection

Importante Note for ESP :
- first blink its normal connection of wifi (ignore it)

## Raspberry PI
Order test :
1) Wifi Connection
2) Server Connection
3) Button Test => you have 5 sec for press the button
4) HC04 Test sensor => you have 5 sec for put your hand in front of the sensor between 5 and 10 cm