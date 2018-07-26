def hey(phrase):
    # Bob is a lackadaisical teenager. In conversation, his responses are very limited.
    # Bob answers 'Sure.' if you ask him a question.
    # He answers 'Whoa, chill out!' if you yell at him.
    # He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
    # He says 'Fine. Be that way!' if you address him without actually saying anything.
    # He answers 'Whatever.' to anything else.
    #
    phrase = phrase.rstrip()
    if phrase.endswith('?') and not phrase.isupper():
        return 'Sure.'
    if phrase.isupper() and not phrase.endswith('?'):
        return 'Whoa, chill out!'
    if phrase.endswith('?') and phrase.isupper():
        return 'Calm down, I know what I\'m doing!'
    if len(phrase) == 0 or phrase.isspace():
        return 'Fine. Be that way!'
    return 'Whatever.'

