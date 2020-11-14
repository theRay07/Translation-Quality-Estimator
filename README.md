[![PyPI - Python](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8-blue.svg)]
[![PyPI - License](https://img.shields.io/badge/license-MIT-green.svg)]


# Translation-Quality-Estimator

Trnaslation Quality Estimator is a simple but powerful way of estimating the quality of translations in over a hundred languages.

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
[Back to ToC](#toc)

The approach focuses on generating language agnostic transformer based embeddings for the list of strings pairs (provided as an input) and measures performance by calculating the cosine similarity between the embeddings of the strings of a pair of languages.

This project is created as a quick and easy method for estimating the quality of translation of strings.

<a name="gettingstarted"/></a>
## 2. Getting Started
[Back to ToC](#toc)  

<a name="installation"/></a>
###  2.1. Installation
**[PyTorch 1.2.0](https://pytorch.org/get-started/locally/)** or higher is recommended. If the install below gives an
error, please install pytorch first [here](https://pytorch.org/get-started/locally/).

Installation can be done using [pypi]

```
pip install translation-quality-estimator
```

<a name="usage"/></a>
###  2.2. Usage

The most minimal example can be seen below for the extraction of keywords:
```python
from tqe import TQE

lang_1 = ["how are you", "what is you name"]
lang_2 = ["क्या हाल है", "तुम्हारा नाम क्या है"]

model = TQE('LaBSE')
cos_sim_values = model.fit(lang_1, lang_2)
```

**NOTE**: For a full overview of all possible transformer models see [sentence-transformer](https://www.sbert.net/docs/pretrained_models.html).
I would advise using `'LaBSE'` but you can also test out any XLM-R or Multilingual-BERT based models.