# first
I'm listening to this song right now:

https://open.spotify.com/track/3NUAOPFCMJg4di2qhy2lso?si=lVR9d5yLQnmB728zK9UgnQ

I don't want to put it on repeat. I just wish it were two hours long.

So the idea kicking around in my head right now is a phone number you can text to talk to the last person who responded the exact same way to a question the number texts you in response to the word 'go'.

There's no way that made sense. Let me try again.

Text `{{ magic_word }}` to `{{ real_number_once_you_sign_up_for_twilio }}`, and here's what's gonna happen behind the scenes:

- I've never actually listened for texts before. I'm assuming twilio has some kind of shit for that.
- Your phone number and message are gonna hit my code
- If your message is the word `{{ magic_word }}` I'm gonna text you a question back. I pick the question. It's hardcoded and changes whenever I feel like deploying (aws lambda?)
- If you text me anything else, I'm gonna store your phone number and message in memory (k so not aws lambda).
- Actually, I'm gonna check if a hash of your message exists in memory already. If the phone number it's associated with is yours, I'm not going to do anything except text you something polite back.
- **But** (new bullet for this) if the number is someone else's, I'm gonna make a link between your two numbers. You two can talk by texting `{{ real_number_once_you_sign_up_for_twilio }}` until one of you texts the word `{{ magic_word }}` (watch out) or until the memory gets flushed when I deploy the code again, probably to update the question.
- That's it! I'll be texting the number too sometimes. Maybe we can talk about...

`{{ hardcoded_thing_i_wanna_talk_about }}`