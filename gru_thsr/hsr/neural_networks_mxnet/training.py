import time
from random import shuffle

from mxnet import gluon, autograd, lr_scheduler, optimizer

from hsr.config import VERBOSITY
from hsr.evaluation.accuracy_mxnet import calculate_accuracy_0
from hsr.preprocessing.ts import load_whole_training_set, load_features, load_targets, get_number_of_batches

LOSS_FUNCTION = gluon.loss.SoftmaxCrossEntropyLoss()
LEARNING_RATE = 0.002
MOMENTUM = 0.9
MAX_NUM_EPOCHS = 50
SCHEDULER_STEPS = [10, 20, 30]
SCHEDULER_FACTOR = 0.5
TURN_OFF_THRESHOLD_ACCURACY = 95.0  # in percent


def train_0(neural_network, training_set_directory):
    if VERBOSITY > 0:
        print('Training using CPU.')
    number_of_batches = get_number_of_batches(training_set_directory)
    trainer = init_trainer_0(neural_network, number_of_batches)
    batch_indices = [i for i in range(number_of_batches)]
    features = load_whole_training_set(training_set_directory, load_features)
    targets = load_whole_training_set(training_set_directory, load_targets)
    mean_train_acc = 0.0
    prev_epoch_progress = 0
    for epoch in range(MAX_NUM_EPOCHS):
        tic = time.time()
        train_loss = 0.0
        train_acc = 0.0
        finished_batches = 0
        shuffle(batch_indices)
        for i in batch_indices:
            # load data and targets (labels)
            data = features[i]
            label = targets[i]
            # forward + backward
            with autograd.record():
                output = neural_network(data)
                loss = LOSS_FUNCTION(output, label)
            loss.backward()
            # update net parameters
            batch_size = int(label.shape[0])
            trainer.step(batch_size)
            # calculate training metrics
            train_loss += loss.mean().asscalar()
            train_acc += calculate_accuracy_0(output, label)
            finished_batches += 1
            if VERBOSITY > 2:
                epoch_progress = int(finished_batches * 100 / number_of_batches)
                if epoch_progress > prev_epoch_progress:
                    print("Epoch no. %d progress: %d%%." % (epoch, epoch_progress))
                prev_epoch_progress = epoch_progress
        mean_train_acc = (train_acc / number_of_batches) * 100  # in percent
        if VERBOSITY > 0:
            print("Epoch no.: %d; LR: %f; loss: %.3f; train accuracy: %.0f%%; epoch duration: %.1f sec." %
                  (epoch,
                   trainer.learning_rate,
                   train_loss / number_of_batches,
                   mean_train_acc,
                   time.time() - tic))
        if mean_train_acc > TURN_OFF_THRESHOLD_ACCURACY:
            break
    if VERBOSITY > 0:
        if mean_train_acc > TURN_OFF_THRESHOLD_ACCURACY:
            print("Training finished successfully.")
        else:
            print("Max. number of epochs reached, training finished.")
    return neural_network


def init_trainer_0(neural_network, number_of_batches):
    steps_iterations = [s * number_of_batches for s in SCHEDULER_STEPS]
    schedule = lr_scheduler.MultiFactorScheduler(step=steps_iterations, factor=SCHEDULER_FACTOR)
    schedule.base_lr = LEARNING_RATE
    sgd_optimizer = optimizer.SGD(learning_rate=LEARNING_RATE, momentum=MOMENTUM, lr_scheduler=schedule)
    trainer = gluon.Trainer(params=neural_network.collect_params(), optimizer=sgd_optimizer)
    return trainer
