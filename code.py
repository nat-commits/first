class ProbablyMisguidedDatastoreButIBetYouItWorks(dict):
    def link_two_things(self, thing1, thing2):
        self[thing1] = thing2
        self[thing2] = thing1

    def unlink_two_things(self, thing):
        try:
            the_other_thing = self.pop(self.pop(thing))
        except KeyError:
            the_other_thing = None
        return the_other_thing


ME = '+18012267012'  # my phone number growing up. get a real one from twilio
MAGIC_WORD = 'go'  # must be lowercase
SAFE_WORD = 'stop'  # must be lowercase
QUESTION_OF_THE_MOMENT = 'What scared you as a child?'
POLITE_THANKS = 'Good answer! I\'ll let you know when someone gives me the same one. Change your mind any time by texting me the word {}. Text me the word {} and I\'ll forget you'.format(MAGIC_WORD, SAFE_WORD)
LADIES_AND_GENTLEMEN_WE_HAVE_A_MATCH = 'I\'ve found someone else who gave the same answer to the question "{}". Text me to text them.'.format(QUESTION_OF_THE_MOMENT)
YOUR_ASS_JUST_GOT_DITCHED = 'It\'s me ({}) again. It seems I\'ve lost your connection. I have likewise forgotten you already. Text me the word {} if you\'d like to try meeting again'
DONT_LET_THE_DOOR_HIT_YOUR_ASS_ON_THE_WAY_OUT = 'I\'ve forgotten you already'


PROBABLY_MISGUIDED_DATASTORE = ProbablyMisguidedDatastoreButIBetYouItWorks()


def is_phone_number(possibly_a_phone_number):
    # hope it's this easy
    try:
        return possibly_a_phone_number.startswith('+')
    except AttributeError:
        return False


def text(number, message):
    # TODO: import twilio's shit and text a message to a number
    print('{} to {}: {}'.format(ME, number, message))


def do_something_cool_with_a_number_and_a_message(number, message):
    other_number_or_message_hash = PROBABLY_MISGUIDED_DATASTORE.get(number)
    other_number_or_message_hash_is_phone_number = is_phone_number(possibly_a_phone_number=other_number_or_message_hash)
    this_number_is_sad_and_alone = other_number_or_message_hash is None
    message_stripped_and_brought_down = ''.join(message.split()).lower()

    if message_stripped_and_brought_down == MAGIC_WORD:
        text(number, QUESTION_OF_THE_MOMENT)
        if not this_number_is_sad_and_alone and other_number_or_message_hash_is_phone_number:
            text(other_number_or_message_hash, YOUR_ASS_JUST_GOT_DITCHED)
    elif message_stripped_and_brought_down == SAFE_WORD:
        text(number, DONT_LET_THE_DOOR_HIT_YOUR_ASS_ON_THE_WAY_OUT)
        if not this_number_is_sad_and_alone and other_number_or_message_hash_is_phone_number:
            text(other_number_or_message_hash, YOUR_ASS_JUST_GOT_DITCHED)
    elif other_number_or_message_hash_is_phone_number:
        text(other_number_or_message_hash, message)
    else:
        # we're gonna need some more variables
        message_hashish = hash(message_stripped_and_brought_down)
        soulmates_number = PROBABLY_MISGUIDED_DATASTORE.get(message_hashish)
        ladies_and_gentlemen_we_have_a_match = soulmates_number and soulmates_number != number

        if ladies_and_gentlemen_we_have_a_match:
            PROBABLY_MISGUIDED_DATASTORE.unlink_two_things(soulmates_number)
            PROBABLY_MISGUIDED_DATASTORE.link_two_things(number, soulmates_number)
            text(number, LADIES_AND_GENTLEMEN_WE_HAVE_A_MATCH)
            text(soulmates_number, LADIES_AND_GENTLEMEN_WE_HAVE_A_MATCH)
        else:
            PROBABLY_MISGUIDED_DATASTORE.link_two_things(number, message_hashish)
            text(number, POLITE_THANKS)
