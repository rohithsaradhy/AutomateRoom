import speech_recognition as sr
import spur
import time
import pyttsx
#key is 9fa31a639d1b4455a45024418c64b2c6 and 096827ed737c443486d7ba9e988262d1

shell = spur.SshShell(hostname="10.0.28.254 ip", username="pi", password="this is password",
                      missing_host_key=spur.ssh.MissingHostKey.accept
                      )


def check(sound):
    return sound in what_you_said


while True:

    # obtain audio from the microphone
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True
    r.pause_threshold = 0.5
    with sr.Microphone() as source:
        print("Hello Rohith, what can I do to Help?")
        audio = r.listen(source, timeout=None)
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`

        what_you_said = r.recognize_google(audio,language="en-IN")
        print what_you_said
        engine = pyttsx.init()
        if check("on") and (check('power') or check('all') or check('everything') or check('both') or (
                    check('light') and check('fan'))):
            print "Okay,I will switch on both light and fan"
            engine.say('Okay,I will switch on both light and fan')
            engine.runAndWait()
            result = shell.run(["python", "/home/pi/voiceCommands/fan_on"])
            time.sleep(1)
            result = shell.run(["python", "/home/pi/voiceCommands/light_on"])


        elif (check("off") or check('of')) and (
                        check('power') or check('all') or check('everything') or check('both') or (
                    check('light') and check('fan'))):
            engine.say('Okay,I will switch off both light and fan')
            engine.runAndWait()
            result = shell.run(["python", "/home/pi/voiceCommands/fan_off"])
            time.sleep(1)
            result = shell.run(["python", "/home/pi/voiceCommands/light_off"])
            print "Okay,I will switch off both light and fan"

        elif check("on") and (check('lights') or check('light')):
            result = shell.run(["python", "/home/pi/voiceCommands/light_on"])

            engine.say('Okay,I will switch on the light')
            engine.runAndWait()
            print "Okay,I will switch on the light"

        elif (check("off") or check('of')) and (check('lights') or check('light')):
            result = shell.run(["python", "/home/pi/voiceCommands/light_off"])
            engine.say('Okay,I will switch off the light')
            engine.runAndWait()
            print "Okay,I will switch off the light"

        elif (check("on")) and (check('fan') or check('sun') or check('fans')):
            result = shell.run(["python", "/home/pi/voiceCommands/fan_on"])
            engine.say('Okay,I will switch on the fan')
            engine.runAndWait()
            print "Okay,I will switch on the fan"

        elif (check("off") or check('of')) and (
                        check('fan') or check('sun') or check('phone') or check('son') or check('fans')):
            result = shell.run(["python", "/home/pi/voiceCommands/fan_off"])
            print 1
            engine.say('Okay,I will switch off the fan')
            engine.runAndWait()
            print "Okay,I will switch off the fan"

        elif check("on") and (check('power') or check('all') or check('everything') or check('both') or (
                    check('light') and check('fan'))):
            print "Okay,I will switch on both light and fan"
            engine.say('Okay,I will switch on both light and fan')
            engine.runAndWait()
            result = shell.run(["python", "/home/pi/voiceCommands/fan_on"])
            time.sleep(3)
            result = shell.run(["python", "/home/pi/voiceCommands/light_on"])


        elif (check("off") or check('of')) and (check('power') or check('all') or check('everything') or check('both')):
            engine.say('Okay,I will switch off both light and fan')
            engine.runAndWait()
            result = shell.run(["python", "/home/pi/voiceCommands/fan_off"])
            time.sleep(1)
            result = shell.run(["python", "/home/pi/voiceCommands/light_off"])
            print "Okay,I will switch off both light and fan"

        else:
            engine.say("Sorry I didn't get that")
            engine.runAndWait()
            print "Sorry I didn't get that"
            # print(result.output)

    except sr.UnknownValueError:
        print("I could not understand what you said")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
