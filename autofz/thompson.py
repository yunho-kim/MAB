import numpy as np
import logging

class fuzzer():
    def __init__(self):
        logging.info('fuzzer init')
        self.S = 1 # success count
        self.F = 1 # fail count
        self.prob = 0.0

    def selectFuccer(fuzzers):
        logging.info('Select fuzzer')

        for value in options.vaules():
            value.prob = np.random.beta(value.S, value.F, size = 1)
            logging.info(f'Success: { value.S }, Fail : {value.F}, Prob: { value.prob }')

        max_prob_fuzzer = max(fuzzers, key=lambda key: fuzzers[key].prob)

        logging.info(f'selected fuzzer: { max_prob_fuzzer }')

        return max_prob_fuzzer

    def updateFuzzerCount(fuzzer, criteria):
        if criteria == 1:
            fuzzer.S = fuzzer.S + 1
            logging.debug('Update fuzzer function - success')
        else:
            fuzzer.F = fuzzer.F +1
            logging.debug('Update fuzzer function - fail')


    
