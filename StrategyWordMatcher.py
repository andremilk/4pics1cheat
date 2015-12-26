import types

class StrategyWordMatcher:

    def __init__(self, matcher=None):
        if matcher is not None:
            self.word_exists = types.MethodType(matcher, self)

    def word_exists(word, language):
        print('No default matcher available yet.')
