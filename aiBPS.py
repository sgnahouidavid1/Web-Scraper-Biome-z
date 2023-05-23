import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
#https://stackoverflow.com/questions/24871047/importerror-no-module-named-sklearn-feature-extraction-text
#Step 1: Make sure apt-get is updated

#sudo apt-get update
#Step 2: Install dependencies

#sudo apt-get install build-essential python-dev python-setuptools python-numpy python-scipy libatlas-dev libatlas3gf-base
#Step 3: pip install Scikit Learn

#pip install --user --install-option="--prefix=" -U scikit-learn
def preprocess(text):
    # Remove special characters and numbers
    text = re.sub('[^a-zA-Z]', ' ', text)
    # Convert to lowercase
    text = text.lower()
    return text

def categorize_bps(paragraph):
    # Define the categories and their corresponding labels
    categories = {'Biological': 0, 'Psychological': 1, 'Social': 2}

    # Load the labeled dataset and preprocess the text
    dataset = []
    with open('labeled_dataset.txt', 'r') as f:
        for line in f:
            label, text = line.split('\t')
            text = preprocess(text)
            dataset.append((text, categories[label.strip()]))

    # Vectorize the text using a bag-of-words model
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform([preprocess(paragraph)] + [d[0] for d in dataset])
    X_test = X[0]
    X_train = X[1:]

    # Train an SVM on the labeled dataset
    y_train = [d[1] for d in dataset]
    clf = SVC(kernel='linear')
    clf.fit(X_train, y_train)

    # Predict the category of the given paragraph
    y_pred = clf.predict(X_test)

    # Return the predicted category
    for category, label in categories.items():
        if label == y_pred:
            return category
