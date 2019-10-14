# Interactive-Digit-Recognizer
Interactive digit recognition using pygame and keras


Using a Neural Network and the typical MNIST dataset, I've trained a model and saved it so when drawing a new digit it tries to recognize it.

WHEN FAILING:
- Try to simulate the MNIST number for the best accuracy.
- Redraw lines making them a couple of pixels wide.

This is a personal project with learning prurposes only. It has no copyright or license.


EDIT: the new model (which I didn't upload it yet) uses a CNN to "preprocess" the mnist images (just two conv2D layer and two maxpooling2D). With this new model, reaches an accuracy of 99.6% (best) when the last model did ~96% (which for the purpose is fine).
