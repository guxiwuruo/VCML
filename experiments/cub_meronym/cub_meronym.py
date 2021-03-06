#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : cub_meronym.py
# Author            : Chi Han, Jiayuan Mao
# Email             : haanchi@gmail.com, maojiayuan@gmail.com
# Date              : 17.07.2019
# Last Modified Date: 31.08.2019
# Last Modified By  : Chi Han, Jiayuan Mao
#
# This file is part of the VCML codebase
# Distributed under MIT license


from .load_cub_meronym import \
    raw_classify_meronym, meronym_balanced_split
from ..utils import assemble, load_questions


def mixed_meronym(test_concepts, dataset, args, logger):
    logger('Mixing visual and conceptual suites for meronym experment')
    with logger.levelup():
        clsf_part = raw_classify_meronym(dataset, args, logger)
        mero_part = meronym_balanced_split(
            test_concepts, dataset, args, logger)
        mixed = load_questions.combine_with_ratio(
            (clsf_part, mero_part),
            load_questions.cg_ratios(args),
            args, logger,
        )
    return mixed


def get_training_schedule(concepts, args, dataset, logger):
    test_concepts = assemble.get_testConcepts(
        concepts, args, logger)
    suite = mixed_meronym(test_concepts, dataset, args, logger)
    training_schedule = [
        {
            'length': 100,
            'question_splits': suite,
            'test_concepts': test_concepts,
        }
    ]
    return training_schedule


config = {
    'dataset': 'cub_meronym',
    'training_schedule': get_training_schedule,
}
