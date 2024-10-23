# PhishGuard Vision

PhishGuard Vision is a machine learning-based project that detects phishing websites using screenshot analysis. The goal is to identify malicious websites based on visual clues, helping to prevent phishing attacks before they harm users.

## Features

- **Screenshot Analysis**: Analyzes website screenshots to detect phishing attempts.
- **Machine Learning Models**: Leverages image processing and classification algorithms for detection.
- **High Accuracy**: Trained on a dataset of phishing and legitimate websites for improved accuracy.
- **Automated Detection**: Quickly flags potential phishing websites from screenshots.
  
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Website](#website)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abhis0410/phishguard-vision.git
   cd phishguard-vision
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Windows, use `env\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the model on a screenshot**:
   ```bash
   python detect.py --image path/to/website_screenshot.png
   ```

2. **Output**: The model will classify the screenshot as either `Phishing` or `Legitimate`.

### Example:
```bash
python detect.py --image sample_screenshot.png
```


## Website

1. **Run the streamlit app**:
   ```bash
   streamlit run ./app/streamlit_app.py
   ```

2. **Output**: This will run the website, where user can upload and classify the image.


## Dataset

The project uses a dataset of phishing and legitimate website screenshots. You can find the dataset [Dataset Link](https://www.kaggle.com/datasets/saurabhshahane/phishiris)

- **Legitimate Website Screenshots**: Images of well-known and trusted websites.
- **Phishing Website Screenshots**: Screenshots of known phishing sites, collected from security resources.

## Model Training

To retrain the model:

1. **Prepare the dataset**:
   - Place phishing and legitimate screenshots into `data/train/phishing/` and `data/train/legitimate/`.

2. **Train the model**:
   ```bash
   python train.py --epochs 50 --batch_size 32
   ```

3. **Save and evaluate**:
   After training, the model will be saved in the `models/` directory.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes. 
You can also report any issues or suggestions in the [Issues](https://github.com/abhis0410/phishguard-vision/issues) section.

## License

This project is licensed under the MIT License.

