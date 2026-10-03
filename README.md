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


## Demo

I maintain folders containing screenshots of C code snippets and
sections from the book I'm studying.

Here is Wordex output to it.

### Input
<img width="795" height="416" alt="5" src="https://github.com/user-attachments/assets/363c8b69-78e5-4357-94a0-8678bd151732" />
<br>
<img width="892" height="560" alt="4" src="https://github.com/user-attachments/assets/fbdf4140-da55-4045-8c0a-71c2b110ac47" />
<br>
### Output
<img width="644" height="609" alt="wor4" src="https://github.com/user-attachments/assets/266ee161-c3cd-4c11-9177-8298bb03f200" />
<br>
<img width="761" height="509" alt="wor3" src="https://github.com/user-attachments/assets/0a111e58-13c5-4415-b459-2013d2894606" />
<br>
<img width="665" height="660" alt="wor2" src="https://github.com/user-attachments/assets/19fb0f5a-8c3c-442b-bfac-4a08f9e56f77" />
<br>


There do are many mistakes, many missing character it is because of the OCR
but the thing is it works. we can change the OCR model in the future

The document structure have been handled pretty well by Wordex.
It was able to distinguish between heading,paragraphs,list and other blocks
and make a pretty neat word document
