<h1 align="center">Wordex</h1>

<p align="center">
  <img width="566" height="349" alt="image" src="https://github.com/user-attachments/assets/70b55972-317e-4966-9e2e-764e0745cc20" />
</p>
<br>
<p align="center">
  <i>Johannes Gutenberg Invented Printing Press back in around 1440s.</i>
</p>

## Origin

The original `main.py` was written by me back in August.

I was making an imaginary scenario in my mind what if you had a lot of images with text you want to make a word document out of them?

At the time, I thought about two approaches:

- Send the images to an LLM/VLM.
- Process them locally.

My potato PC can't handle VLMs, so I went
with the OCR approach

I also happened to meet someone who had a tedious typing job,
which made me think that this could actually be useful.

So I wrote a small Python script using Tesseract OCR and
`python-docx` to turn images into Word documents.

A few days ago, Jev came out. I played around with it and started
thinking about this project again.

That led to `wordex_v1.py`

Jev isn't doing anything grand here. I'm mainly
experimenting with what happens when a decision model is placed
between OCR and document generation. I'll explain it below.

## Working and Usage

The working is pretty simple. You pass a filepath to an image or a folder to **wordex** as:

```bash
python wordex_v1.py C:/User/admin/Desktop/notes
```

Python calls **Tesseract OCR** and parses its TSV output to create blocks that can be passed to **Jev** to decide the semantics (is it a paragraph/heading/metadata etc.). Then, Python executes as per Jev confidence on a block of image.

## Usage

### Requirements
* Python
* Tesseract OCR
* The Python packages listed in `requirements.txt`
* A TypeSafe API key

Install the Python dependencies:

```bash
pip install -r requirements.txt
```


## Demo

I maintain folders containing screenshots of C code snippets and
sections from the book I'm studying.

Here is Wordex output to it.

### Input
<img width="48%" alt="5" src="https://github.com/user-attachments/assets/363c8b69-78e5-4357-94a0-8678bd151732" /> <img width="48%" alt="4" src="https://github.com/user-attachments/assets/fbdf4140-da55-4045-8c0a-71c2b110ac47" />
<br>
## Output
<div align="center">
  <img src="https://github.com/user-attachments/assets/266ee161-c3cd-4c11-9177-8298bb03f200" alt="wor4" width="80%" />
  <br><br>
  <img src="https://github.com/user-attachments/assets/0a111e58-13c5-4415-b459-2013d2894606" alt="wor3" width="80%" />
  <br><br>
  <img src="https://github.com/user-attachments/assets/19fb0f5a-8c3c-442b-bfac-4a08f9e56f77" alt="wor2" width="80%" />
</div>

There do are many mistakes, many missing character it is because of the OCR
but the thing is it works. we can change the OCR model in the future

The document structure have been handled pretty well by Wordex.
It was able to distinguish between heading,paragraphs,list and other blocks
and make a pretty neat word document
