# Jamar Fraction
# CPTS 315
# PA3

from random import shuffle

STOP_LIST = '../data/fortune-cookie-data/stoplist.txt'
TRAIN_DATA = '../data/fortune-cookie-data/traindata.txt'
TRAIN_LABELS = '../data/fortune-cookie-data/trainlabels.txt'
TEST_DATA = '../data/fortune-cookie-data/testdata.txt'
TEST_LABELS = '../data/fortune-cookie-data/testlabels.txt'

OUT_FILE = './output.txt'


# Read in the file
def read_input(file):

    # reading in data
    with open(file, "r") as text_file:
        all_lines = text_file.read().splitlines()

    return all_lines


# file dumping
def dump_output(user_recommendations):
    with open(OUT_FILE, "w") as text_file:
        pass

    return


def build_vocabulary(training_lines, stop_list):
    # create a set of all the words in the fortune cookies that are not stop words
    print("Cleaning vocabulary")
    vocabulary = sorted(
        list(set([word for sentence in training_lines for word in sentence.split() if word not in stop_list])))
    print("done")

    return vocabulary


def create_feature_vectors(training_lines, vocabulary, stop_list):
    feature_vectors = []

    # split the training lines to a list of lists of strings
    split_lines = [line.split() for line in training_lines]

    for line in split_lines:

        current_vector = []

        # if the current word in the vocab is in the current line, append a 1, if not, append a zero
        # this produces a vector of size len(vocab), where the ith index of the vector will be a 1 if the ith word in
        # vocab is present in the current line
        for word in vocabulary:
            current_vector.append(1) if word in line else current_vector.append(0)

        feature_vectors.append(current_vector)

    # return the fruits of our labor
    return feature_vectors


def binary_classifier_algorithm(feature_vectors, training_labels, number_of_iterations):
    # initialize the weight vector + bias
    w = [0] * len(feature_vectors[0])
    b = 0

    # start training
    for iteration in range(number_of_iterations):

        # generate the order of training examples that we'll be iterating over
        r = list(range(len(feature_vectors)))
        shuffle(r)

        for i in r:

            # compute the activation
            a = compute_activation(weight_vector=w, feature_vector=feature_vectors[i], bias=b)

            # pull the correct answer from the training labels list
            correct_answer = int(training_labels[i]) if int(training_labels[i]) == 1 else -1

            if correct_answer * a <= 0:
                w = update_weights(weight_vector=w, feature_vector=feature_vectors[i], correct_answer=correct_answer)
                b += correct_answer

    return w, b


def compute_activation(weight_vector, feature_vector, bias):
    vector_summation = 0

    for i in range(len(feature_vector)):
        vector_summation += (weight_vector[i] * feature_vector[i])

    vector_summation += bias

    return vector_summation


def update_weights(weight_vector, feature_vector, correct_answer):
    new_weight_vector = [0] * len(weight_vector)

    for i in range(len(weight_vector)):
        new_weight_vector[i] = weight_vector[i] + (feature_vector[i] * correct_answer)

    return new_weight_vector


def build_test_dictionary(test_lines, test_labels):
    test_dictionary = {}

    for i in range(len(test_lines)):
        key = tuple(test_lines[i])
        value = test_labels[i]

        if test_dictionary.get(key):
            print("wait")

        test_dictionary[key] = value

    return test_dictionary


def perceptron_tests(weight_vector, bias, test_dictionary):
    pass


def main():
    # Fortune Cookie classification

    # Pre-process steps
    # ********************************************************
    # Read in the training data
    print("Reading training data")
    training_lines = read_input(TRAIN_DATA)
    print("Done")

    # Read in the training labels
    print("Reading training labels")
    training_labels = read_input(TRAIN_LABELS)
    print("Done")

    # Read in the stop list
    print("Reading stop list")
    stop_list = read_input(STOP_LIST)
    print("Done")

    print("Building vocabulary")
    vocabulary = build_vocabulary(training_lines, stop_list)
    print("Done building vocabulary")

    # Create training feature vectors
    print("Creating training feature vectors")
    training_feature_vectors = create_feature_vectors(training_lines=training_lines, vocabulary=vocabulary,
                                                      stop_list=stop_list)
    print("Done")

    # Train with provided examples
    print("Training..")
    weight_vector, bias = binary_classifier_algorithm(training_feature_vectors, training_labels, 20)
    print("Done")

    # Read in test data
    print("Reading test data")
    test_lines = read_input(TEST_DATA)
    print("Done")

    # Read in the training labels
    print("Reading training labels")
    test_labels = read_input(TEST_LABELS)
    print("Done")

    # Create test feature vectors
    print("Creating test feature vectors")
    test_feature_vectors = create_feature_vectors(training_lines=test_lines, vocabulary=vocabulary, stop_list=stop_list)
    print("Done")

    # Build line:answer dictionary
    print("Creating test dictionary")
    test_dictionary = build_test_dictionary(test_feature_vectors, test_labels)
    print("Done")

    # Run perceptron tests
    print("Running perceptron tests")
    perceptron_tests(weight_vector=weight_vector, bias=bias, test_dictionary=test_dictionary)
    print("done")


if __name__ == '__main__':
    main()
