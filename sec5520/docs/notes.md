Sec5520
=======

## Operation
1. Take a photo every X seconds
2. Upload photo to dropbox
3. If motion detected
    - generate temp link to last photo
    - send SMS message with photo link
    - start taking photos even quicker
    - after X min, reset to X seconds

## Tasks
1. Python script to take a photo every X seconds
2. Upload photos to Dropbox
    - generate temp link to photo
3. Send text message
4. Detect motion

## Notes
* Keep photos small in file size, but keep detail

## Links

### Dropbox
* http://dropbox-sdk-python.readthedocs.io/en/master/index.html

### Blynk
* http://docs.blynk.cc/#hardware-set-ups-raspberry-pi
* https://github.com/blynkkk/blynk-library
* http://community.blynk.cc/t/howto-for-raspberry-pi/332/21
* https://github.com/blynkkk/blynk-library/blob/master/linux/README.md
