# ml_models.py

from sklearn.ensemble import RandomForestClassifier

class TradingModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

# Example usage
# model = TradingModel()
# model.train(X_train, y_train)
# predictions = model.predict(X_test)