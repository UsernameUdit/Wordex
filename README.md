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
