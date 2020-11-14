[![PyPI - Python](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8-blue.svg)](https://pypi.org/project/translation-quality-estimator/)
[![PyPI - License](https://img.shields.io/badge/license-MIT-green.svg)](/LICENSE)
[![PyPI - PyPi](https://img.shields.io/pypi/v/translation-quality-estimator)](https://pypi.org/project/translation-quality-estimator/)

# Translation Quality Estimator

Translation Quality Estimator is a simple but powerful way of estimating the quality of translations in over a hundred languages. It takes two lists of strings as input and returns the cosine similarity scores between their embeddings.

<a name="toc"/></a>
## Table of Contents  
<!--ts-->
   1. [About the Project](#about)  
   2. [Getting Started](#gettingstarted)    
        2.1. [Installation](#installation)    
        2.2. [Basic Usage](#usage)
<!--te-->


<a name="about"/></a>
## 1. About the Project

The approach focuses on generating language agnostic state-of-the-art 🤗 transformer embeddings for the list of string pairs (provided as an input) and measures performance by calculating the cosine similarity between the embeddings. The similarity scores range between [0, 1] with higher referring to better quality of translations.

The aim of this project is to create a quick and easy method for estimating the quality of translation of strings.

<a name="gettingstarted"/></a>
## 2. Getting Started 

<a name="installation"/></a>
###  2.1. Installation
**[PyTorch 1.2.0](https://pytorch.org/get-started/locally/)** or higher is recommended. If the install below gives an error, please install pytorch first [here](https://pytorch.org/get-started/locally/).

Installation can be done using [pypi](https://pypi.org/project/translation-quality-estimator/)

```
pip install translation-quality-estimator
```

<a name="usage"/></a>
###  2.2. Usage

The most minimal example can be seen below for translation quality estimation between two lists of strings:
```python
from tqe import TQE

lang_1 = ["what are you doing", "what is your name"]
lang_2 = ["तुम क्या कर रहे हो", "तुम्हारा नाम क्या है"]

model = TQE('LaBSE')
cos_sim_values = model.fit(lang_1, lang_2)
print(cos_sim_values)
```

**NOTE**: For a full overview of all possible multi-lingual transformer models see [sentence-transformer](https://www.sbert.net/docs/pretrained_models.html).
I would advise using `'LaBSE'` but you can also test out any `'XLM-R'` or `'Multilingual-BERT'` based models.

## License
[MIT](LICENSE)