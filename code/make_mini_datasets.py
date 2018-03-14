"""
A very simple script for generating a mini data set from
the training data sets, so that we can sanity check architecture
changes very quickly but using the dev set as a training set,
and this new mini set as the dev set.
"""

import itertools

mini_write_answer = open('../data/mini.answer', 'w')
mini_write_question = open('../data/mini.question', 'w')
mini_write_context = open('../data/mini.context', 'w')
mini_write_span = open('../data/mini.span', 'w')

train_reader_answer = open('../data/train.answer', 'r')
train_reader_question = open('../data/train.question', 'r')
train_reader_context = open('../data/train.context', 'r')
train_reader_span = open('../data/train.span', 'r')

MINI_SZ = 1000
count = 0
answers = []
questions = []
for answer, question in itertools.izip(train_reader_answer, train_reader_question):
    answers.append(answer)
    questions.append(question)
    count += 1
    if count == MINI_SZ:
        break

mini_write_answer.writelines(answers)
mini_write_answer.close()

mini_write_question.writelines(questions)
mini_write_question.close()

### repeat :)

count = 0
contexts = []
spans = []
for context, span in itertools.izip(train_reader_context, train_reader_span):
    contexts.append(context)
    spans.append(span)
    count += 1
    if count == MINI_SZ:
        break

mini_write_context.writelines(contexts)
mini_write_context.close()

mini_write_span.writelines(spans)
mini_write_span.close()

















print count
