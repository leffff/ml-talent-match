# Resume Analysis Model System, ml-talent-match

## Description
This project is designed to automate the processes of analyzing and evaluating resumes using cutting-edge natural language processing (NLP) approaches. The system consists of three key components:

1. **Resume Corpus Collection and Preprocessing**: The model was trained on a corpus of approximately 135,000 resumes collected from the internet.
2. **LaBSE (Language-agnostic BERT Sentence Embeddings)**: A multilingual model pretrained for feature extraction. It can be used to map 109 languages to a shared vector space.
3. **LoRA (Low-Rank Adaptation)**: An efficient fine-tuning method that doesn't require a significant increase in the number of model parameters.

## Components

### 01. Resume Corpus and LaBSE
We assembled a resume corpus and utilized LaBSE for "post-pretraining" the model, allowing it to adapt to the resume format.

### 02. LaBSE Fine-tuning
The LaBSE model underwent rigorous fine-tuning on our collected corpus to enhance the accuracy of named entity recognition.

### 03. LoRA Adapter
The use of LoRA enables model fine-tuning without a significant increase in parameter count, making it a "lighter" method compared to traditional approaches.

## Results
After fine-tuning LaBSE, our results show:
- Precision for named entity recognition: 0.94
- F1-score for named entity recognition: 0.95

## Application
The model can be used for automated processing and analysis of resumes in HR, improving job search and recommendation systems, and in other areas where resume information extraction is necessary.

## Repo
.py files:
* model.py - NERModel used for NER in the service
* preprocessing.py - preprocessor is used for cleaning the input string
* parser.py - ResumeParser our parser that can parse different data formats into text: doc, docx, pdf, md (useful for github), and even png and jpg images with OCR

.ipynb files:
* pretraining.ipynb - notebok for performing pretraining on large Resume Corpus
* finetuning.ipynb - notebok for model finetuning

## Contact
For additional information and inquiries, please contact us:

- Email: malbashich@yandex.ru, 
- Phone: +7 985 475 86 50

---

© MISiS University, ITAM, 2024.
